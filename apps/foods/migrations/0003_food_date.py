# Generated by Django 5.1 on 2024-08-23 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_food_image_alter_food_price_alter_food_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
