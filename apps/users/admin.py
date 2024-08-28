from django.contrib import admin
from apps.users import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'full_name', 'language', 'banned')
    list_filter = ('language', 'banned')
    search_fields = ('phone_number', 'full_name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('staff_set')


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'dashboard_username', 'role')
    list_filter = ('role',)
    search_fields = ('dashboard_username', 'user__full_name')

    def role_name(self, obj):
        return dict(models.StaffType.choices)[obj.role]
    role_name.short_description = 'Роль'
    readonly_fields = ('role_name',)

    fieldsets = (
        (None, {'fields': ('user', 'dashboard_username', 'dashboard_password')}),
        ('Роль', {'fields': ('role_name',)}),
    )