from django.views.generic import ListView, DetailView, FormView

from .models import Job
from .forms import ApplicationForm


class JobDetailView(DetailView):
    """ Подробное описание вакансии """
    model = Job


class JobListView(ListView):
    """ Список вакансий """
    model = Job


class ApplicationFormView(FormView):
    """ Форма отклика на вакансию """
    template_name = 'forms/application_form.html'
    form_class = ApplicationForm
    success_url = '/thanks'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
