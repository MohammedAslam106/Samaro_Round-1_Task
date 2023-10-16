from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/products', views.products, name='api/products'),
    path('api/transactions',views.transactions,name='api/transactions'),
    path('payment',views.create_payment_method,name='payment'),
    path('success/',views.payment_successfull,name='success'),
    path('cancel/',views.payment_cancel,name='cancel')

]
