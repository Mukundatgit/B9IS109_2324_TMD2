from django.urls import path
from account import views

app_name = "account"

urlpatterns = [


    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
