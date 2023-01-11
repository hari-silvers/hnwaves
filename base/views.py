from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
#from .forms import ProfileForm,CustomUserForm

# Create your views here.
def homepage(request):
    
    return render(request, 'base/base.html')