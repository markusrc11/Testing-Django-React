from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'SKU', 'cantidad']
        # Añadimos clases de Tailwind directamente a los widgets
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none'}),
            'SKU': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'placeholder': 'ING-0000'}),
            'cantidad': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none'}),
        }