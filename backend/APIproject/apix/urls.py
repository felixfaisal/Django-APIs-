from django.urls import path, include
#from api import urls
from .views import home, listView, AnimeListView
urlpatterns = [
    path('home/',home,name='home'),
    path('list/',listView.as_view(), name='list'),
    path('anime/',AnimeListView.as_view(), name='anime')
]
