from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-input'
    }))
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'form-input'
    }))
    phone_number = forms.CharField(max_length=17, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'form-input'
    }))
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-input'
    }))
    
    # Vendor specific fields
    company_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Company Name',
        'class': 'form-input vendor-field'
    }))
    business_type = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Business Type',
        'class': 'form-input vendor-field'
    }))
    business_address = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'placeholder': 'Business Address',
        'class': 'form-input vendor-field',
        'rows': 3
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'full_name', 'phone_number', 'user_type')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        # Split full name into first and last name
        full_name = self.cleaned_data['full_name'].split(' ', 1)
        user.first_name = full_name[0]
        user.last_name = full_name[1] if len(full_name) > 1 else ''
        
        user.phone_number = self.cleaned_data['phone_number']
        user.user_type = self.cleaned_data['user_type']
        
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-input'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-input'
    }))