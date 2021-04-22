from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        exclude = ["last_login", "is_superuser", "is_active", "is_staff", "groups", "user_permissions", "date_joined", "password"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone_number", "street_address", "city", "state", "zipcode"]