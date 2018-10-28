from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:pk>/', views.userIndex, name='user_name'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('add/', views.register, name='add'),
    path('log/' , views.log, name='login'),
    path('log2/', views.log2, name='logout'),
    path('deposit/<int:pk>/', views.deposit, name='deposit'),
    path('withdraw/<int:pk>/', views.withdraw, name='withdraw')

    # path('user/' , views.thisUser, name='thisUser'),

]