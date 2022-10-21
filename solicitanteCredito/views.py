from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import solicitanteForm
from .logic.solicitante_logic import get_solicitante, create_solicitante

def solicitante_list(request):
    solicitante = get_solicitante()
    context = {
        'solicitante_list': solicitante
    }
    return render(request, 'solicitante/solicitante.html', context)

def solicitante_create(request):
    if request.method == 'POST':
        form = solicitanteForm(request.POST)
        if form.is_valid():
            create_solicitante(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created solicitante')
            return HttpResponseRedirect(reverse('solicitanteCreate'))
        else:
            print(form.errors)
    else:
        form = solicitanteForm()

    context = {
        'form': form,
    }
    return render(request, 'solicitante/solicitanteCreate.html', context)