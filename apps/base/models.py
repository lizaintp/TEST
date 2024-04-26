from django.db import models

# Create your models here.

class Settings(models.Model):
    is_eighteen = models.BooleanField(
        verbose_name='Вам есть 18?',
        default=False
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название сайта'
    )
    description = models.TextField(
        verbose_name='Описание сайта'
    )
    instagram = models.URLField(
        verbose_name='Инстаграм'
    )
    telegram = models.URLField(
        verbose_name='Телеграм'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '1)Основная настройка'
        verbose_name_replue = '1)Основные настройки'
        

  