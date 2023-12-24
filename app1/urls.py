from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_registration),
    path('FLEXBOOK', views.main),
    path('registration', views.registre_proccess),
    path('login', views.login_proccess),
    path('post', views.post),
    path('comment/<int:id>', views.comment),
    path('change_avatar', views.change),
    path('update_avatar', views.update),
    path('like/<int:id>', views.like),
    path('control', views.control),
    path('control/<int:id>', views.control_del),
    path('send/<int:id>', views.send_request),
    path('accept/<int:id>', views.accept_request),
    path('delete/<int:id>', views.delete_post),
    path('delete_comment/<int:id>', views.delete_comment),
    path('sendmessage/<int:id>', views.send_message),
    path('message/<int:id>/', views.message_page),
    path('validate', views.check),
    path('message_continuos_update', views.message_continuos_update),
    path('count_comment/<int:id>', views.count_comment),
    path('friend_request_update', views.friend_request_update),
    path('edit_post/<int:id>', views.edit_post),
    path('text_message_update/<int:id>/', views.text_message_update),
    path('logout', views.logout),
]
