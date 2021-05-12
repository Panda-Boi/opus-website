from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Org

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def organisations(request):
    return HttpResponse('In progress')

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("main:index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "main/login.html", {
                "message": "Invalid Credentials"
            })
    
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:index"))

def aboutUs(request):
    return HttpResponse('In progress')

def user(request):
    return render(request, 'main/account.html', {
        "email": request.user.email,
        "name": request.user.data.name,
        "info": request.user.data.info,
        "website": request.user.data.website
    })

def signUp(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        email = request.POST["email"]
        info = request.POST["info"]
        name = request.POST["name"]
        website = request.POST["website"]

        if password == password2:
            user = User.objects.create_user(username, email, password)
            org = Org(user=user, name=name, info=info, website=website)
            org.save()
            return HttpResponseRedirect(reverse("main:login"))
        else:
            return render(request, 'main/signUp.html', {
                'message': 'Passwords do not match'
            })

    return render(request, 'main/signUp.html')
