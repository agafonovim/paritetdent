from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

app_name = 'services'
urlpatterns = [
    path('sales', views.SalesListView.as_view(), name='sales_list'),
    path('services', views.ServicesListView.as_view(), name='services_list'),
    path('pricelist', views.PricelistListView.as_view(), name='pricelist_list'),
    path('appointment', views.AppointmentFormView.as_view(), name='appointment_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)