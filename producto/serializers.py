from decimal import Decimal

from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):

    test = serializers.IntegerField(default=None, read_only=True)
    precio_con_impuesto = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        #fields = ['id', 'nombre', 'precio', 'descripcion', 'test', 'precio_con_impuesto']
        fields = '__all__'

    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value

    def create(self, validated_data):
        validated_data["nombre"] = validated_data["nombre"].upper() #Convertirlo en mayuscula
        return Producto.objects.create(**validated_data)

    def get_precio_con_impuesto(self, obj):
        return obj.precio * Decimal(1.19) #Calcula el precio con un 19%
