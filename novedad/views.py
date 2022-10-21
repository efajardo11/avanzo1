from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import novedadForm
from .logic.novedad_logic import get_novedad, create_novedad

def novedad_list(request):
    novedad = get_novedad()
    context = {
        'novedad_list': novedad
    }
    return render(request, 'novedad/novedad.html', context)

def novedad_create(request):
    if request.method == 'POST':
        form = novedadForm(request.POST)
        if form.is_valid():
            create_novedad(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created novedad')
            return HttpResponseRedirect(reverse('novedadCreate'))
        else:
            print(form.errors)
    else:
        form = novedadForm()

    context = {
        'form': form,
    }
    return render(request, 'novedad/novedadCreate.html', context)