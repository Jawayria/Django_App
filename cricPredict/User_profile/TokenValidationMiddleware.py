from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.utils.deprecation import MiddlewareMixin


class TokenValidationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if 'Authorization' in request.headers:
            token = str(request.headers.get('Authorization')).split()[1]

            if cache.get(token) is not None:
                raise ValidationError(message='Invalid Token')

        return None

    def process_response(self, request, response):
        return response
