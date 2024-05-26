from django.urls import path
from . import views

urlpatterns = [
    path("category", views.get_all_category),
    path("category/<int:user_id>", views.get_category_by_user),
    path("category_custom", views.get_custom_category),
    path("category/create", views.create_user_category),
    path("category/edit/<int:category_id>", views.edit_category),
    path("finance/<int:user_id>", views.get_finances_by_user),
    path("finance/create", views.create_finance),
    path("finance/edit/<int:finance_id>", views.edit_finance),
    path("goals/<int:user_id>", views.get_goals_by_user, name="goals"),
    path("goals/create", views.create_goal),
    path("goals/edit/<int:goal_id>", views.edit_goal),
]
