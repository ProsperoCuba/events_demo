# from django.contrib import messages
# from django.views.generic.edit import ModelFormMixin
#
# from core.utils import get_template_text
#
#
# class MessageMixin(ModelFormMixin):
#     invalid_message = None
#     success_message = None
#     message_gender = "M"
#
#     def form_invalid(self, form):
#         if not form.non_field_errors:
#             if not self.invalid_message:
#                 self.invalid_message = get_template_text('messages/form_invalid.html')
#             messages.error(self.request, self.invalid_message)
#         return super(MessageMixin, self).form_invalid(form)
#
#     def form_valid(self, form):
#         template = 'messages/create_success.html'
#         if form.instance and form.instance.pk:
#             template = 'messages/update_success.html'
#         template_kwargs = {
#             "model": self.model._meta.verbose_name.title(),
#             "gender": self.message_gender
#         }
#         messages.success(self.request, get_template_text(template, template_kwargs))
#         return super(MessageMixin, self).form_valid(form)
