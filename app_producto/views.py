from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all()
    return render(request, 'app_producto/index.html', {'productos': productos})

def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'app_producto/add.html', {'form': ProductoForm(), 'success': True})
    else:
        form = ProductoForm()
    return render(request, 'app_producto/add.html', {'form': form})

def edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return render(request, 'app_producto/edit.html', {'form': form, 'success': True})
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app_producto/edit.html', {'form': form})

def delete(request, pk):
    # En tu index usas modal que hace POST a esta url; aquí borramos y redirigimos.
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        # Si quieres borrar también el archivo físico:
        if producto.foto:
            try:
                producto.foto.delete(save=False)
            except:
                pass
        producto.delete()
    return redirect('index')
