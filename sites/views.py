from django.db.models import Sum, Avg
from django.views.generic import ListView, DetailView

from .models import Site


class SitesListView(ListView):
    model = Site
    context_object_name = 'sites'


class SiteDetailView(DetailView):
    model = Site
    context_object_name = 'site'


class SummarySumView(ListView):
    model = Site
    context_object_name = 'sites'
    template_name = 'sites/site_summary_sum_list.html'

    def get_queryset(self):
        return Site.objects.annotate(
            value_a=Sum('siteentry__value_a'),
            value_b=Sum('siteentry__value_b'),
        )


class SummaryAverageView(ListView):
    model = Site
    context_object_name = 'sites'
    template_name = 'sites/site_summary_average_list.html'

    def get_queryset(self):
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

        return Site.objects.raw(sql)
