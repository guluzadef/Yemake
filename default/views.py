from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import AddFood
from django.views import generic
from django.contrib.auth import login, authenticate
from default.models import TokenModel

from default.forms import UserRegisterForm, CookerRegisterForm, LoginForm


def user_login(request):
    context={}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user  = authenticate(username=username,password=password)
            login(request,user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    context['form'] = LoginForm()
    return render(request,'login.html',context)
def user_register(request):
    context={}
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save(commit=False)
            user.user_type = 'U'
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'{username} Zehmet olmasa emailinizi yoxlayin')
            return redirect('index')
        else:
            print(form.errors.as_data())
            messages.warning(request, form.errors)
            return redirect('index')
    context['form'] = form
    return render(request,'user-register.html',context)

def cooker_register(request):
    context={}
    form = CookerRegisterForm()
    if request.method == 'POST':
        form = CookerRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save(commit=False)
            user.user_type = 'C'
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'{username} Zehmet olmasa emailinizi yoxlayin')
            return redirect('index')
        else:
            messages.warning(request,form.errors)
            return redirect('index')
    context['form'] = form
    return render(request,'cooker-register.html',context)

def verify_view(request,token,id):
    verify=TokenModel.objects.filter(
        token=token,
        expired=False,
        user_id= id
    ).last()
    if verify:
        verify.user.is_active = True
        verify.user.save()
        verify.expired = True
        verify.save()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return redirect('index')
    else:
        print('---------------------------------------------')
        return redirect('index')


def common():
    context = {}
    context["sitename"] = Site_name.objects.all()
    context['menu'] = Menu.objects.all()
    context['main'] = Main.objects.all()
    context['footer'] = Footer.objects.all()
    context['photos'] = Photos_Pages.objects.last()
    context['text'] = Texts_Pages.objects.last()


    return context


def Home(request):
    context = common()
    context['first'] = First.objects.last()
    context['second'] = Second.objects.last()
    context['meals'] = Meals.objects.all()

    return render(request, "index.html", context)


def add_food(request):
    context = common()
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




class DetailFood(generic.DetailView):
    model = Meals
    template_name = "DetailFood.html"
    extra_context = common()