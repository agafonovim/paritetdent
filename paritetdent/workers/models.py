from django.db import models


# Create your models here.
class Positions(models.Model):
    """
        Модель Должности
    """

    # Должность
    title = models.CharField(
        max_length=512,
        verbose_name="Название"
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self) -> str:
        return self.title


class Workers(models.Model):
    """
        Модель Сотрудники
    """

    # Фамилия
    surname = models.CharField(
        max_length=128,
        verbose_name="Фамилия"
    )

    # Имя
    name = models.CharField(
        max_length=128,
        verbose_name="Имя"
    )

    # Отчество
    patronymic = models.CharField(
        max_length=128,
        verbose_name="Отчество"
    )

    # Пол
    GENDER = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина')
    ]
    sex = models.CharField(
        verbose_name="Пол",
        max_length=1,
        choices=GENDER
    )

    # Должность
    position = models.ManyToManyField(
        Positions,
        verbose_name="Должность",
        help_text="Зажмите 'Ctrl' или 'Command' на Mac, чтобы выбрать несколько должностей."
    )

    # Описание
    description = models.TextField(
        verbose_name="Описание"
    )

    # Стаж
    experience = models.CharField(
        verbose_name="Стаж работы",
        max_length=32,
        help_text="Пример: 10 лет"
    )

    # Дата добавления сотрудника
    creation_date = models.DateField(
        verbose_name="Дата добавления",
        auto_now_add=True,
        help_text="Дата добавления сотрудника"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self) -> str:
        return "%s %s %s" % (self.surname, self.name, self.patronymic)
