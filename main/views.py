from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.models import User
from main.models import Org
import os

user_created = False

def home(request):
    return render(request, 'main/home.html', { "title": "Home"})


def organisations(request):

    all = request.GET.get("all")

    if all or not request.user.is_authenticated:
        o = orgs(request, True)
    else:
        o = orgs(request, False)

    return render(request, 'main/orgs.html', {
        "title": "Organisations",
        "orgs": o            
    })
    

def orgs(request, all):

    ## generate orgs
    data = []
    users = User.objects.all()    

    if all:
        for user in users:
            if user.is_superuser:
                continue

            data.append(user)
    else:
        metadata = toArray(request.user.data.metadata)

        for user in users:
            if user == request.user or user.is_superuser:
                continue

            for i in metadata:
                for j in toArray(user.data.metadata):
                    if i == j:                        
                        if user in data:
                            continue

                        data.append(user)

    return data
    

def org(request):

    name = request.GET.get("name")
    o = Org.objects.get(name = name)
    user = o.user
    
    return render(request, 'main/org.html', {
        "title":o.name,
        "user": user
    })


def login(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login_user(request, user)
            return HttpResponseRedirect(reverse("main:home"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "main/login.html", {
                "message": "Invalid Credentials",
                "title": "Login",
                "type": "danger"
            })
    
    global user_created

    if user_created:
        user_created = False
        return render(request, 'main/login.html', {
            "title": "Login",
            "message": "User Created Succesfully!",
            "type": "success"
            })

    else:
        return render(request, 'main/login.html', { "title": "Login" })


def logout(request):
    logout_user(request)
    return HttpResponseRedirect(reverse("main:home"))


def aboutUs(request):
    return render(request, 'main/about.html', { "title": "About Us"})


def user(request):
    return render(request, 'main/account.html', {
        "user": request.user
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
        metadata = request.POST["metadata"]
        logo = request.POST["logo"]
    
        ##check if passwords match
        if password == password2:
            ##check if username is unique
            for u in User.objects.all():
                if u.username == username:
                    return render(request, 'main/signUp.html', {
                'message': 'Username already exists',
                "title": "Sign Up"
                })      
            ##create user       
            user = User.objects.create_user(username, email, password)
            org = Org(user=user, name=name, info=info, website=website, metadata=metadata, logo=logo)
            org.save()
            global user_created
            user_created = True
            return HttpResponseRedirect(reverse("main:login"))            
        else:
            return render(request, 'main/signUp.html', {
                'message': 'Passwords do not match',
                "title": "Sign Up"
            })

    return render(request, 'main/signUp.html', { "title": "Sign Up" })


def toArray(string):

    params = []
    p = ""
    for i in string:
        if i == ",":
            params.append(p)
            p = ""
        else:
            p = p + i

    return params
