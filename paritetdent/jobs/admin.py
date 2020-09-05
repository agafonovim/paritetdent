from django.contrib import admin


from .models import Job, Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    # Отображение формы работы
    prepopulated_fields = {'slug': ('position',)}
    fieldsets = [
        (None, {
            'fields':
                [
                    'position',
                    'slug',
                    'schedule',
                    'experience',
                    'salary'
                ]
        }),
        ('Рабочий процесс', {
            'fields':
                [
                    'requirements',
                    'conditions'
                ]
        }),
    ]
    # Отображение списка работ
    list_display = ('position', 'schedule', 'experience', 'salary')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ['position', 'name', 'email', 'phone', 'about']
    # Отображение формы заявлений
    fieldsets = [
        (None, {
            'fields':
                [
                    'position',
                    'name',
                    'email',
                    'phone',
                    'about'
                ]
        }),
    ]
    # Отображение списка заявлений
    list_display = ('position', 'name', 'email', 'phone')
