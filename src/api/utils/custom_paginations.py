from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):

    def get_paginated_response(self, data):
        return {
            **data,
            **{
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
            }
        }
