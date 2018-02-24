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
        return Site.objects.all_with_sum_data()


class SummaryAverageView(ListView):
    model = Site
    context_object_name = 'sites'
    template_name = 'sites/site_summary_average_list.html'

    def get_queryset(self):
        return Site.objects.all_with_average_data()
