from django.urls import path

from . import views


urlpatterns = [
    path('', views.SitesListView.as_view(), name='sites-list'),
    path('<int:pk>', views.SiteDetailView.as_view(), name='site-detail'),
]
