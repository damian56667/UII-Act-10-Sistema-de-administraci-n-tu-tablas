from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio_venta', 'stock', 'id_marca', 'foto']
        labels = {
            'nombre': 'Nombre',
            'precio_venta': 'Precio de Venta',
            'stock': 'Stock',
            'id_marca': 'ID Marca',
            'foto': 'Foto del Producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_marca': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
