from django.urls import path,include

from . import views
urlpatterns=[ 
    path('register/',views.RegisterVw,name='register'),
    path('',include('django.contrib.auth.urls')),
]