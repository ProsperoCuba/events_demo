import django_filters
from django.utils.translation import ugettext_lazy as _
from django_filters import FilterSet

CHOICES_BOOLEAN_FILTER = (
    (0, _("No")),
    (1, _("Yes")),
)


class SearchFilter(FilterSet):
    search = django_filters.CharFilter(label=_("Search"), method="my_custom_filter")

    class Meta:
        fields = ("search",)

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })
