from django.urls import path

from . import views


urlpatterns = [
    path('', views.SitesListView.as_view()),
]
