from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True, next_page='upcoming_events'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('users/', views.list_users, name='list_users'),
]
