from django.db import models

from django.urls import reverse


class Job(models.Model):
    """
        Модель Вакансии
    """

    # Должность
    position = models.CharField(
        verbose_name="Должность",
        unique=True,
        max_length=256
    )

    # Слаг для SEO
    slug = models.SlugField(
        unique=True,
        help_text="Авто-заполняемое поле, руками не трогать! :)"
    )

    # График работы
    SCHEDULE_CHOICES = [
        ('П', 'Полный рабочий день'),
        ('У', 'Удаленная работа'),
        ('Г', 'Гибкий график'),
        ('С', 'Сменный график')
    ]
    schedule = models.CharField(
        verbose_name="График работы",
        max_length=1,
        choices=SCHEDULE_CHOICES
    )

    # Требуемый опыт
    experience = models.CharField(
        max_length=128,
        verbose_name="Опыт",
        help_text="Пример: от 2 до 3 лет"
    )

    # Зарплата
    salary = models.CharField(
        max_length=128,
        verbose_name="Заработная плата",
        help_text="Пример: от 2.000 рублей в месяц"
    )

    # Требования кандидата
    requirements = models.TextField(
        verbose_name="Требования"
    )

    # Условия работы
    conditions = models.TextField(
        verbose_name="Условия работы"
    )

    # Получение URL
    def get_absolute_url(self):
        return reverse('jobs:job_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self) -> str:
        return self.position


class Application(models.Model):
    """
        Модель Заявки
    """

    # Должность
    position = models.ForeignKey(
        Job,
        verbose_name="Должность",
        on_delete=models.CASCADE
    )

    # Имя кандидата
    name = models.CharField(
        max_length=128,
        verbose_name="Имя"
    )

    # Электронная почта
    email = models.EmailField(
        verbose_name="Электронная почта"
    )

    # Номер телефона
    phone = models.CharField(
        max_length=18,
        verbose_name="Номер телефона"
    )

    # О себе
    about = models.TextField(
        max_length="2048",
        verbose_name="О себе"
    )

    class Meta:
        verbose_name = "Отклик на вакансию"
        verbose_name_plural = "Отклики на вакансии"

    def __str__(self) -> str:
        return self.name
