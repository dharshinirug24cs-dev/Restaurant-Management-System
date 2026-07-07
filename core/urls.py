from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reservation/", views.reservation, name="reservation"),
    path("order/", views.order, name="order"),
    path("inventory/", views.inventory, name="inventory"),
]