from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('menu/',views.menu, name='menu'),
    path('contact/',views.contact, name='contact'),

    path('cart/',views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

    path('checkout/',views.checkout, name='checkout'),
    path('ordered/', views.ordered, name='ordered')
]