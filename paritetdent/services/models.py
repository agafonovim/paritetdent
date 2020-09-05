import os

from django.db import models

from ckeditor.fields import RichTextField
from django.dispatch import receiver


class Pricelist(models.Model):
    """
        Модель Прайслист
    """

    # Вид стоматологической помощи
    STOMATOLOGY_CHOICES = [
        ('ОБ', 'Общие виды работ '),
        ('Т', 'Стоматология терапевтическая'),
        ('Д', 'Детская стоматология'),
        ('ОР', 'Стоматология ортопедическая'),
        ('Х', 'Хирургическая стоматология')
    ]
    stomatology = models.CharField(
        verbose_name="Вид стоматологической помощи",
        max_length=2,
        choices=STOMATOLOGY_CHOICES
    )

    order = models.CharField(
        verbose_name="Номер по порядку",
        max_length=24
    )

    # Код услуги по номенклатуре
    number = models.CharField(
        verbose_name="Код услуги",
        max_length=32
    )

    # Наименование услуги
    title = models.CharField(
        verbose_name="Наименование услуги",
        max_length=256
    )

    # Цена
    price = models.FloatField(
        verbose_name="Цена",
        help_text="Цена услуги в рублях"
    )

    # Дата последнего изменения
    modified_date = models.DateField(
        verbose_name="Дата последнего изменения",
        auto_now=True
    )

    class Meta:
        verbose_name = "Цена услуги"
        verbose_name_plural = "Цены услуг"

    def __str__(self) -> str:
        return self.title


class Sale(models.Model):
    """
        Модель Акции
    """

    # Заголовок
    title = models.CharField(
        verbose_name="Заголовок",
        unique=True,
        max_length=256
    )

    # Описание
    text = RichTextField(
        verbose_name="Описание"
    )

    # Постоянство
    constantly = models.BooleanField(
        verbose_name="Действует постоянно"
    )

    # Дата окончания дейтсвия акции
    expiration_date = models.DateField(
        verbose_name="Действует до",
        help_text="Укажите любую дату, если скидка постоянная",
        null=False,
        blank=False
    )

    # Опубликовано
    published = models.BooleanField(
        verbose_name="Опубликовано",
        default=0
    )

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self) -> str:
        return self.title


class Classification(models.Model):
    """
        Модель Классицикация услуг
    """

    # Заголовок
    title = models.CharField(
        verbose_name="Заголовок",
        unique=True,
        max_length=256
    )

    # Изображение
    image = models.FileField(
        verbose_name="Изображение",
        upload_to="classifications",
        null=True,
        blank=True
    )

    # Отображение на главной
    show = models.BooleanField(
        verbose_name="Отображение на главной",
        help_text="Максимум 4 элемента",
        default=False
    )

    class Meta:
        verbose_name = "Направление лечения"
        verbose_name_plural = "Направления лечения"

    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    """
        Модель Услуга
    """

    # Заголовок
    title = models.CharField(
        verbose_name="Название",
        max_length=256
    )

    # Краткое описание
    text = models.TextField(
        verbose_name="Краткое описание",
        null=True,
        blank=True
    )

    # Направление
    classification = models.ForeignKey(
        Classification,
        verbose_name="Классификация услуги",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self) -> str:
        return self.title


class Appointment(models.Model):
    """
        Модель Записи на приём
    """

    # Имя
    name = models.CharField(
        verbose_name="Имя клиента",
        max_length=256,
        blank=True
    )

    # Номер телефона
    phone = models.CharField(
        max_length=18,
        verbose_name="Номер телефона"
    )

    # Краткое описание
    text = models.TextField(
        verbose_name="Описание проблемы",
        max_length=512,
        blank=True
    )

    # Статус звонка
    call = models.BooleanField(
        verbose_name="Диалог состоялся",
        default=False
    )

    # Дата заявки
    creation_date = models.DateTimeField(
        verbose_name="Дата подачи заявки",
        auto_now=True
    )

    class Meta:
        verbose_name = "Заявка на запись"
        verbose_name_plural = "Заявки на запись"

    def __str__(self) -> str:
        return self.name or 'Клиент'
