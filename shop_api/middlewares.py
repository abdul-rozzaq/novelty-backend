from django.utils.deprecation import MiddlewareMixin

from shop_api.models import Shop, Token


class ShopAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request.shop = None
        auth_header = request.headers.get("Authorization")

        if auth_header is not None:
            _, key = auth_header.split(' ')
            token = Token.objects.select_related('shop').filter(key=key)

            if token.exists():
                request.shop = token.first().shop

        return request

    def __call__(self, request):
        return self.get_response(self.process_request(request))
