from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import SessionAuthentication
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from django.conf import settings

urlpatterns = [
    path("docs/", include_docs_urls(title=str(_("Events API Docs")), public=False,
                                            permission_classes=(AllowAny,),
                                            authentication_classes=(SessionAuthentication,), schema_url='/')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('auth/', include('dj_rest_auth.urls')),

    # Apps
    # path('address/', include('address.api.urls')),
    path('users/', include("users.api.urls")),
    path('rooms/', include("rooms.api.urls")),
    path('events/', include("events.api.urls")),
    path('reservations/', include("reservations.api.urls")),

]

# Documentation
if settings.DEBUG:
    urlpatterns += [
        path('auth/', include('rest_framework.urls'))
    ]

