from django.conf.urls import include, url
from .views import register,home, contact, contactList, login, logout

app_name = 'manager'

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),

    #CRUD

    url(r'^contact/$', contact, name='contact'),
    #url(r'^/detail/$', contact, name='detail'),
    #url(r'^/update/$',, name='update'),
    #url(r'^delete/$', , name='delete'),
    url(r'^list/$', contactList, name='list'),
    # url(r'^list/$', contactList.as_view(), name='list'),
    

    #REGISTRATION
    url(r'^register/$', register.as_view() , name='register'),
    url(r'^login/$', login.as_view() , name='login'),
    url(r'^logout/$', logout , name='logout'),
    
    ]