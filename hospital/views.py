from django.shortcuts import render, redirect
from .models import *
from .forms import CustomerForm, AppointmentForm


def index(request):
    post = MainDoctor.objects.all()
    post1 = TreatDoctor.objects.all()
    context = {
        'post': post,
        'post1': post1
    }
    return render(request,
                  template_name='index.html',
                  context = context)


def add_customer(request):
    comments = Customer.objects.all()
    if request.method == 'POST':
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-create')
            return redirect('')
    else:
        form = CustomerForm()
    context = {'form' : form,
               'comments' : comments }
    return render(request,
                  template_name='index.html',
                  context=context)


def add_app(request):
    if request.method == 'POST':
        form = AppointmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            print('ok')
            return redirect('app-create')
        else:
            print('not ok')
    else:
        form = AppointmentForm()
    context = {'form': form}
    return render(request,
                  template_name='index.html',
                  context=context)


