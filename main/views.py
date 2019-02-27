from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mlblogger, MlbloggerCategory, MlbloggerSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def single_slug(request, single_slug):
    categories = [c.category_slug for c in MlbloggerCategory.objects.all()]
    if single_slug in categories:
        matching_series = MlbloggerSeries.objects.filter(mlblogger_category__category_slug=single_slug)  
      
        series_urls = {}
        for m in matching_series.all():
                part_one = Mlblogger.objects.filter(mlblogger_series__mlblogger_series=m.mlblogger_series).earliest("mlblogger_published")
                series_urls[m] = part_one.mlblogger_slug
        
        return render(request=request,
                      template_name='main/category.html',
                      context={"mlblogger_series": matching_series, "part_ones": series_urls})        



    mlbloggers = [m.mlblogger_slug for m in Mlblogger.objects.all()]
    if single_slug in mlbloggers:
      return HttpResponse(f"{single_slug} is a MLblog")  

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")  


def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={"categories": MlbloggerCategory.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")    

    form = NewUserForm
    return render(request,
                  "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")    
        else:
            messages.error(request, "Invalid username or password")           
    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})    




