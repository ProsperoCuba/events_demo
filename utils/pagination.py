from collections import OrderedDict

from rest_framework_datatables.pagination import DatatablesPageNumberPagination
from rest_framework.response import Response


class CustomDatatablesPageNumberPagination(DatatablesPageNumberPagination):

    page_size_query_param = 'length'

    def get_paginated_response(self, data):
        """
        Override to include page number on paginated responses
        """
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('num_pages', self.page.paginator.num_pages),
            ('page', self.page.number),
            ('results', data)
        ]))

    def get_paginated_response_schema(self, schema):
        """
        Override to include page number on paginated responses
        """
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'next': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{page_query_param}=4'.format(
                        page_query_param=self.page_query_param)
                },
                'previous': {
                    'type': 'string',
                    'nullable': True,
                    'format': 'uri',
                    'example': 'http://api.example.org/accounts/?{page_query_param}=2'.format(
                        page_query_param=self.page_query_param)
                },
                'page': {
                    'type': 'int',
                    'nullable': False,
                    'example': 1,
                },
                'results': schema,
            },
        }
