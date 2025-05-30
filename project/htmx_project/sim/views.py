from django.shortcuts import redirect, render
from django.http import HttpResponse
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
    queryset = Products.objects.all()
    context = {'products': queryset}
    # return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')
    # return render('example.html', context)
    return example(request)

def delete_demographics(request, id):
    if request.method == 'GET':
        queryset = Products.objects.get(id=id)
        queryset.delete()
        return redirect('/')    

def example(request):
    queryset = Products.objects.all()
    context = {'products': queryset}
    return render(request, 'example.html', context)


