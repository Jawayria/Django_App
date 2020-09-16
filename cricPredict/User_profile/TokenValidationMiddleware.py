from django.core.cache import cache
from django.core.exceptions import ValidationError


class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)


class TokenValidationMiddleware(BaseMiddleware):

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'Authorization' in request.headers:
            token = str(request.headers.get('Authorization')).split()[1]

            if cache.get(token) is not None:
                raise ValidationError(message='Invalid Token')

        return None
