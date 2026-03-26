from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ProductoSerializer

# Create your views here.
def  productos(request):
  items = Producto.objects.all()
  return render(request, 'inventario/list.html', {'items': items})

@api_view(['GET', 'POST'])
def product_api_list(request):
  if request.method == 'GET':
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def producto_api_detail(request, pk):
  try:
    producto = Producto.objects.get(pk=pk)
  except Producto.DoesNotExist:
    return Response(status=404)

  serializer = ProductoSerializer(producto)
  return Response(serializer.data)

def crear_producto(request):
  if request.method == 'POST':
    form = ProductoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('lista_productos')
  else:
    form = ProductoForm()
  return render(request, 'inventario/producto_form.html', {'form': form})