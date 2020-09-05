from django.urls import path

from . import views

app_name = 'about'
urlpatterns = [
    path('regulations/<slug:slug>', views.RegulationDetailView.as_view(), name='regulation_detail'),
    path('about', views.AboutView.as_view(), name='about'),
    path('', views.MainPageView.as_view(), name='index'),
]