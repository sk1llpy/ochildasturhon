from django.db import models
from apps.general.models import BaseModel
from apps.general.utils.uploaders import food_uploader_directory

# Create your models here.
class Food(BaseModel):
    title = models.CharField(max_length=255, null=True, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, upload_to=food_uploader_directory, verbose_name='Изображение')
    date = models.DateField(null=True, blank=True)
    price = models.IntegerField(null=True, verbose_name='Цена')
    
    def __str__(self):
        return f"{self.title} | {self.price} сум"
    
    class Meta:
        verbose_name = "Еда"
        verbose_name_plural = "Еда"