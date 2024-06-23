from django.urls import path
from . import views

urlpatterns = [
    path("categories", views.get_all_category),
    path("categories/<int:user_id>", views.get_category_by_user),
    path("categories/create", views.create_user_category),
    path("categories/update/<int:category_id>", views.edit_category),
    path("finances/<int:user_id>", views.get_finances_by_user),
    path("finances/create", views.create_finance),
    path("finances/update/<int:finance_id>", views.edit_finance),
    path("goals/<int:user_id>", views.get_goals_by_user, name="goals"),
    path("goals/create", views.create_goal),
    path("goals/edit/<int:goal_id>", views.edit_goal),
]
