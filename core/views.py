from django.shortcuts import render, redirect
from .models import MenuItem, Reservation, RestaurantTable, Order, Inventory


def home(request):
    menu_items = MenuItem.objects.filter(available=True)
    return render(request, "core/home.html", {
        "menu_items": menu_items
    })

def order(request):
    if request.method == "POST":
        Order.objects.create(
            customer_name=request.POST["name"],
            phone=request.POST["phone"],
            menu_item_id=request.POST["menu"],
            quantity=request.POST["quantity"]
        )
        return redirect("home")

    menu_items = MenuItem.objects.filter(available=True)

    return render(request, "core/order.html", {
        "menu_items": menu_items
    })

def inventory(request):
    inventory_items = Inventory.objects.all()

    return render(request, "core/inventory.html", {
        "inventory_items": inventory_items
    })


def reservation(request):
    if request.method == "POST":
        Reservation.objects.create(
            customer_name=request.POST["name"],
            phone=request.POST["phone"],
            reservation_date=request.POST["date"],
            reservation_time=request.POST["time"],
            table_id=request.POST["table"]
        )
        return redirect("home")

    tables = RestaurantTable.objects.filter(available=True)

    return render(request, "core/reservation.html", {
        "tables": tables
    })