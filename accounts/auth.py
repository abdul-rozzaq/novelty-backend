from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from .models import Token, _

class TokenAuthentication(TokenAuthentication):
    model = Token
    
    
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        return (token.user, token)