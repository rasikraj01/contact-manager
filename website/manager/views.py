from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View


from .forms import UserForm, LoginForm, ContactForm

# Create your views here.
class home(View):
	def get(self, request):
		return render(request ,'home.html')