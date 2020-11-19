from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('try/', views.try_it, name='try_it'),
    path('login/', views.login, name='login'),
    path('quizz/', views.quizz, name='quizz'),
    path('quizz/microscopy/', views.microscopy, name='microscopy'),
    path('quizz/biological/', views.biological, name='biological'),
    path('quizz/explore/', views.explore, name='explore')
]
