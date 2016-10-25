from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView


from .forms import UserForm, LoginForm, ContactForm
from .models import Contact
# Create your views here.
class home(View):
	def get(self, request):
		return render(request ,'home.html')



def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		return redirect('manager:home')
	context = {
		"form": form,
	}
	return render(request, "contact_form.html", context)

# class contactList(ListView):
# 	template_name='contact_list.html'
	
# 	def get_queryset(self):
# 		return Contact.objects.all()

def contactList(request):
	queryset = Contact.objects.filter(user=request.user)
	return render(request, 'contact_list.html', {"query": queryset})

# def register(request):    
# 	form = UserForm(request.POST or None)
# 	if form.is_valid():
# 		user = form.save(commit=False)
# 		username = form.cleaned_data['username']
# 		password = form.cleaned_data['password']
# 		user.set_password(password)
# 		user.save()
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				query = Contact.objects.filter(user=request.user)
# 				return render(request, 'contact_list.html', {"query":query})
# 	context = {
# 		"form": form,
# 	}
# 	return render(request, 'register.html', form)

class register(View):
	form_class = UserForm
	template_name = 'register.html'

	def get(self, request): 
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			
			if auth_user is not None:

				if auth_user.is_active:
					login(request, auth_user)
					return  redirect('manager:home')

		return render(request, self.template_name, {'form': form})

def Logout(request):
	if request.user.is_authenticated():
		logout(request)
		return redirect('manager:home')
	else:	
		return render(request, 'not_logged_in.html')




class Login(View):
	form = LoginForm
	template_name = 'login.html'

	def get(self, request): 
		form = self.form(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				if auth_user.is_active:
					login(request, auth_user)
					return  render(request, 'home.html')

			else:
				template_name = 'invalid_login.html'
				return render(request, template_name)