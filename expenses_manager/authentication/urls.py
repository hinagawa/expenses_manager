from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("signIn", views.signIn),
    path("logout", views.logout),
    path("signUp", views.create_user),
]
