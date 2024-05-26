from django.urls import path
from . import views

urlpatterns = [
    path("user/<int:user_id>", views.get_user_by_id, name="users_by_id"),
    path("users/", views.get_all_users, name="all_users"),
    path("create", views.create_user),
    path("edit", views.edit_user),
    path("currency", views.get_currency),
    path("currency/edit", views.edit_currency),
    path("currency/create", views.create_currency),
]
