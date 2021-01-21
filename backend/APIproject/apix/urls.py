from django.urls import path, include
#from api import urls
from .views import home, listView
urlpatterns = [
    path('home/',home,name='home'),
    path('list/',listView.as_view(), name='list'),
]
