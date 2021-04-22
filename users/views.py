from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User
from .forms import UserCreateForm, UserUpdateForm

# Create your views here.
class UserList(ListView):
    template_name = "users/list.html"
    model = User
    queryset = User.objects.filter(is_active=True)
    context_object_name = "users"


class UserDetail(DetailView):
    template_name = "users/detail.html"
    model = User
    context_object_name = "user_"


class UserCreate(CreateView):
    template_name = "users/register.html"
    model = User
    form_class = UserCreateForm


class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = "users/update.html"
    form_class = UserUpdateForm

    def test_func(self):
        return self.request.user.is_superuser or (self.request.user == self.get_object())


class UserDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "users/delete.html"

    def test_func(self):
        return self.request.user.is_superuser or (self.request.user == self.get_object())

    def delete(self, request, *args, **kwargs):
        user_ = self.get_object()
        user_.is_active = False
        user_.save()
        return redirect("users:list")