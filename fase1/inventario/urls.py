from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='lista_productos'),
    path('nuevo/', views.crear_producto, name='crear_producto'),
    path('api/productos/', views.product_api_list, name='producto_api_list'),
    path('api/productos/<int:pk>/', views.producto_api_detail, name='producto_api_detail'),
]
