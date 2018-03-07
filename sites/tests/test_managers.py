from decimal import Decimal

from django.test import TestCase

from ..models import Site, SiteEntry


class TestSiteManager(TestCase):

    def test_it_returns_all_data_aggregated_by_sum(self):
        site = Site.objects.create(name='Demo Site')
        SiteEntry.objects.create(site=site, value_a=12.00, value_b=16.00)
        SiteEntry.objects.create(site=site, value_a=20.00, value_b=100.00)
        SiteEntry.objects.create(site=site, value_a=20.00, value_b=80.00)

        sites = Site.objects.all_with_sum_data()

        self.assertEqual(sites[0].value_a, Decimal('52.00'))
        self.assertEqual(sites[0].value_b, Decimal('196.00'))

    def test_it_returns_all_data_aggregated_by_avg(self):
        site = Site.objects.create(name='Demo Site')
        SiteEntry.objects.create(site=site, value_a=12.00, value_b=16.00)
        SiteEntry.objects.create(site=site, value_a=20.00, value_b=100.00)
        SiteEntry.objects.create(site=site, value_a=20.00, value_b=80.00)

        sites = Site.objects.all_with_average_data()

        self.assertAlmostEqual(sites[0].value_a, 17.33, places=2)
        self.assertAlmostEqual(sites[0].value_b, 65.33, places=2)
