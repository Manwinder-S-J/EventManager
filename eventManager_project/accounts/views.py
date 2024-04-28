from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrantCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrantCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            registrant_group, created = Group.objects.get_or_create(name='registrant')
            registrant_group.user_set.add(new_user)
            messages.success(request, f'Account for {new_user.username} has been successfully created. Please login to view the events to register.')
            return redirect('login')
    else:
        form = RegistrantCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upcoming_events')  
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Please correct the below errors'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  


def admin_check(user):
    return user.is_staff

@login_required
@user_passes_test(admin_check)
def list_users(request):
    registrant_group = Group.objects.get(name='registrant')
    registrants = User.objects.filter(groups=registrant_group).order_by('-date_joined')
    return render(request, 'list_users.html', {'users': registrants})
