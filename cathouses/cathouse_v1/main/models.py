from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    opisanie = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукцию'
        verbose_name_plural = 'Продукция'