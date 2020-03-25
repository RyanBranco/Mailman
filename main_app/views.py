from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Package
from .forms import SignUpForm


def login(request):
    return render(request, '../templates/registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            username = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class PackageCreate(CreateView):
    model = Package
    fields = ["origination", "destination", "length", "width", "height", "weight", "is_fragile"]
    success_url = '/profile/'

def home(request):
    packages = Package.objects.all()
    return render(request, 'main_app/home.html', { "packages": packages })

class PackageUpdate(UpdateView):
    model = Package
    fields = ["length", "width", "height", "weight", "is_fragile"]
    success_url = "/profile/"

class PackageDelete(DeleteView):
    model = Package
    success_url = "/profile/"

def profile(request):
    packages = Package.objects.all()
    return render(request, 'main_app/profile.html', { "packages": packages })

# @login_required
def package_detail(request, pkg_id):
    packages = Package.objects.get(id=pkg_id)
    return render(request, 'main_app/detail.html')