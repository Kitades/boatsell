# Generated by Django 5.1.1 on 2024-09-19 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год выпуска')),
            ],
            options={
                'verbose_name': 'Лодка',
                'verbose_name_plural': 'Лодки',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владельцы',
            },
        ),
        migrations.CreateModel(
            name='BoatHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='владел c')),
                ('stop_year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='владел пo')),
                ('boat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.boat', verbose_name='Лодка')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boat.owner', verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'История владения',
                'verbose_name_plural': 'Истории владения',
            },
        ),
        migrations.AddField(
            model_name='boat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.owner', verbose_name='Владелец'),
        ),
    ]
