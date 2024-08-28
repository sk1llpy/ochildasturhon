# Generated by Django 5.1 on 2024-08-22 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
        ('orders', '0002_remove_order_foods_remove_order_user_delete_basket_and_more'),
        ('users', '0005_alter_staff_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Обновлено время')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Активен')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('rejected', 'rejected'), ('delivered', 'delivered')], default='pending', max_length=255)),
                ('location', models.CharField(choices=[('tinchlik', 'Tinchlik'), ('yunusabad', 'Yunusabad'), ('chilonzor_qutbinso', 'Chilonzor Qutbinso'), ('chilonzor_18', 'Chilonzor 18'), ('maksim_gorkiy', 'Maksim Gorkiy'), ('sergeli', 'Sergeli')], max_length=255, null=True)),
                ('foods', models.ManyToManyField(blank=True, to='orders.basket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
