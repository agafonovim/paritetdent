from django.views.generic import ListView, FormView

from .models import Sale, Service, Classification, Pricelist
from .forms import AppointmentForm


class SalesListView(ListView):
    """ Список акций """
    model = Sale
    queryset = Sale.objects.filter(published=True).order_by('expiration_date')


class ServicesListView(ListView):
    """ Список услуг """
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classifications'] = Classification.objects.all()
        return context


class PricelistListView(ListView):
    """ Прайс-лист """
    model = Pricelist
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['last_modified'] = Pricelist.objects.latest('modified_date')
        except Pricelist.DoesNotExist:
            context['last_modified'] = None

        return context


class AppointmentFormView(FormView):
    """ Форма записи """
    template_name = 'forms/appointment_form.html'
    form_class = AppointmentForm
    success_url = '/thanks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
