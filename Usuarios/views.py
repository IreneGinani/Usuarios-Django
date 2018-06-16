# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Usuario
from .forms import UsuarioForm

from django.shortcuts import render, get_object_or_404

# Create your views here.

def user_list(request):

    usuario = Usuario.objects.all()
    print(usuario)
    return render(request, 'Usuarios/user_list.html', {'usuario': usuario})

def user_new(request):
    form = UsuarioForm()
    return render(request, 'Usuarios/user_edit.html', {'form': form})

def user_new(request):
    if (request.method == "POST"):
        form = UsuarioForm(request.POST)
    	if form.is_valid():
            usuario = form.save(commit=False)
            usuario.nome = form.cleaned_data['nome']
            usuario.idade = form.cleaned_data['idade']
            usuario.sexo = form.cleaned_data['nome']
            usuario.save()
    else:
        form = UsuarioForm()
    return render(request, 'Usuarios/user_edit.html', {'form': form})

def user_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.nome = form.cleaned_data['nome']
            usuario.idade = form.cleaned_data['idade']
            usuario.sexo = form.cleaned_data['nome']
            usuario.save()
            return redirect('user_detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'Usuarios/user_edit.html', {'form': form})

def user_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'Usuarios/user_detail.html', {'usuario': usuario})

