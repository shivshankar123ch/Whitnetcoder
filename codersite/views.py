from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *
from .forms import CreateUserForm




def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)



def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact_info(request):
    if request.method == "POST":
        userdetail = contact()
        userdetail.Name = request.POST.get('Name')
        userdetail.Email_id = request.POST.get('Email_id')
        userdetail.subject = request.POST.get('subject')
        userdetail.message = request.POST.get('message')
        userdetail.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def java(request):
    return render(request,'java.html')

def html(request):
    return render(request,'html.html')

def css(request):
    return render(request,'css.html')

def javas(request):
    return render(request,'javas.html')

def python(request):
    return render(request,'python.html')

def sql(request):
    return render(request,'sql.html')

def php(request):
    return render(request,'php.html')



def fresher(request):
    return render(request,'fresher.html')

def professional(request):
    return render(request,'professional.html')

def softskills(request):
    return render(request,'softskills.html')

def incompany(request):
    return render(request,'incompany.html')

def inplant(request):
    return render(request,'inplant.html')

def internship(request):
    return render(request,'internship.html')

def virtual(request):
    return render(request,'virtual.html')

def elearning(request):
    return render(request,'elearning.html')

def overview(request):
    return render(request,'overview.html')

def hrservices(request):
    return render(request,'hrservices.html')


















