from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_customer/', views.add_customer, name='add_customer'),
    path('edit_customer/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('add_purchase/', views.add_purchase, name='add_purchase'),
    path('customers/', views.customer_list, name='customer_list'),
    path('products/', views.product_list, name='product_list'),
    path('purchases/', views.purchase_list, name='purchase_list'),
]