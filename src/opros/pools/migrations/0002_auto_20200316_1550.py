# Generated by Django 3.0.4 on 2020-03-16 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='answer',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный ключ'),
        ),
        migrations.AddField(
            model_name='question',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Уникальный ключ'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Запись удалена'),
        ),
        migrations.AlterField(
            model_name='pool',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Запись удалена'),
        ),
        migrations.AlterField(
            model_name='pool',
            name='limit',
            field=models.IntegerField(blank=True, default='0', verbose_name='Ограничение на количество  опрошенных'),
        ),
        migrations.AlterField(
            model_name='pool',
            name='password',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Пароль доступа к опросу'),
        ),
        migrations.AlterField(
            model_name='question',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Запись удалена'),
        ),
    ]