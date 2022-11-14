from django.shortcuts import redirect
from django.utils.translation import LANGUAGE_SESSION_KEY, activate as activate_language


# Set User Language
def set_user_language(request):
    user_language = request.GET.get("language")
    if request.user.is_authenticated:
        user = request.user
        user.preferred_language = user_language
        user.save()
    activate_language(user_language)
    request.session[LANGUAGE_SESSION_KEY] = user_language
    request.LANGUAGE_CODE = user_language
    current_url = request.META.get("HTTP_REFERER") if request.META.get("HTTP_REFERER") is not None else "/"
    return redirect(current_url)
