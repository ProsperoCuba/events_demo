import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from users.models import User


class UserFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(label=_("Address"), method="search_address")
    full_name = django_filters.CharFilter(label=_("Address"), method="search_full_name")

    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'email': ['icontains'],
            'phone_number': ['exact'],
            'gender': ['exact'],
            'profile': ['exact'],
            'identity_document': ['exact'],
            'document_number': ['icontains'],
            "address__province": ['exact'],
            "address__municipality": ['exact'],
            "address__postal_code": ['exact'],
            "language": ["exact"],
            "date_joined": ['lte', 'gte'],
            "groups__id": ['exact']
        }

    def search_address(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(address__address__icontains=value) |
                Q(address__postal_code__code__icontains=value) |
                Q(address__postal_code__locality__icontains=value) |
                Q(address__province__name__icontains=value) |
                Q(address__municipality__name__icontains=value)
            )
        return queryset

    def search_full_name(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(username__icontains=value) |
                Q(first_name__icontains=value) |
                Q(middle_name__icontains=value) |
                Q(last_name__icontains=value)
            )
        return queryset