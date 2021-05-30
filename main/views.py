from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Org

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def organisations(request):

    if not request.user.username:
        return render(request, 'main/orgs.html', {
            ##"orgs": Org 
        })
    else:
        return render(request, 'main/orgs.html', {
            "metadata": request.user.data.metadata
            ##"orgs": Org
        })
    
def orgs(request):
    
    ## get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or start + 9)

    ## generate orgs
    data = []
    dataUsers = []
    users = User.objects.all()

    if not request.user.username:

        for user in users:

            if user == request.user or user.is_superuser:
                continue

            o = {'name': user.data.name, 'info': user.data.info}
            data.append(o)

        return JsonResponse({
            "orgs": data
        })
    else:

        metadata = toArray(request.user.data.metadata)         

        for user in users:

            if user == request.user or user.is_superuser:
                continue

            for i in metadata:

                for j in toArray(user.data.metadata):

                    if i == j:                        
                        if user in dataUsers:
                            continue
                        
                        o = {'name': user.data.name, 'info': user.data.info}
                        data.append(o) 
                        dataUsers.append(user)         

        return JsonResponse({
            "orgs": data
        })
    

def org(request):

    name = request.GET.get("name")
    o = Org.objects.get(name = name)
    
    return render(request, 'main/org.html', {
        "email": o.user.email,
        "name": o.name,
        "info": o.info,
        "website": o.website,
        "metadata": o.metadata
    })


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
        "website": request.user.data.website,
        "metadata": request.user.data.metadata
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
    
        if password == password2:
            user = User.objects.create_user(username, email, password)
            org = Org(user=user, name=name, info=info, website=website, metadata=metadata)
            org.save()
            return HttpResponseRedirect(reverse("main:login"))
        else:
            return render(request, 'main/signUp.html', {
                'message': 'Passwords do not match'
            })

    return render(request, 'main/signUp.html')

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
