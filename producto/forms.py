from django import forms
from .models import Producto


"""
class ProductoForm(forms.Form):
    nombre = forms.CharField(label='Nombre A', max_length=100)
    precio = forms.DecimalField(label='Precio', max_digits=10, decimal_places=2)
"""

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ["nombre", "descripcion", "precio"]
        fields = "__all__"