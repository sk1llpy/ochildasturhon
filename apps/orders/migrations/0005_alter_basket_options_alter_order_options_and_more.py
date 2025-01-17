# Generated by Django 5.1 on 2024-08-22 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
        ('orders', '0004_remove_order_foods_orderfood'),
        ('users', '0006_alter_staff_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderfood',
            options={'verbose_name': 'Блюдо в заказе', 'verbose_name_plural': 'Блюда в заказе'},
        ),
        migrations.AlterField(
            model_name='basket',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='order',
            name='location',
            field=models.CharField(choices=[('tinchlik', 'Tinchlik'), ('yunusabad', 'Yunusabad'), ('chilonzor_qutbinso', 'Chilonzor Qutbinso'), ('chilonzor_18', 'Chilonzor 18'), ('maksim_gorkiy', 'Maksim Gorkiy'), ('sergeli', 'Sergeli')], max_length=255, null=True, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('rejected', 'rejected'), ('delivered', 'delivered')], default='pending', max_length=255, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='orderfood',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foods.food', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='orderfood',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ'),
        ),
    ]
