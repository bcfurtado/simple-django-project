from django.test import TestCase

from ..models import Site


class TestSitesView(TestCase):

    def test_it_str_returns_the_site_name(self):
        site = Site(name='Demo Site')
        self.assertEqual(str(site), 'Demo Site')

    def test_it_the_default_order_field_is_name(self):
        Site.objects.create(name='Site L')
        Site.objects.create(name='Site Z')
        Site.objects.create(name='Site E')

        sites = Site.objects.all()

        self.assertEqual(str(sites[0]), 'Site E')
        self.assertEqual(str(sites[1]), 'Site L')
        self.assertEqual(str(sites[2]), 'Site Z')
