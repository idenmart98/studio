from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

DEFAULT = 'DEFAULT'
ACCOUNTANT = 'ACCOUNTANT'
LINE_PRODUCER = 'LINE_PRODUCER'
PRODUCER = 'PRODUCER'
EXECUTIVE_PRODUCER = 'EXECUTIVE_PRODUCER'
BUYER = 'BUYER'


USER_GROUP = (
    (DEFAULT, 'По умолчанию'),
    (ACCOUNTANT, 'Бухгалтер'),
    (LINE_PRODUCER, 'Линейный продюсер'),
    (PRODUCER, 'Продюсер'),
    (EXECUTIVE_PRODUCER, 'Исполнительный продюсер'),
    (BUYER, 'Закупщик'),
)


class UserGroup(models.Model):
    name = models.CharField(
        max_length=20, verbose_name='Имя Группы', choices=USER_GROUP, default='DEFAULT'
    )
    user = models.ManyToManyField(
        User, verbose_name='Пользователи',
        related_name='user_groups'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'