from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import AnonymousUser


class IsAuthenticated(IsAuthenticated):

    def has_permission(self, request, view):

        return request.shop != None


class IsOwner(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.shop == obj.shop:
            return True

        return False
