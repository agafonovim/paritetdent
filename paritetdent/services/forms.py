from django.forms import ModelForm, TextInput, Textarea, EmailInput, Select
from django.utils.translation import gettext_lazy as _

from .models import Appointment


class AppointmentForm(ModelForm):
    """
        Форма записи на приём
    """
    class Meta:
        model = Appointment
        fields = ('name', 'phone', 'text')
        widgets = {
            'name': TextInput(attrs={"placeholder": "Ваше имя", "id": "name"}),
            'phone': TextInput(attrs={"placeholder": "+7 (", "id": "phone", "type": "tel"}),
            'text': Textarea(attrs={"rows": "4", "placeholder": "Укажите, если надо позвонить в определенное время", "id": "text"}),
        }
        labels = {
            'name': 'Как вас зовут?',
            'phone': 'Телефон для связи',
            'text': 'Комментарий',
        }
