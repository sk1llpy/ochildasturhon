from django.contrib import admin
from apps.orders import models

# Register your models here.
@admin.register(models.Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'food')
    list_filter = ('user', 'food')
    search_fields = ('user__full_name', 'food__title')


@admin.register(models.OrderFood)
class OrderFoodAdmin(admin.ModelAdmin):
    list_display = ('order', 'food')
    list_filter = ('order', 'food')
    search_fields = ('order__id', 'food__title')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'location')
    list_filter = ('status', 'location')
    search_fields = ('user__full_name', 'location')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('orderfood_set')

    def order_foods(self, obj):
        return ', '.join([str(of.food) for of in obj.orderfood_set.all()])
    order_foods.short_description = 'Блюда в заказе'
    readonly_fields = ('order_foods',)

    fieldsets = (
        (None, {'fields': ('user', 'status', 'location')}),
        ('Блюда в заказе', {'fields': ('order_foods',)}),
    )