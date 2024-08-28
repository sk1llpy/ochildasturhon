from django.db import models

from apps.general.models import BaseModel
from apps.general.choices import OrderStatusType, LocationType

from apps.foods.models import Food
from apps.users.models import User


# Create your models here.
class Basket(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Блюдо')

    def __str__(self):
        return f"{self.user.full_name} - {self.food.title}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class OrderFood(BaseModel):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, verbose_name='Заказ')
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Блюдо')

    def __str__(self):
        return f"{self.order.id} - {self.food.title}"

    class Meta:
        verbose_name = 'Блюдо в заказе'
        verbose_name_plural = 'Блюда в заказе'


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(
        max_length=255, choices=OrderStatusType.choices, default=OrderStatusType.pending, verbose_name='Статус')
    location = models.CharField(
        max_length=255, choices=LocationType.choices, null=True, verbose_name='Локация')

    def __str__(self):
        return f"{self.user} -> {self.location}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            super().save(*args, **kwargs)
            self.create_order_foods()
            self.clear_basket()
        else:
            super().save(*args, **kwargs)

    def create_order_foods(self):
        basket_items = Basket.objects.filter(user=self.user)
        for item in basket_items:
            OrderFood.objects.create(order=self, food=item.food)

    def clear_basket(self):
        Basket.objects.filter(user=self.user).delete()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'