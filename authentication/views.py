from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from django.conf import settings
from .forms import CustomUserCreationForm, LoginForm
from .models import TouristProfile, VendorProfile, CustomUser

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        
        # Check if Google OAuth is configured
        google_configured = bool(
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', None) and 
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None) and
            settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY != 'your_google_client_id_here'
        )
        
        return render(request, 'authentication/login.html', {
            'form': form, 
            'google_configured': google_configured,
            'register_mode': False
        })
    
    def post(self, request):
        form = LoginForm(request.POST)
        google_configured = bool(
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', None) and 
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None)
        )
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authenticate using email or username
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                
                # Redirect based on user type
                if user.user_type == 'vendor':
                    return redirect('vendor:dashboard')  # Make sure this URL exists
                else:
                    return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
        
        return render(request, 'authentication/login.html', {
            'form': form, 
            'google_configured': google_configured,
            'register_mode': False
        })

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = CustomUserCreationForm()
        
        google_configured = bool(
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', None) and 
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None) and
            settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY != 'your_google_client_id_here'
        )
        
        return render(request, 'authentication/login.html', {
            'form': form, 
            'register_mode': True,
            'google_configured': google_configured
        })
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        google_configured = bool(
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', None) and 
            getattr(settings, 'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None)
        )
        
        if form.is_valid():
            try:
                user = form.save()
                
                # Create appropriate profile
                if user.user_type == 'tourist':
                    TouristProfile.objects.create(user=user)
                else:  # vendor
                    VendorProfile.objects.create(
                        user=user,
                        company_name=form.cleaned_data.get('company_name', ''),
                        business_type=form.cleaned_data.get('business_type', ''),
                        business_address=form.cleaned_data.get('business_address', '')
                    )
                
                # Login user
                login(request, user)
                messages.success(request, f'Account created successfully! Welcome, {user.username}!')
                
                if user.user_type == 'vendor':
                    return redirect('vendor:dashboard')
                else:
                    return redirect('home')
            
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
        else:
            # Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
        
        return render(request, 'authentication/login.html', {
            'form': form, 
            'register_mode': True,
            'google_configured': google_configured
        })

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('authentication:login')