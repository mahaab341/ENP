from django.urls import path
from . import views

urlpatterns = [
    # Main navigation pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('package/', views.package, name='package'),
    path('destination/', views.destination, name='destination'),
    path('team/', views.team, name='team'),
    path('map/', views.map, name='map'),
    path('planner/', views.planner, name='planner'),
    path('weather/', views.weather, name='weather'),
    #hotels
    path('hotels/', views.hotels, name='hotels'),
    
    # Additional pages
    path('feedback/', views.feedback, name='feedback'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('login/', views.login, name='login')

    # Authentication pages

 
]