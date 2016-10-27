from django.conf.urls import include, url
from .views import register,home, contact, contactList, Login, Logout, detail,update, delete

app_name = 'manager'

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),

    #CRUD
    url(r'^contact/$', contact, name='contact'),
    url(r'^(?P<contact_id>[0-9]+)/$', detail, name='detail'),
    url(r'^(?P<contact_id>[0-9]+)/update/$', update, name='update'),
    url(r'^(?P<contact_id>[0-9]+)/delete/$', delete, name='delete'),
    url(r'^list/$', contactList, name='list'),    

    #REGISTRATION
    url(r'^register/$', register.as_view() , name='register'),
    url(r'^login/$', Login , name='login'),
    url(r'^logout/$', Logout , name='logout'),
    
    ]