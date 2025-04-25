from django.urls import path
from ecom import views

app_name = 'ecom'

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail.html/', views.product_detail, name='product-detail'),
]
