from django.contrib import admin

# Register your models here.
from .models import Workers
from .models import Positions

admin.site.register(Positions)


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    # Отображение формы
    readonly_fields = ('creation_date',)
    filter_horizontal = ('position',)
    fieldsets = [
        (None, {
            'fields':
                [
                    'surname',
                    'name',
                    'patronymic',
                    'sex'
                ]
        }),
        ('Рабочая информация', {
            'fields':
                [
                    'position',
                    'experience',
                    'description',
                    'creation_date'
                ]
        }),
    ]
    # Отображение списка
    list_display = ['surname', 'experience', 'creation_date']
    search_fields = ['surname', 'name', 'patronymic']
