from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def validate_positions(self, positions):
        if not positions:
            raise ValidationError("You're trying to add an empty stock")

        products = [position.get('product') for position in positions]
        if len(products) != len(set(products)):
            raise ValidationError("You're trying to add same products multiple times")

        return positions

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            product = position.get('product')
            StockProduct.objects.update_or_create(
                stock=stock, product=product,
                defaults={'stock': stock,
                          'product': product,
                          **position}
            )

        return stock
