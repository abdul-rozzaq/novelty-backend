from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework import exceptions

from .models import Token



class TokenAuthentication(TokenAuthentication):
    model = Token
    related_field = 'user'    
    
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related(self.related_field).get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')

        return (token.user, token)
