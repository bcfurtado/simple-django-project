from django.db import models


class SiteManager(models.Manager):
    def all_with_sum_data(self):
        return self.annotate(
            value_a=models.Sum('siteentry__value_a'),
            value_b=models.Sum('siteentry__value_b'),
        )

    def all_with_average_data(self):
        sql = '''
        SELECT
          sites_site.id,
          sites_site.name,
          avg(sites_siteentry.value_a) as value_a,
          avg(sites_siteentry.value_b) as value_b
        FROM
          sites_site
        LEFT JOIN
          sites_siteentry ON sites_site.id == sites_siteentry.site_id
        GROUP BY
          sites_site.id;
        '''
        return self.raw(sql)
