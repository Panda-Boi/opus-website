from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def organisations(request):
    return HttpResponse('In progress')

def signUp(request):
    return HttpResponse('In progress')

def aboutUs(request):
    return HttpResponse('In progress')
