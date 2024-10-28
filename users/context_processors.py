from users.models import Profile

def profile(request):
    if not request.user.is_authenticated or request.user.is_superuser:
        current_user_profile = None
    else:
        current_user_profile = Profile.objects.get(user=request.user)
    return {'current_user_profile': current_user_profile}