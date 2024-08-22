from django.db import models

from apps.general.models import BaseModel
from apps.general.choices import LanguageType, StaffType


# Create your models here.
class User(BaseModel):
    user_id = models.BigIntegerField(null=True)
    phone_number = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=2, choices=LanguageType, null=True)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.phone_number} | {self.full_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Staff(BaseModel):
    dashboard_username = models.CharField(max_length=255, null=True, blank=True)
    dashboard_password = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=255, choices=StaffType.choices, null=True)

    def __str__(self):
        return f"{({role[0]: role[1] for role in StaffType.choices}[self.role])}: {self.user}"
        
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
