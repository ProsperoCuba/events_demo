from django.conf import settings as app_settings
from django.contrib.sites.shortcuts import get_current_site


def settings(request):
    """
    Return settings context variables for use in templates.
    """
    context_extras = dict()

    context_extras['current_site'] = get_current_site(request)
    context_extras['web_domain'] = "{}://{}".format("https" if request.is_secure() else "http", app_settings.DOMAIN)

    return context_extras
