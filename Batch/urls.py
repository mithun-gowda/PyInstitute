from django.urls import path

from . import views

urlpatterns=[ 
    path('sub/',views.SubjectVW,name='sub'),
    path('trainer/',views.TrainerVW,name='trainer'),
    path('profile/',views.TranierDisplay,name='profile'),
    path('batchvw/',views.BatchVW,name='batchvw'),
    path('bdisplay/',views.BatchDisplay,name='bdisplay'),
    path('trainerupdate/<pk>/',views.TrainerUP,name='trainerupdate'),
    path('Home/',views.Home,name='Home'),
]