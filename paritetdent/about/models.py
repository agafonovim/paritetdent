import os

from django.db import models

from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.urls import reverse


class Schedule(models.Model):
    """
        Модель График работы
    """

    # День недели
    SCHEDULE_CHOICES = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресение')
    ]

    day = models.CharField(
        verbose_name="День недели",
        max_length=9,
        unique=True,
        choices=SCHEDULE_CHOICES
    )

    # Время открытия
    opening_hours = models.TimeField(
        verbose_name="Время открытия",
        default="09:00:00"
    )

    # Время закрытия
    closing_hours = models.TimeField(
        verbose_name="Время закрытия",
        default="21:00:00"
    )

    # Выходной
    day_off = models.BooleanField(
        verbose_name="Выходной",
        default=False
    )

    class Meta:
        verbose_name = "Часы работы"
        verbose_name_plural = "Часы работы"

    def __str__(self) -> str:
        return self.day


class Regulation(models.Model):
    """
        Модель Положения
    """

    # Название положения
    title = models.CharField(
        verbose_name="Название",
        max_length=512,
        unique=True
    )

    # Слаг для SEO
    slug = models.SlugField(
        unique=True,
        help_text="Авто-заполняемое поле, руками не трогать! :)"
    )

    # Текст положения
    text = RichTextField(
        verbose_name="Название",
        unique=True
    )

    # Дата последнего изменения
    modified_date = models.DateField(
        verbose_name="Дата последнего изменения",
        auto_now=True
    )

    def get_absolute_url(self):
        return reverse('about:regulation_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Положение"
        verbose_name_plural = "Положения"

    def __str__(self) -> str:
        return self.title


class License(models.Model):
    """
        Модель Положения
    """

    # Название положения
    title = models.CharField(
        verbose_name="Название",
        max_length=512,
        unique=True
    )

    # Изображение
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="license",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Файл лицензии"
        verbose_name_plural = "Файлы лицензии"

    def __str__(self) -> str:
        return self.title
