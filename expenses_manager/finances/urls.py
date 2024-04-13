from django.urls import path
from . import views

urlpatterns = [
    path('category', views.get_all_category),
    path('category/<int:user_id>', views.get_category_by_user),
    path('category_custom', views.get_custom_category),
    path('category/create', views.create_user_category),
    path('currency', views.get_currency),
    path('finances', views.get_finances_by_user),
    path('finances/create', views.create_finance),
    path('goals/<int:user_id>', views.get_goals_by_user, name='goals'),
    path('goals/create', views.create_goal),
    path('users/<int:user_id>', views.get_user_by_id, name='all_users'),
    path('users/', views.get_all_users, name='user_by_id'),
    path('users/create', views.create_user)
]
