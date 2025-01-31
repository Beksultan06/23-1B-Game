from django.db import models
from ckeditor.fields import RichTextField

from app.settings.icon import ICON

# Create your models here.
class Banner(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    title2 = models.CharField(
        max_length=155,
        verbose_name='Заголовка 2'
    )
    imgae = models.ImageField(
        upload_to='banner/',
        verbose_name='Фото'
    )
    video = models.URLField(
        verbose_name='Ссылка на видео'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройка Баннера в Главной Страницы'

class Settings(models.Model):
    title_game = models.CharField(
        max_length=155,
        verbose_name='Заголовка Игры'
    )
    descriptions_game = RichTextField(
        verbose_name='Описание игры'
    )
    title_match = models.CharField(
        max_length=155,
        verbose_name='Заголовка Мачт'
    )
    description_match = RichTextField(
        verbose_name="Описание Матч"
    )
    title_team = models.CharField(
        max_length=155,
        verbose_name='Заголовка  Команды'
    )
    description_team = RichTextField(
        verbose_name="Описание  Команды"
    )
    title_news = models.CharField(
        max_length=155,
        verbose_name='Заголовка  Новости'
    )
    description_news = RichTextField(
        verbose_name="Описание  Новости"
    )

    def __str__(self):
        return self.title_game

    class Meta:
        verbose_name_plural = 'Настройка Главной Страницы'


class Contact(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField()
    icon = models.CharField(
        max_length=50,
        choices=ICON
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Контакты'

class ContactFrom(models.Model):
    name = models.CharField(
        max_length=155
    )
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Обраная связ'