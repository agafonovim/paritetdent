from django.contrib import admin

from .models import Schedule, Regulation, License


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    # Отображение режима работы
    list_display = ('day', 'opening_hours', 'closing_hours', 'day_off')


@admin.register(Regulation)
class RegulationsAdmin(admin.ModelAdmin):
    # Отображение формы положений
    readonly_fields = ('modified_date',)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {
            'fields':
                [
                    'title',
                    'slug',
                    'text',
                    'modified_date'
                ]
        })
    ]

    # Отображение списка
    list_display = ('title', 'modified_date')
    search_fields = ('title',)
    ordering = ['title']


admin.site.register(License)  # Отображение лицензий
