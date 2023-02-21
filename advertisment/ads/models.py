from django.db import models


class Ads(models.Model):  # модель, которая отвечает за объявления, связь один ко многим с рубрикой
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    def __str__(self):  # как будет передаваться название
        return self.title

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

    objects = models.Manager  # необходимо для работы в community версии


class Rubric(models.Model):  # модель, которая отвечает за рубрики
    name = models.CharField(max_length=30, db_index=True, verbose_name='Рубрика')

    def __str__(self):
        return self.name

    objects = models.Manager

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']


