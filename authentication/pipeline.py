from .models import TouristProfile, VendorProfile

def create_user_profile(backend, user, response, *args, **kwargs):
    """
    Create user profile after social authentication
    """
    if backend.name == 'google-oauth2':
        # Set user details from Google
        if not user.first_name and response.get('given_name'):
            user.first_name = response.get('given_name', '')
        if not user.last_name and response.get('family_name'):
            user.last_name = response.get('family_name', '')
        if not user.email and response.get('email'):
            user.email = response.get('email', '')
        
        # Set default user type to tourist for social auth users
        if not user.user_type:
            user.user_type = 'tourist'
        
        user.save()
        
        # Create appropriate profile if it doesn't exist
        if user.user_type == 'tourist' and not hasattr(user, 'tourist_profile'):
            TouristProfile.objects.create(user=user)
        elif user.user_type == 'vendor' and not hasattr(user, 'vendor_profile'):
            VendorProfile.objects.create(
                user=user,
                company_name=f"{user.get_full_name() or user.username}'s Business",
                business_type="Travel Services",
                business_address="To be updated"
            )