from django.urls import path
from . import views

urlpatterns = [
    path('registerform/',views.createUserView,name='register'),
    # path('demo/',views.demoView,name='demo'),
    path('loginform/',views.loginUserView,name='login'),

    
]