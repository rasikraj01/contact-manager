from django.shortcuts import get_object_or_404 ,render , redirect

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView, DetailView

from .forms import UserForm, LoginForm, ContactForm
from .models import Contact


# Create your views here.
class home(View):
	def get(self, request):
		return render(request ,'home.html')

#CRUD

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
	if request.user.is_authenticated():
		queryset = Contact.objects.filter(user=request.user)
		return render(request, 'contact_list.html', {"query": queryset})
	else:
		return render(request, 'not_logged_in.html')

def detail(request, contact_id):
	if request.user.is_authenticated():
		queryset = Contact.objects.filter(pk = contact_id)
		return render(request, 'contact_detail.html', {"query":queryset})
	else:
		return render(request, 'not_logged_in.html')

def update(request, contact_id):
	if request.user.is_authenticated():
		instance = get_object_or_404(Contact, id=contact_id)
		form = ContactForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect("manager:list")

		context = {
			"name": instance.name,
			"number": instance.number,
			"form": form
		}
		return render(request, "contact_form.html", context)
	else:
		return render(request, 'not_logged_in.html')


def delete(request, contact_id):
	if request.user.is_authenticated():
		instance = get_object_or_404(Contact, id=contact_id)
		instance.delete()
		return redirect("manager:list")
	else:
		return render(request, 'not_logged_in.html')

	
#AUTH

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
