from django.urls import path
from . import views
urlpatterns=[
    path('', views.home, name='home')
]

urlpatterns=[
 path('',views.home, name='home'),
 path('add',views.add, name='add'),
 path('dashboard/',views.dashboard, name='dashboard'),
 path('link/',views.link,name='link'),
]