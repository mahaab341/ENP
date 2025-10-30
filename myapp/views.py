from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    # If user is authenticated, show personalized home
    if request.user.is_authenticated:
        packages = [
            {
                'image': 'img/package-1.jpg',
                'location': 'Murree',
                'duration': '3 Days',
                'persons': '2 Person',
                'price': 'Rs.30,000',
                'description': '"Murree the crown of Pakistan\'s hills, where clouds kiss the mountains."'
            },
            {
                'image': 'img/sawat.jpeg',
                'location': 'Swat',
                'duration': '3 Days', 
                'persons': '2 Person',
                'price': 'Rs.25,000',
                'description': '"Swat – the emerald valley where rivers sing and mountains whisper."'
            },
        ]
        
        travel_guides = [
            {
                'image': 'img/sana.jpeg',
                'name': 'Sana Khan',
                'username': '@sanakhaan21',
                'facebook': '#',
                'twitter': '#', 
                'instagram': '#',
                'youtube': '#'
            },
        ]
        
        testimonials = [
            {
                'image': 'img/female.jpeg',
                'name': 'Maha',
                'location': 'Gujranwala,Pakistan',
                'comment': 'Tempor erat elitr rebum at clita. Diam dolor diam ipsum sit diam amet diam et eos. Clita erat ipsum et lorem et sit.'
            },
        ]
        
        context = {
            'packages': packages,
            'travel_guides': travel_guides,
            'testimonials': testimonials,
            'user': request.user  # Add user to context
        }
    else:
        # Show basic home page for non-authenticated users
        context = {}
    
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def package(request):
    return render(request, 'package.html')

def planner(request):
    return render(request, 'planner.html')

def map(request):
    return render(request, 'map.html')

def weather(request):
    return render(request, 'weather.html')

def destination(request):
    return render(request, 'destination.html')

def team(request):
    return render(request, 'team.html')

def feedback(request):
    return render(request, 'feedback.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def page_404(request):
    return render(request, '404.html')

def dashboard(request):
    return render(request, 'admin_dashboard.html')

def login(request):
    return render(request, 'login.html')

