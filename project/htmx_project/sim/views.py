from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Products


def createUser(request, *args, **kwargs):
    print(f'{request.POST = }')
    app_name = request.POST.get('app_name', '')
    app_email = request.POST.get('app_email', '')
    # favourite_colour = request.POST.get('favourite_color', '')

    # if name and email:
    #         return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')
    # else:    
    #         return HttpResponse('<p class="error">Please provide both name and email and favourite color.❌</p>')

    Products.objects.create(
            app_name = app_name,
            app_email = app_email,
        )
    products=Products.objects.all()
    # queryset = Products.objects.all()
    context = {'products': products}
    # example(request)
    # return request
    # return HttpResponseRedirect("http://localhost:8000/")
    # return HttpResponse(content='<input type="text" name="app_name" placeholder="Name" required /><input type="email" name="app_email" placeholder="Email" required /><input refresh="true" hx-trigger="load" type="submit" value="Submit"/>')
    return render(request, "example.html", context)
    # return redirect('example')
    # return HttpResponseRedirect('../')

def deleteDemographics(request, id):
    # if request.htmx:
        queryset = Products.objects.get(id=id)
        queryset.delete()
        products=Products.objects.all()
        context = {'products': products}
        # return HttpResponseRedirect("http://localhost:8000/")
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
        # demographics_name = data.get('demographics_name')
        # demographics_surname = data.get('demographics_surname')
        # # demographics_image = request.FILES.get('demographics_image')
        # demographics_address = data.get('demographics_address')
        # demographics_age = data.get('demographics_age')

        queryset.app_name = app_name
        queryset.app_email = app_email
        # queryset.demographics_image = demographics_image
        # queryset.demographics_address = demographics_address
        # queryset.demographics_age = demographics_age
        

        # if demographics_image:
        #     queryset.demographics_image = demographics_image

        # queryset.save()
        # return redirect('/')

    context = {'products': queryset}
    return render(request, 'update_demographics.html', context)

def updateUser(request):
    

    if request.method == 'POST':
        data = request.POST
        queryset = Products.objects.get(id=data.get('app_id'))
        app_name=data.get('app_name')
        app_email=data.get('app_email')
        # demographics_name = data.get('demographics_name')
        # demographics_surname = data.get('demographics_surname')
        # # demographics_image = request.FILES.get('demographics_image')
        # demographics_address = data.get('demographics_address')
        # demographics_age = data.get('demographics_age')

        queryset.app_name = app_name
        queryset.app_email = app_email
        # queryset.demographics_image = demographics_image
        # queryset.demographics_address = demographics_address
        # queryset.demographics_age = demographics_age
        

        # if demographics_image:
        #     queryset.demographics_image = demographics_image

        queryset.save()
        # return redirect('/')

    products=Products.objects.all()
    # queryset = Products.objects.all()
    context = {'products': products}
    
    # return HttpResponseRedirect("http://localhost:8000/")
    return render(request, 'example.html', context)


