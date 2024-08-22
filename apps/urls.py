from django.urls import path
from apps.users.views import login_view

urlpatterns = [
    path('admin/login/<str:username>/<str:password>/', login_view, name='admin')
]