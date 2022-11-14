# MENUS = {
#     "NAV_MENU_LEFT": [
#
#         # PUBLIC MENU OPTIONS
#         {
#             "name": "My Panel",
#             "icon_class": "fas fa-desktop",
#             "url": 'dashboard',
#             "root": True,
#         },
#
#         {
#             "name": "Users",
#             "icon_class": "fas fa-users-cog",
#             "url": '#',
#             "root": True,
#             "validators": [
#                 'dashboard.menu_validators.has_accounting_permission'
#             ],
#             "submenu": (
#                 {
#                     "name": "Directory",
#                     "url": 'users:user_list',
#                     "validators": [
#                         ('menu_generator.validators.user_has_permission', 'users.view_user')
#                     ],
#                 },
#                 # {
#                 #     "name": _("Grupos y Permisos"),
#                 #     # "url": 'users:group_list',
#                 #     "url": '#',
#                 #     "validators": [
#                 #         ('menu_generator.validators.user_has_permission', 'auth.view_group')
#                 #     ],
#                 # },
#                 # {
#                 #     "name": _("Email Address"),
#                 #     # "url": 'accounting:emails',
#                 #     "url": '#',
#                 #     "validators": [
#                 #         ('menu_generator.validators.user_has_permission', 'account.view_emailaddress')
#                 #     ],
#                 # },
#             )
#         },
#         # {
#         #     "name": _("Reports"),
#         #     "icon_class": "fas fa-chart-pie",
#         #     "url": '#',
#         #     "root": True,
#         #     "validators": [
#         #         'dashboard.menu_validators.has_report_permission'
#         #     ],
#         #     "submenu": (
#         #         {
#         #             "name": _("Transaction Report"),
#         #             "url": 'reports:transaction_report',
#         #             "validators": [],
#         #         },
#         #         {
#         #             "name": _("Inventory Report"),
#         #             "url": 'reports:inventory_report',
#         #             "validators": [],
#         #         },
#         #         {
#         #             "name": _("Signature Sheet Report"),
#         #             "url": 'reports:signature_sheet_report',
#         #             "validators": [],
#         #         },
#         #
#         #     )
#         # },
#
#         # {
#         #     "name": _("Support Settings"),
#         #     "icon_class": "fa fa-life-ring",
#         #     "url": "#",
#         #     "root": True,
#         #     "validators": [
#         #         'dashboard.menu_validators.has_faq_guides_permission'
#         #     ],
#         #     "submenu": (
#         #         {
#         #             "name": _("FAQ's"),
#         #             "url": 'faq:question',
#         #             "validators": [
#         #                 ('menu_generator.validators.user_has_permission', 'faq.view_question')
#         #             ],
#         #         },
#         #         {
#         #             "name": _("Guides"),
#         #             "url": 'guides:guide',
#         #             "validators": [
#         #                 ('menu_generator.validators.user_has_permission', 'guides.view_guide')
#         #             ],
#         #         }
#         #     )
#         # },
#
#     ],
#
# }
