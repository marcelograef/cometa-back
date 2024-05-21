from rest_framework import serializers
from .models import Beer, Stock, Item, RoundItem, Round, Order

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model: Beer
        fields = ['name', 'price', 'quantity']

class StockSerializer(serializers.ModelSerializer):
    beers = BeerSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['last_updated', 'beers']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'price_per_unit', 'total']

class RoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundItem
        fields = ['name', 'quantity', 'subtotal']

class RoundSerializer(serializers.ModelSerializer):
    items = RoundItemSerializer(many=True)

    class Meta:
        model = Round
        fields = ['created', 'items']

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    rounds = RoundSerializer(many=True)

    class Meta:
        model = Order
        fields = ['created', 'paid', 'subtotal', 'taxes', 'discounts', 'items', 'rounds']
