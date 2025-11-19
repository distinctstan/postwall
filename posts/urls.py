from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.home,name='home'),
    path('post/add/',views.add_post,name='add'),
    path('post/update/<slug:slug>/',views.update_post,name='update'),
    path('post/delete/<slug:slug>/',views.delete_post,name='delete'),
    path('post/<slug:slug>/',views.detail,name='detail'),
]
