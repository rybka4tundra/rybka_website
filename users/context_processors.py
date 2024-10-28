from users.models import Profile

def profile(request):
    if not request.user.is_authenticated or request.user.is_superuser:
        profile = None
    else:
        profile = Profile.objects.get(user=request.user)
    return {'profile': profile}