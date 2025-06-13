from django.shortcuts import render, redirect, get_object_or_404
from .models import Comuna
from .forms import ComunaForm

def listar_comunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'MisComunas/list.html', {'comunas': comunas})

def crear_comuna(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_comunas')
    else:
        form = ComunaForm()
    return render(request, 'MisComunas/form.html', {'form': form})

def editar_comuna(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('listar_comunas')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'MisComunas/form.html', {'form': form})

def eliminar_comuna(request, pk):
    comuna = get_object_or_404(Comuna, pk=pk)
    if request.method == 'POST':
        comuna.delete()
        return redirect('listar_comunas')
    return render(request, 'MisComunas/confirm_delete.html', {'comuna': comuna})
