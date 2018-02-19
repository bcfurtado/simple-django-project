from django.views.generic import ListView

from .models import Site


class SitesListView(ListView):
    model = Site
    context_object_name = 'sites'
