from django.urls import path

from . import views


urlpatterns = [
    path('sites/', views.SitesListView.as_view(), name='sites-list'),
    path('sites/<int:pk>', views.SiteDetailView.as_view(), name='site-detail'),
    path('summary', views.SummarySumView.as_view(), name='site-summary-sum'),
    path('summary-average', views.SummaryAverageView.as_view(), name='site-summary-avg'),
    path('', views.SitesListView.as_view(), name='index'),
]
