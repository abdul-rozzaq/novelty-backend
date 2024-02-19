from django.http import HttpResponseBadRequest
from django.shortcuts import redirect


def shop_check_decorator(function=None, login_url=None):
    def wrapped_view(request, *args, **kwargs):        
        if 'shop_id' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('login_page')

    return wrapped_view
