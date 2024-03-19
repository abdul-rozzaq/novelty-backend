from django.http import HttpResponseBadRequest
from django.shortcuts import redirect


def login_required(function=None):
    def wrapped_view(request, *args, **kwargs):        
        if request.shop:
            return function(request, *args, **kwargs)
        else:
            return redirect('login_page')
    
    return wrapped_view
