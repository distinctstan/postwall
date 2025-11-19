from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.signin,name='login'),
    path('logout/',views.signout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/update/',views.update_profile,name='update_profile'),
]
