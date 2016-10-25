from django.conf.urls import include, url
from .views import home, contact, contactList

app_name = 'manager'

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    url(r'^contact/$', contact, name='contact'),

    url(r'^list/$', contactList, name='list'),
    # url(r'^list/$', contactList.as_view(), name='list'),
    
    ]