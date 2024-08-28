from django.db import models


class StaffType(models.TextChoices):
    cook = "cook", "Шеф-повар"
    manager = "manager", "Менеджер"
    ceo = "ceo", "Генеральный директор (CEO)"


class LanguageType(models.TextChoices):
    uz = "uz", "Узбекский"
    ru = "ru", "Русский"


class LocationType(models.TextChoices):
    tinchlik = "tinchlik", "Tinchlik"
    yunusabad = "yunusabad", "Yunusabad"
    chilonzor_qutbinso = "chilonzor_qutbinso", "Chilonzor Qutbinso"
    chilonzor_18 = "chilonzor_18", "Chilonzor 18"
    maksim_gorkiy = "maksim_gorkiy", "Maksim Gorkiy"
    sergeli = "sergeli", "Sergeli"


class OrderStatusType(models.TextChoices):
    pending = "pending", "pending"
    confirmed = "confirmed", "confirmed"
    rejected = "rejected", "rejected"
    delivered = "delivered", "delivered"