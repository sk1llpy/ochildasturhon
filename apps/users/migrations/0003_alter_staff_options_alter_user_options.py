# Generated by Django 5.1 on 2024-08-22 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_staff_dashboard_password_staff_dashboard_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Сотрудники', 'verbose_name_plural': 'Сотрудник'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователи', 'verbose_name_plural': 'Пользователь'},
        ),
    ]
