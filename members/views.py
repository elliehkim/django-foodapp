from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Accounts was created for ' + user)
                return redirect('login')
        return render(request,'members/register.html',{'form':form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password= password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')
            
        context = {}
        return render(request, 'members/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')