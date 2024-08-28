from django.contrib import admin
from apps.foods import models

# Register your models here.
@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price',)
    list_filter = ('price',)
    search_fields = ('title',)