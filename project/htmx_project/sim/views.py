from django.shortcuts import render
from django.http import HttpResponse


def sample_post(request, *args, **kwargs):
    print(f'{request.POST = }')
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    favourite_colour = request.POST.get('favourite_color', '')

    if name and email and favourite_colour:
            return HttpResponse('<p class="success">Form submitted successfully! ✅</p>')
    else:    
            return HttpResponse('<p class="error">Please provide both name and email and favourite color.❌</p>')


def example(request):
    return render(request, 'example.html')
