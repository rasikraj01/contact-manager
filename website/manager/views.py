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
	if request.user.is_authenticated():
		form = ContactForm(request.POST or None)

		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			#success
			return redirect('manager:list')
		context = {
			"form": form,
	
		}
		return render(request, "contact_form.html", context)
	return render(request, "not_logged_in.html")

def contactList(request):
	queryset = Contact.objects.filter(user=request.user)
	return render(request, 'contact_list.html', {"query": queryset})

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

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('manager:home')
            else:
                return render(request, 'invalid_login.html')#disabled
        else:
            return render(request, 'invalid_login.html')#invalid login

    return render(request, 'login.html')
