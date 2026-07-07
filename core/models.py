from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class RestaurantTable(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"


class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer_name} - Table {self.table.table_number}"


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.menu_item.name}"
    
class Inventory(models.Model):
    ingredient_name = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    minimum_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.ingredient_name