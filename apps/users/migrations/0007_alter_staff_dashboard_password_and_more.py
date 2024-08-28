# Generated by Django 5.1 on 2024-08-22 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_staff_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='dashboard_password',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Пароль в панели'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='dashboard_username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя пользователя в панели'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('cook', 'Шеф-повар'), ('manager', 'Менеджер'), ('ceo', 'Генеральный директор (CEO)')], max_length=255, null=True, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_set', to='users.user', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='user',
            name='banned',
            field=models.BooleanField(default=False, verbose_name='Заблокирован'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('uz', 'Узбекский'), ('ru', 'Русский')], max_length=2, null=True, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=255, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.BigIntegerField(null=True, verbose_name='Идентификатор пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя пользователя'),
        ),
    ]