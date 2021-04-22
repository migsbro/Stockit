from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('', views.ItemList.as_view(), name="item_list"),
    path('new/', views.ItemCreate.as_view(), name="item_create"),
    path('<int:pk>/', views.ItemDetail.as_view(), name="item_detail"),
    path('<int:pk>/update/', views.ItemUpdate.as_view(), name="item_update"),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name="item_delete"),
]