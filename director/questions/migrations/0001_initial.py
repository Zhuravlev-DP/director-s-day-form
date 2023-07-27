# Generated by Django 2.2.19 on 2023-07-26 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Топливный', 'Топливный'), ('Машиностроение', 'Машиностроение'), ('ЯОК', 'ЯОК'), ('Энергетический', 'Энергетический')], max_length=50, verbose_name='Название дивизиона')),
            ],
            options={
                'verbose_name': 'Дивизион',
                'verbose_name_plural': 'Дивизионы',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название предприятия')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enterprise', to='questions.Division', verbose_name='Дивизион')),
            ],
            options={
                'verbose_name': 'Предприятие',
                'verbose_name_plural': 'Предприятия',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата время вопроса')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('enterprise', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='questions.Enterprise', verbose_name='Предприятие')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-pub_date'],
            },
        ),
    ]