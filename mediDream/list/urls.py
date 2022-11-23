from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.list_view,name='list'),
    path('info/<str:word>',views.pill_info,name='pill'),
]