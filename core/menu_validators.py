# from django.contrib.auth.models import Group
#
#
# def has_full_control(request):
#     return request.user.is_superuser
# #
# # def has_accounting
#
#
# def has_module_perms(request, module):
#     """
#     Returns True if request.user has the permission else returns False
#     :param request: HttpRequest
#     :param module: Has any permission of module to be searched
#     """
#     return request.user.has_module_perms(module)
#
#
# def has_users_permission(request):
#     user = request.user
#
#     return user.has_perm('users.manage_users') or user.manage_users
#
#
# def has_accounting_permission(request):
#     user = request.user
#     return user.manage_users or request.user.has_perm('auth.view_group')
#
#
# def has_store_and_resources_permission(request):
#     user = request.user
#     return any([user.manage_stores, user.manage_resources, user.manage_platforms, user.manage_resource_types,
#                 user.has_perm('stores.view_store'), user.has_perm('stores.view_platform'),
#                 user.has_perm('stores.view_resourcetype'), user.has_perm('stores.view_resourcetype')])
#
#
# #TODO: update permissions down
#
# def has_payment_permission(request):
#
#     return request.user.has_module_perms('taxes') or request.user.has_perm('ltc_stripe_core.view_payment') or \
#            request.user.has_perm('ltc_stripe_core.view_paymentrefund') or \
#            request.user.has_perm('djstripe.view_bankaccount') or \
#            request.user.has_perm('djstripe.view_transfer') or \
#            request.user.has_perm('djstripe.view_transferreveral') or \
#            request.user.has_perm('ltc_stripe_connect.view_transferlog') or \
#            request.user.has_perm('payment.view_setting') or \
#            request.user.has_perm('payment.view_connectpayout') or \
#            request.user.has_perm('djstripe.view_card') or \
#            request.user.has_perm('ordering.process_payment')
#
#
# def has_coupon_permission(request):
#     return request.user.has_perm('coupon.manage_coupons') and request.user.has_perm('coupon.view_coupon')
#
#
# def has_entity_coupon_permission(request):
#     return not request.user.has_perm('coupon.manage_coupons') and request.user.has_perm('coupon.view_coupon')
#
#
# def has_map_permission(request):
#     return request.user.has_perm('ordering.view_order') or request.user.has_perm('distribution.view_distribution')
#
#
# def has_human_resources_permission(request):
#     return request.user.has_perms(['entity.view_employee']) or \
#         request.user.has_perm('signature_sheet.view_signaturesheet')
#
#
# def has_faq_guides_permission(request):
#     return request.user.has_perm('faq.view_question') or \
#     request.user.has_perm('guides.view_guide')
#
#
# def has_stripe_sync_permission(request):
#
#     if request.user.is_distributor():
#         business = request.user.individual_business
#         if business.use_stripe and not business.stripe_connect_account:
#             return True
#     return False
#
#
# def has_entity_stripe_sync_permission(request):
#
#     if request.user.is_entity_owner():
#         entity = request.user.get_entity()
#         if entity.use_stripe and not entity.stripe_connect_account:
#             return True
#
#     return False
#
#
# def has_affiliate_stripe_sync_permission(request):
#
#     if request.user.is_affiliate():
#         return True if not request.user.get_business() else False
#
#     return False
#
#
# def has_only_view_payment(request):
#     return not request.user.has_perm('ltc_stripe_core.manage_payment') and request.user.has_perm('ltc_stripe_core.view_payment')
#
#
# def has_only_admin_manage_payment(request):
#     return request.user.has_perm('ltc_stripe_core.manage_payment') and request.user.has_perm('ltc_stripe_core.view_payment')
#
#
# def has_only_process_payment(request):
#     return not request.user.has_perm('ltc_stripe_core.manage_payment') and request.user.has_perm('ordering.process_payment')
#
#
# def has_report_permission(request):
#     return request.user.has_perm('accounting.manage_reports') or request.user.has_perm('accounting.view_report')
#
#
# def has_signature_sheet_permission(request):
#     return request.user.has_perm('signature_sheet.manage_signature_sheet') or request.user.has_perm('signature_sheet.view_signaturesheet')
#
#
# def has_idanalyzerlog_permission(request):
#     return request.user.has_perm('idanalyzer.manage_idanalyzerlogs') or request.user.has_perm('idanalyzer.view_idanalyzerlog')
#
#
# def has_giftset_permission(request):
#     return request.user.has_perm('inventory.view_warehousesku') or request.user.has_perm('inventory.view_entitysku')
#
#
# # new after menu restructure
# def has_menu_entity_permission(request):
#     permissions = ['entity.view_entity', 'entity.add_entity', 'inventory.view_category', 'core.view_region',
#                    'inventory.view_package', 'inventory.view_expertscore', 'inventory.view_filtertagsection',
#                    'inventory.view_warehousesku', 'inventory.view_supplyrequest']
#
#     return any([request.user.has_perm(perm) for perm in permissions])
#
#
# # new after menu restructure
# def has_menu_inventory_permission(request):
#     permissions = ['inventory.view_warehousesku', 'inventory.view_entityku', 'inventory.view_product',
#                    'inventory.view_inventoryprovider',
#                    'inventory.view_inventoryreceipt', 'inventory.view_inventorylocation',
#                    'inventory.view_inventorylocationtype']
#
#     return any([request.user.has_perm(perm) for perm in permissions])
