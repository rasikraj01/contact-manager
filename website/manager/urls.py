from django.conf.urls import include, url
from .views import home

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    ]