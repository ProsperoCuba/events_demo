"""
Column action for Table
actions: ['view', 'edit', 'remove' ]
"""
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django_tables2 import columns
import itertools

from django_tables2.utils import AttributeDict


ACTIONS_ATTR = {"th": {"class": "text-center"}, "td": {"class": "text-center"}}
SELECTION_ATTR = {'class': "kt-checkbox kt-checkbox--bold kt-checkbox--info"}
HEADER_ATTR = {"class": "table"}


class TableMixinCounter(tables.Table):
    counter = tables.TemplateColumn('{{ }}', verbose_name="No")

    class Meta:
        sequence = ('counter', '...')
        attrs = HEADER_ATTR

    def __init__(self, *args, **kwargs):
        super(TableMixinCounter, self).__init__(*args, **kwargs)
        self.count = itertools.count()

    def render_counter(self):
        return next(self.count) + 1


class CustomCheckboxColumn(tables.columns.CheckBoxColumn):

    @property
    def header(self):
        default = {"type": "checkbox"}

        general = self.attrs.get("input")
        specific = self.attrs.get("th__input")
        attrs = AttributeDict(default, **(specific or general or {}))

        input = "<input %s/ autocomplete='off'><span></span>" % attrs.as_html()
        header_attrs = AttributeDict(SELECTION_ATTR)
        label = f"<label {header_attrs.as_html()}>{input}</label>"

        return mark_safe(label)

    def render(self, value, bound_column, record):
        input = super(CustomCheckboxColumn, self).render(value, bound_column, record)
        # include span
        input = input + "<span></span>"
        attrs = AttributeDict(SELECTION_ATTR)
        label = f"<label {attrs.as_html()}>{input}</label>"

        return mark_safe(label)


class TableMixinSelection(tables.Table):
    selection = CustomCheckboxColumn(accessor="pk")

    class Meta:
        sequence = ('selection', '...')
        attrs = HEADER_ATTR


class TranslatedTable(tables.Table):
    def __init__(self, *args, **kwargs):
        super(TranslatedTable, self).__init__(*args, **kwargs)
        for column in self.base_columns:
            verbose = self.base_columns[column].verbose_name
            if verbose:
                self.base_columns[column].verbose_name = _(verbose)
            else:
                self.base_columns[column].verbose_name = _(column)


class CustomHeadersMixinTable(tables.Table):
    def __init__(self, *args, **kwargs):
        super(CustomHeadersMixinTable, self).__init__(*args, **kwargs)

        for key, value in self.Meta.headers.items():
            if key in self.base_columns:
                self.base_columns[key].verbose_name = value
