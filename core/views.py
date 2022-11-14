from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.views import View

from core.utils import get_template_text


@login_required
def dashboard_view(request):

    context = dict()

    context['title'] = _("Administration Panel")

    return render(request, "dashboard/dashboard.html", context)


class BulkDeleteView(View):

    model = None
    redirect_url = None
    queryset = None

    def get_queryset(self):
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )

        return queryset

    def get_model_class_meta(self):
        """
        Properly access model meta if either the model or the queryset was provided
        :return: Model instance meta
        """
        return self.get_queryset().model._meta

    def get_success_message(self):
        """
        text message to send when selection is successfully deleted
        :return: String
        """
        return get_template_text('messages/delete_success.html',
                                 {"model": self.get_model_class_meta().verbose_name_plural.title()})

    def get_no_selection_message(self):
        """
        text message to send when no selections are provided
        :return: String
        """
        return str(_("No {} selected")).format(self.get_model_class_meta().verbose_name_plural.title())

    def get_redirect_url(self):
        """
        validates that the redirect_url is provided.
        redirect_url is used for redirecting after success or attempting a method not allowed request
        :return: redirect_url
        """
        if self.redirect_url is not None:
            return self.redirect_url
        else:
            raise ImproperlyConfigured("No URL to redirect to.")

    def make_delete(self, selection):
        """
        Where actual logic happens. it deletes the selection provided based on the queryset
        :param selection: list of ids to delete
        """
        self.get_queryset().filter(pk__in=selection).delete()
        messages.success(self.request, self.get_success_message())

    def get(self, *args, **kwargs):
        return redirect(self.get_redirect_url())

    def post(self, *args, **kwargs):
        selection = self.request.POST.getlist("selection[]")

        if len(selection) > 0:

            self.make_delete(selection)
        else:
            messages.info(self.request, self.get_no_selection_message())
        return redirect(self.get_redirect_url())