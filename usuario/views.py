from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UsuarioForm
from .logic.usuario_logic import get_usuario, create_usuario

def usuario_list(request):
    usuario = get_usuario()
    context = {
        'usuario_list': usuario
    }
    return render(request, 'Usuario/usuario.html', context)

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            create_usuario(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created usuario')
            return HttpResponseRedirect(reverse('usuarioCreate'))
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    context = {
        'form': form,
    }
    return render(request, 'Usuario/UsuarioCreate.html', context)