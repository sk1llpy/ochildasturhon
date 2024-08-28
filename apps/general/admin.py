from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

# Register your mdoels here.
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ("Личная информация", {"fields": ("username", "first_name", "last_name", "email")}),
        (
            "Разрешения",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )
