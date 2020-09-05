from django.urls import path

from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('application', views.ApplicationFormView.as_view(), name='application'),
    path('<slug:slug>', views.JobDetailView.as_view(), name='job_detail'),
]