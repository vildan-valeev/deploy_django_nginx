from django.db import models


class Foo(models.Model):
    bar = models.CharField(max_length=300, null=True, verbose_name='Имя')

    class Meta:
        ordering = ['id']
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.bar
