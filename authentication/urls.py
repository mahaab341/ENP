from django.urls import path, include
from . import views

app_name = 'authentication'  # Keep app_name here

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]