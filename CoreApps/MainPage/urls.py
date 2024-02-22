from django.urls import path, include
#from CoreApps.MainPage.views import index
from CoreApps.MainPage import views
from CoreApps.MainPage.views import main
from CoreApps.MainPage import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("", main.as_view(), name='mainpage'),
    #path("about", about.as_view(), name='about'),    
]