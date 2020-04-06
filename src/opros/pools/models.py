import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Pool(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    uuid = models.UUIDField(
        u'Уникальный ключ',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        u'Название',
        default='',
        max_length=250,
    )
    date_created = models.DateField(
        u'Дата добавления опроса',
        auto_now_add=True,
    )
    date_start = models.DateTimeField(
        u'Дата начала опроса',
        auto_now_add=True,
    )
    date_end = models.DateTimeField(
        u'Дата окончания опроса',
        blank=True,
        null=True,
    )
    password = models.CharField(
        u'Пароль доступа к опросу',
        default='',
        blank=True,
        max_length=50,
    )
    limit = models.IntegerField(
        u'Ограничение на количество  опрошенных',
        blank=True,
        default='0',
    )
    comments = models.NullBooleanField(
        u'Разрешить комментарии',
        default=True
    )
    deleted = models.BooleanField(
        u'Запись удалена',
        default=False
    )

    def __str__(self):
        return '<Pool %s>' % self.uuid

    class Meta:
        ordering = ('date_created',)
        verbose_name = u'Опрос'
        verbose_name_plural = u'Опросы'


class Question(models.Model):
    pool = models.ForeignKey(Pool, on_delete=models.DO_NOTHING)
    uuid = models.UUIDField(
        u'Уникальный ключ',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date_created = models.DateTimeField(
        u'Дата добавления вопроса',
        auto_now_add=True
    )
    title = models.CharField(
        u'Текст вопроса',
        default='',
        max_length=250
    )
    order = models.IntegerField(
        u'Порядок сортировки в опросе',
        default=1
    )
    deleted = models.BooleanField(
        u'Запись удалена',
        default=False
    )

    def __str__(self):
        return '<Question %s>' % self.uuid

    def total_count(self):
        return self.useranswer_set.all().count()

    class Meta:
        ordering = ('pool', 'date_created',)
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    uuid = models.UUIDField(
        u'Уникальный ключ',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date_created = models.DateTimeField(
        u'Дата добавления ответа',
        auto_now_add=True
    )
    title = models.CharField(
        u'Текст ответа',
        default='',
        max_length=250
    )
    link = models.CharField(
        u'Ссылка на вариант ответа',
        default='',
        blank=True,
        max_length=250
    )
    deleted = models.BooleanField(
        u'Запись удалена',
        default=False
    )

    def __str__(self):
        return '<Answer %s>' % self.uuid

    def ua_count(self):
        return self.useranswer_set.all().count()

    def ua_persent(self):
        return int(self.ua_count() * 100 / self.question.total_count())

    class Meta:
        ordering = ('question', 'date_created',)
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, default='', on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answer, default='', on_delete=models.DO_NOTHING)
    uuid = models.UUIDField(
        u'Уникальный ключ',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    useragent = models.CharField(
        u'Агент',
        default='',
        blank=True,
        max_length=250
    )
    ipaddress = models.CharField(
        u'Адрес',
        default='',
        blank=True,
        max_length=16
    )
    date_created = models.DateTimeField(
        u'Дата добавления ответа',
        auto_now_add=True
    )

    def __str__(self):
        return '<UserAnswer %s>' % self.uuid

    class Meta:
        ordering = ('date_created',)
        verbose_name = u'Ответ пользователя'
        verbose_name_plural = u'Ответы пользователей'
