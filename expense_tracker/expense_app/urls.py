from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.userIndex, name='user_name'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('add/', views.add, name='add')

    # path('user/' , views.thisUser, name='thisUser'),

]