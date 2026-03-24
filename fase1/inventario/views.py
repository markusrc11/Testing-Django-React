from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def  productos(request):
  items = Producto.objects.all()
  return render(request, 'inventario/list.html', {'items': items})

def crear_producto(request):
  if request.method == 'POST':
    form = ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('lista_productos')
  else:
    form = ProductoForm()
  return render(request, 'inventario/producto_form.html', {'form': form})