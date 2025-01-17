# Generated by Django 5.1 on 2024-08-21 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('user_id', models.BigIntegerField(null=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('language', models.CharField(choices=[('uz', 'Узбекский'), ('ru', 'Русский')], max_length=2, null=True)),
                ('banned', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('role', models.CharField(choices=[('courier', 'Курьер'), ('cook', 'Шеф-повар'), ('call_center', 'Колл-центр'), ('manager', 'Менеджер'), ('admin', 'Администратор'), ('ceo', 'Генеральный директор (CEO)')], max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
