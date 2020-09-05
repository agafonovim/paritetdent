from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Pricelist, Sale, Classification, Service, Appointment


@admin.register(Pricelist)
class PricelistAdmin(ImportExportModelAdmin):
    # Отображение формы прайс-листа
    readonly_fields = ('modified_date',)
    fieldsets = [
        (None, {
            'fields':
                [
                    'stomatology',
                    'order',
                    'number',
                    'title',
                    'price',
                    'modified_date'
                ]
        })
    ]

    # Отображение списка цен
    list_filter = ('stomatology', )
    list_display = ('order', 'stomatology', 'number', 'title', 'price')
    search_fields = ('order', 'number', 'title', 'price')
    ordering = ['order']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    # Отображение списка акций
    list_display = ('title', 'constantly', 'published')
    ordering = ['expiration_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # Отображение списка услуг
    list_filter = ('classification', )
    list_display = ('title', 'text', 'classification')
    ordering = ['classification']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # Отображение формы записи
    readonly_fields = ('name', 'phone', 'creation_date')
    fieldsets = [
        (None, {
            'fields':
                [
                    'name',
                    'phone',
                    'text',
                    'call',
                    'creation_date',
                ]
        })
    ]

    # Отображение списка записи
    list_filter = ('call', )
    list_display = ('phone', 'name', 'text', 'call', 'creation_date')
    search_fields = ('name', 'phone')
    ordering = ['creation_date']


admin.site.register(Classification)  # Отображение классификаций
