from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('', views.cart_view, name='cart'),
    path('', views.event_view, name='events'),
    path('add-to-cart/<int:event_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:event_id>/', views.remove_from_cart, name='remove_from_cart')
]
