from django.views.generic import ListView, DetailView

from .models import Site


class SitesListView(ListView):
    model = Site
    context_object_name = 'sites'


class SiteDetailView(DetailView):
    model = Site
    context_object_name = 'site'
