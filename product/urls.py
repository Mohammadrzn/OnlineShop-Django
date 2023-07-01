from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('<int:pk>/', views.detail, name="detail"),
    path('categories/', views.main_category, name="category"),
    path('categories/products/<int:pk>/', views.category_product, name="product_category"),
    path('order/', views.order_page, name="order_page"),
    path('', views.CartView.as_view(), name='cart'),
    path('cart/<int:product_id>/', views.CartView.as_view(), name='cart-product'),
    path('cart/', views.cart_view, name='cart_page'),
    path('clear/', views.ClearCartView.as_view(), name='clear'),
]