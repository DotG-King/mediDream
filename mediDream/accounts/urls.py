from django.urls import path
from . import views

urlpatterns=[
    path('main/',views.main,name='main'),
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
