from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import AnonymousUser


class IsAuthenticated(IsAuthenticated):

    def has_permission(self, request, view):

        return request.shop != None
