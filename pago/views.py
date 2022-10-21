from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import pagoForm
from .logic.pago_logic import get_pago, create_pago

def pago_list(request):
    pago = get_pago()
    context = {
        'pago_list': pago
    }
    return render(request, 'pago/pago.html', context)

def pago_create(request):
    if request.method == 'POST':
        form = pagoForm(request.POST)
        if form.is_valid():
            create_pago(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created pago')
            return HttpResponseRedirect(reverse('pagoCreate'))
        else:
            print(form.errors)
    else:
        form = pagoForm()

    context = {
        'form': form,
    }
    return render(request, 'pago/pagoCreate.html', context)