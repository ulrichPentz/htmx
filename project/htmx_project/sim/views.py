from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Products


def createUser(request, *args, **kwargs):
    print(f'{request.POST = }')
    app_name = request.POST.get('app_name', '')
    app_email = request.POST.get('app_email', '')
    
    Products.objects.create(
            app_name = app_name,
            app_email = app_email,
        )
    products=Products.objects.all()
    context = {'products': products}
    return render(request, "example.html", context)
    
def deleteDemographics(request, id):
        queryset = Products.objects.get(id=id)
        queryset.delete()
        products=Products.objects.all()
        context = {'products': products}
        return render(request, "example.html", context)

def example(request):
    queryset = Products.objects.all()
    context = {'products': queryset}
    return render(request, 'example.html', context)

def update_demographics(request, id):
    queryset = Products.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST

        app_name=data.get('app_name')
        app_email=data.get('app_email')
        queryset.app_name = app_name
        queryset.app_email = app_email
        
    context = {'products': queryset}
    return render(request, 'update_demographics.html', context)

def updateUser(request):
    

    if request.method == 'POST':
        data = request.POST
        queryset = Products.objects.get(id=data.get('app_id'))
        app_name=data.get('app_name')
        app_email=data.get('app_email')
        
        queryset.app_name = app_name
        queryset.app_email = app_email

        queryset.save()
        
    products=Products.objects.all()
    context = {'products': products}
    
    return render(request, 'example.html', context)


