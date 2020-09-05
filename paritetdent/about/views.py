from django.views.generic import DetailView, TemplateView

from .models import Regulation, License
from services.models import Classification


class RegulationDetailView(DetailView):
    """ Полный текст положения """
    model = Regulation


class AboutView(TemplateView):
    """ О клинике """
    template_name = "about/about_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regulations'] = Regulation.objects.all()
        context['licence'] = License.objects.all()

        return context


class MainPageView(TemplateView):
    """ Главная страница """
    template_name = "about/main-page_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Classification.objects.filter(show=True)[:4]

        return context
