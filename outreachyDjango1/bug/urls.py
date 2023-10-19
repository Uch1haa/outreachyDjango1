from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_bug, name='register_bug'),
    path('<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('list/', views.bug_list, name='bug_list'),
]