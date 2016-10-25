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

	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
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
	queryset = Contact.objects.all()
	return render(request, 'contact_list.html', {"query": queryset})