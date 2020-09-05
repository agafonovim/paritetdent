from django.forms import ModelForm, TextInput, Textarea, EmailInput, Select
from django.utils.translation import gettext_lazy as _

from .models import Application


class ApplicationForm(ModelForm):
    """
        Форма заявки на вакансию
    """
    class Meta:
        model = Application
        fields = ('name', 'position', 'email', 'phone', 'about')
        widgets = {
            'name': TextInput(attrs={"placeholder": "Ваше имя", "id": "name"}),
            'position': Select({"id": "position"}),
            'email': EmailInput(attrs={"placeholder": "Ваш email", "id": "email"}),
            'phone': TextInput(attrs={"placeholder": "+7 (", "id": "phone", "type": "tel"}),
            'about': Textarea(attrs={"placeholder": "Расскажите о себе в свободной форме", "id": "about"}),
        }
        labels = {
            'name': 'Как вас зовут?',
            'position': 'Выберите вакансию:',
            'phone': 'Телефон для связи',
            'email': 'Электронная почта',
            'about': 'Коротко о себе',
        }
