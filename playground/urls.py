# for mapping urls and functons
from django.urls import path
from . import views # . (dot) means current folder

#create a URLConf ie URL configuration
urlpatterns = [
        #url or route  ,    pass reference to the function
    path('hello/', views.sey_Hello)
]