from django import template

from services.models import Sale

register = template.Library()


@register.simple_tag
def get_sales_status():
    # Проверка наличия акций
    return Sale.objects.filter(published=True).count()
