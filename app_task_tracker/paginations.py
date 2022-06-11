from rest_framework.pagination import PageNumberPagination, CursorPagination


class TeamResultsPagination(CursorPagination):
    page_size = 8
    cursor_query_param='cu'
    # page_size_query_param = 'page'
    max_page_size = 32