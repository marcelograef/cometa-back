from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Stock(models.Model):
    last_updated = models.DateTimeField()
    beers = models.ManyToManyField(Beer)

    def __str__(self):
        return f"Stock updated on {self.last_updated}"

class Item(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class RoundItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    subtotal = models.FloatField(default=0.0)  # Added default value


    def __str__(self):
        return self.name

class Round(models.Model):
    created = models.DateTimeField()
    items = models.ManyToManyField(RoundItem)

    def __str__(self):
        return f"Round created on {self.created}"

class Order(models.Model):
    created = models.DateTimeField()
    paid = models.BooleanField(default=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    discounts = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(Item)
    rounds = models.ManyToManyField(Round)

    def __str__(self):
        return f"Order created on {self.created}, Paid: {self.paid}"
