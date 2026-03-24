from django.shortcuts import render
from .models import Producto

# Create your views here.
def  productos(request):
  items = Producto.objects.all()
  return render(request, 'inventario/list.html', {'items': items})