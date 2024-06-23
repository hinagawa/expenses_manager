from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:user_id>", views.get_user_by_id, name="users_by_id"),
    path("users/", views.get_all_users, name="all_users"),
    path("users/create", views.create_user),
    path("users/update", views.edit_user),
    path("currencies", views.get_currency),
    path("currencies/update", views.edit_currency),
    path("currencies/create", views.create_currency),
]
