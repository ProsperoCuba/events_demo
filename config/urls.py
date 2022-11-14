"""Events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from utils.views import set_user_language

admin.site.site_header = _("Events Administration")
admin.site.site_title = _("Events Admin Portal")
admin.site.index_title = _("Welcome to Events Admin")

urlpatterns = [
    path('', RedirectView.as_view(url='/support', permanent=False), name='core'),
    path('support/', admin.site.urls),

    # apps
    path('api/v1/', include("api.urls")),
    path("auth/", include("allauth.urls")),
    path('core/', include("core.urls")),
    path('users/', include("users.urls")),
    path("select2/", include("django_select2.urls")),
    path("language/", set_user_language, name="set_user_language"),
]

# Custom images and assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [path("translations/", include("rosetta.urls"))]
