from django.utils.deprecation import MiddlewareMixin

from .models import Shop


class ShopAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        session = request.session.get('shop_id')
        request.shop = None
        
        
        if session:
            shop = Shop.objects.filter(pk=session)
            
            if shop.exists():
                request.shop = Shop.objects.get(pk=session)
        
        return request

    def __call__(self, request):
        return self.get_response(self.process_request(request))