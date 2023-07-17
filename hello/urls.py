from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    path('mekky',views.mekky,name="Mekky"),
    path('login',views.login,name='login')

]