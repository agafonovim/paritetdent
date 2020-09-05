import datetime
from django import template
from django.utils import timezone

from about.models import Schedule

register = template.Library()


@register.simple_tag
def get_working_status():
    # Функция получения рабочего статуса на текущее время
    day_now = timezone.localtime().strftime("%A")
    now = timezone.localtime().time()

    try:
        schedule = Schedule.objects.get(day=day_now)
    except Schedule.DoesNotExist:
        return False

    if schedule.day_off:
        return False
    return schedule.opening_hours <= now <= schedule.closing_hours


@register.inclusion_tag('blocks/other/schedule.html')
def get_schedule():
    # Функция получения расписания работы
    schedule = Schedule.objects.all()
    day_now = timezone.localtime().strftime("%A")

    return {'schedule': schedule, "day_now": day_now}
