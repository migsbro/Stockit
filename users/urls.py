from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UserList.as_view(), name="list"),
    path("<int:pk>/", views.UserDetail.as_view(), name="detail"),
    path("<int:pk>/update/", views.UserUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", views.UserDelete.as_view(), name="delete"),
    path("register/", views.UserCreate.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]