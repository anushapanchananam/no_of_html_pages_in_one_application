from django.shortcuts import render

# Create your views here.

def box(request):
    return render(request, 'box.html')

def me(request):
    return render(request, 'me.html')

def fourimages(request):
    return render(request, 'fourimages.html')

def imagehandling(request):
    return render(request, 'imagehandling.html')

def random(request):
    return render(request, 'random.html')

def seminar(request):
    return render(request, 'seminar.html')

def student(request):
    return render(request, 'student.html')

def transform(request):
    return render(request, 'transform.html')

def bubbles(request):
    return render(request, 'bubbles.html')

def application(request):
    return render(request, 'application.html')

def birthday(request):
    return render(request, 'birthday.html')