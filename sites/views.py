from django.db.models import Sum
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
