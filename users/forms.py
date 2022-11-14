# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Group
# from django_select2.forms import Select2Widget
# from phonenumber_field.formfields import PhoneNumberField
# from intl_tel_input.widgets import IntlTelInputWidget
#
# from django import forms
#
# from django.contrib.auth import get_user_model
#
# from django.utils.translation import gettext_lazy as _
# from users.widgets import TabularPermissionsWidget
# from utils.forms import AlphaOrderedColumnForm
#
# User = get_user_model()
#
#
# class CustomPhoneNumberField(PhoneNumberField):
#     default_error_messages = {"invalid": _("Please enter a correct phone number.")}
#
#
# class UserForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "email", "is_active",
#                   "password1", "password2"]
#         required_fields = ["first_name", "last_name", "email"]
#
#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#         for field in self.Meta.required_fields:
#             self.fields[field].required = True
#
#
# class AdminUserForm(UserForm):
#
#     class Meta(UserForm.Meta):
#         model = User
#         fields = UserForm.Meta.fields + ["is_active", "is_superuser", "is_staff"]
#
#
# class UserUpdateForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "email"]
#         required_fields = ["first_name", "last_name", "email"]
#
#     def __init__(self, *args, **kwargs):
#         super(UserUpdateForm, self).__init__(*args, **kwargs)
#         for field in self.Meta.required_fields:
#             self.fields[field].required = True
#
#
# class AdminUserUpdateForm(UserUpdateForm):
#
#     class Meta(UserUpdateForm.Meta):
#         model = User
#         fields = UserUpdateForm.Meta.fields + ["is_active", "is_superuser", "is_staff"]
#
#
# class UserAssignGroupForm(forms.ModelForm):
#     groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=False, label=_('Groups'))
#
#     class Meta:
#         model = User
#         fields = ["groups"]
#
#
# class UserAssignPermissionForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ["user_permissions"]
#
#     def __init__(self, *args, **kwargs):
#         permissions = kwargs.pop("user_permissions", None)
#         super(UserAssignPermissionForm, self).__init__(*args, **kwargs)
#         self.fields['user_permissions'].queryset = permissions
#         self.fields["user_permissions"].widget = TabularPermissionsWidget(
#             verbose_name=_("Permissions"), is_stacked=True, permissions_list=permissions
#         )
#
#
# class UserDeactivationForm(forms.ModelForm):
#     deactivate = forms.BooleanField(label=_("Confirm deactivate the user account"),
#                                     widget=forms.CheckboxInput(attrs={"enabled": False}))
#
#     class Meta:
#         model = User
#         fields = (
#             "deactivate",
#         )
#
