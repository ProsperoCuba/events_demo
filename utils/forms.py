import unidecode

from django import forms
from django.core.exceptions import ImproperlyConfigured


class AlphaOrderedForm(forms.ModelForm):
    """
    Abstract Model Form to be used for ordering form fields alphabetically
    """

    def __init__(self, *args, **kwargs):
        if not hasattr(self.Meta, 'ordered_fields'):
            raise ImproperlyConfigured("Must provide the ordered_fields Meta with a list of fields keys to be ordered")

        super(AlphaOrderedForm, self).__init__(*args, **kwargs)

        # init variable to append form field labels
        values_to_order = dict()
        for key in self.fields:
            if key in self.Meta.ordered_fields:
                l = self[key].label
                # remove any unicode characters
                lt = unidecode.unidecode(l)
                values_to_order.update({key: lt})

        # orders dictionary based con the value (labels)
        ordered_dict = [k for k, v in sorted(values_to_order.items(), key=lambda item: item[1])]

        # call internal order_fields to rearrange form fields
        self.order_fields(ordered_dict)


class AlphaOrderedColumnForm(AlphaOrderedForm):
    """
    Abstract Model Form to be used for ordering form fields alphabetically
    """

    def __init__(self, *args, **kwargs):
        super(AlphaOrderedColumnForm, self).__init__(*args, **kwargs)
        if not hasattr(self.Meta, 'columns'):
            raise ImproperlyConfigured(
                "Must provide the columns Meta with an integer representing total columns to use")

        if not isinstance(self.Meta.columns, int):
            raise ImproperlyConfigured("Must provide an integer for the columns Meta")

        self.fields_per_column = self.get_fields_per_column()

    def get_fields_per_column(self):
        return int(round(len(self.fields) / self.Meta.columns))
