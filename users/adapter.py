# from allauth.account.adapter import DefaultAccountAdapter
# from django.contrib.sites.shortcuts import get_current_site
# from constance import config as constance_config
# from django.conf import settings
# from django.urls import reverse_lazy
# from modeltranslation.utils import get_language
# from users.enums import ProfileOptions
# from utils.utils import get_current_domain, get_current_site_no_request
#
#
# class CustomAllauthAdapter(DefaultAccountAdapter):
#     def get_email_confirmation_redirect_url(self, request):
#         """Redirect to next if in request GET params, used to properly redirect to checkout page after sign up though
#         session cart
#             :param request:
#             :return: url
#         """
#         if request.GET.get('next'):
#             return request.GET.get('next')
#         return super(CustomAllauthAdapter, self).get_email_confirmation_redirect_url(request)
#
#     def is_open_for_signup(self, request):
#         return constance_config.ALLOW_NEW_USERS
#
#     def send_confirmation_mail(self, request, emailconfirmation, signup):
#         """ Generate token with proper next={url} """
#
#         user = emailconfirmation.email_address.user
#         send_mail = True
#         if constance_config.ACTIVE_NEW_GUEST_ON_REGISTER:
#             user.is_active = True if user.profile == ProfileOptions.guest else False
#             send_mail = constance_config.SEND_ACTIVATION_EMAIL_FOR_NEW_GUEST
#         else:
#             user.is_active = False
#
#         user.save(update_fields=['is_active'])
#
#         if send_mail:
#             current_site = get_current_site(request) if request else get_current_site_no_request()
#             activate_url = reverse_lazy("account_confirm_email", kwargs={"key": emailconfirmation.key})
#             activate_url = f"{get_current_domain(remove_trailing=True)}{activate_url}"
#
#             ctx = {
#                 "user": emailconfirmation.email_address.user,
#                 "email": emailconfirmation.email_address.email,
#                 "activate_url": activate_url,
#                 "current_site": current_site,
#                 "key": emailconfirmation.key,
#                 'next': request.POST.get('next') if request else None
#             }
#             if signup:
#                 email_template = 'account/email/email_confirmation_signup'
#             else:
#                 email_template = 'account/email/email_confirmation'
#
#             self.send_mail(email_template,
#                            emailconfirmation.email_address.email,
#                            ctx)