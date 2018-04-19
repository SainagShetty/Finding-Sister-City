# howdy/urls.py
from django.conf.urls import url
from SisterCityApp import views



urlpatterns = [
    url(r'^$', views.homePage),
	url(r'^getSisterCities/$', views.searchCity),
    url(r'^getSpecificCity/$', views.searchSpecific),

]