from django.test import TestCase

from ..models import Site, SiteEntry


class TestSitesListView(TestCase):

    def test_it_shows_message_when_there_is_no_sites_available(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No sites available')

    def test_it_shows_the_site_name_when_there_is_site_available(self):
        Site.objects.create(name='Demo Site')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Demo Site')


class TestSiteDetailView(TestCase):

    def test_it_shows_site_name_on_site_detail_page(self):
        site = Site.objects.create(name='Demo Site')
        response = self.client.get('/sites/{}'.format(site.id))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Demo Site')

    def test_it_shows_message_when_there_is_no_site_entries(self):
        site = Site.objects.create(name='Demo Site')
        response = self.client.get('/sites/{}'.format(site.id))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No sites available')

    def test_it_shows_site_details_when_there_is_site_entries(self):
        site = Site.objects.create(name='Demo Site')
        SiteEntry.objects.create(site=site, value_a=12.00, value_b=16.00)
        response = self.client.get('/sites/{}'.format(site.id))

        self.assertContains(response, '12.00', status_code=200)


class TestSummaryView(TestCase):

    def setUp(self):
        site = Site.objects.create(name='Demo Site')
        SiteEntry.objects.create(site=site, value_a=12.00, value_b=16.00)
        SiteEntry.objects.create(site=site, value_a=20.00, value_b=100.00)
        SiteEntry.objects.create(site=site, value_a=20.00, value_b=80.00)

    def test_it_shows_site_sum_summary_data(self):
        response = self.client.get('/summary')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Demo Site')
        self.assertContains(response, '52.00')
        self.assertContains(response, '196.00')

    def test_it_shows_site_average_summary_data(self):
        response = self.client.get('/summary-average')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Demo Site')
        self.assertContains(response, '17.33')
        self.assertContains(response, '65.33')
