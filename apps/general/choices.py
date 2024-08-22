from django.db import models

class StaffType(models.TextChoices):
    courier = "courier", "Курьер"
    cook = "cook", "Шеф-повар"
    call_center = "call_center", "Колл-центр"
    manager = "manager", "Менеджер"
    admin = "admin", "Администратор"
    ceo = "ceo", "Генеральный директор (CEO)"


class LanguageType(models.TextChoices):
    uz = "uz", "Узбекский"
    ru = "ru", "Русский"
