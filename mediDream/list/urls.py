from django.urls import path
from . import views

urlpatterns=[
    path('',views.list_view,name='list'),
    path('info/<int:word>',views.pill_info,name='pill'),
]