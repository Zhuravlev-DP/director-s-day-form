from django.db import models


DIVISION_CHOICES = (
    ('Топливный', 'Топливный'),
    ('Машиностроение', 'Машиностроение'),
    ('ЯОК', 'ЯОК'),
    ('Энергетический', 'Энергетический'),
)
MAX_LENGHT = 50


class Division(models.Model):
    title = models.CharField(
        max_length=MAX_LENGHT,
        choices=DIVISION_CHOICES,
        verbose_name='Название дивизиона'
    )

    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'Дивизионы'

    def __str__(self):
        return self.title


class Enterprise(models.Model):
    title = models.CharField(
        max_length=MAX_LENGHT,
        blank=True,
        verbose_name='Название предприятия'
    )
    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        related_name='enterprise',
        verbose_name='Дивизион'
    )

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'

    def __str__(self):
        return self.title


class Question(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата время вопроса'
    )
    enterprise = models.ForeignKey(
        Enterprise,
        blank=True,
        on_delete=models.CASCADE,
        related_name='question',
        verbose_name='Предприятие'
    )
    text = models.TextField(verbose_name='Текст вопроса')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text
