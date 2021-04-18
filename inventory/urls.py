from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('', views.InventoryList.as_view(), name="list"),
    path('<int:pk>/', views.InventoryDetail.as_view(), name="detail"),

]