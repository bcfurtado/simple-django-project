from django.test import TestCase

from ..models import Site


class TestSitesListView(TestCase):

    def test_it_shows_message_when_there_is_no_sites_available_(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No sites available')

    def test_it_shows_the_site_name_when_there_is_site_available(self):
        Site.objects.create(name='Demo Site')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Demo Site')
