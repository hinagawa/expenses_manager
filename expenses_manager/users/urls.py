from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:user_id>", views.get_user_by_id, name="all_users"),
    path("users/", views.get_all_users, name="user_by_id"),
    path("users/create", views.create_user),
    path("users/edit", views.edit_user),
    path("users/currency", views.get_currency),
    path("users/currency/edit", views.edit_currency),
]
