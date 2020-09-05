from django.views.generic import ListView

from .models import Workers


class WorkersListView(ListView):
    """ Список работников """
    model = Workers

