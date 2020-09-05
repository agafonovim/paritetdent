from django.urls import path

from . import views

app_name = 'workers'
urlpatterns = [
    path('team', views.WorkersListView.as_view(), name='workers_list'),
]