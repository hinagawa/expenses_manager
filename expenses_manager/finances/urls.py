from django.urls import path
from . import views

urlpatterns = [
    path("finances/category", views.get_all_category),
    path("finances/category/<int:user_id>", views.get_category_by_user),
    path("finances/category_custom", views.get_custom_category),
    path("finances/category/create", views.create_user_category),
    path("finances/category/edit", views.edit_category),
    path("finances", views.get_finances_by_user),
    path("finances/create", views.create_finance),
    path("finances/edit", views.edit_finance),
    path("finances/goals/<int:user_id>", views.get_goals_by_user, name="goals"),
    path("finances/goals/create", views.create_goal),
    path("finances/goals/edit", views.edit_goal),
]
