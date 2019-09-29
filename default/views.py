from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import AddFood

from default.forms import UserRegisterForm, CookerRegisterForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_register(request):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save(commit=False)
            user.user_type = 'User'
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'{username} Zehmet olmasa emailinizi yoxlayin')
        return redirect('index')
    context['form'] = form
    return render(request, 'user-register.html', context)


def cooker_register(request):
    context = {}
    form = CookerRegisterForm()

    context['form'] = form
    return render(request, 'cooker-register.html', context)


def common(request):
    context = {}
    context["sitename"] = Site_name.objects.all()
    context['menu'] = Menu.objects.all()
    context['main'] = Main.objects.all()
    context['footer'] = Footer.objects.all()

    return context


def Home(request):
    context = common(request)
    context['first'] = First.objects.last()
    context['second'] = Second.objects.last()
    context['meals'] = Meals.objects.all()

    return render(request, "index.html", context)


def add_food(request):
    context = common(request)
    context["form"] = AddFood()
    if request.method == "POST":
        form = AddFood(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("index")
        else:
            print(form.errors)
    return render(request, "yemek.html", context)
