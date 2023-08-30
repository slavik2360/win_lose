from django.db import models
from auths.models.my_user import MyUser

class ActivationCode(models.Model):
    user = models.OneToOneField(
        verbose_name='пользователь',
        related_name='code',
        to=MyUser,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        verbose_name='код',
        unique=True,
        max_length=200
    )
    is_active = models.BooleanField(
        verbose_name='активный?',
        default=True
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания',
        auto_created=True,
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Код',
        verbose_name_plural = 'Коды активации'