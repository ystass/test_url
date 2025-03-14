import random

from django.db import models

ALPHABET = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz234567890@#$_-*&^!'
LEN = 6


class ShortUrl(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        """
        При генерации короткой ссылки достаточно только полной ссылки,
        короткая ссылка генерируется автоматически.
        Перед сохранением объекта короткая ссылка проверяется на уникальность
        """
        if not self.short_url:
            while True:  # цикл будет повторять, до тех пор пока, не сгенерирует уникальную ссылку
                self.short_url = ''.join(
                    random.choices(
                        ALPHABET,  # алфавит для генерации короткой ссылки
                        k=LEN  # длина короткой ссылки
                    )
                )
                if not ShortUrl.objects.filter(  # проверка на уникальность
                        short_url=self.short_url
                ).exists():
                    break
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.full_url} -> {self.short_url}'

    class Meta:
        verbose_name = "url"
        verbose_name_plural = "urls"
