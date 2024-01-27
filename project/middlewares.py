from django.utils.deprecation import MiddlewareMixin

from project.models import Shop, Token


class ShopAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request.shop = None
        auth_header = request.headers.get("Authorization")

        if auth_header is not None:

            _, key = auth_header.split(' ')

            try:
                # request.shop = Shop.objects.get()
                token = Token.objects.select_related('shop').get(key=key)
                print(token)
                print(token.shop)
            except Exception as e:
                print(f'Error {e}')

        return request

    def __call__(self, request):
        return self.get_response(self.process_request(request))
