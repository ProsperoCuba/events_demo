from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django_select2.forms import Select2TagWidget


def get_template_text(template, context=None):
    if 'django.contrib.messages' in settings.INSTALLED_APPS:
        try:
            return render_to_string(template, context or {}).strip()
        except TemplateDoesNotExist:
            return ""
    return ""


class TagCoreWidget(Select2TagWidget):
    def value_from_datadict(self, data, files, name):
        values = super(TagCoreWidget, self).value_from_datadict(data, files, name)
        return ",".join(values)

    def optgroups(self, name, value, attrs=None):
        subgroup = None
        if value:
            values = value
            selected = set(values)
            subgroup = [self.create_option(name, v, v, selected, i) for i, v in enumerate(values)]
        return [(None, subgroup, 0)]