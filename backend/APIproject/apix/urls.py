from django.urls import path, include
#from api import urls
from .views import home
urlpatterns = [
    path('home/',home,name='home'),
]
