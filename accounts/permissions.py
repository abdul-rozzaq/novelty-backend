from rest_framework.permissions import IsAuthenticated


class IsAuthenticated(IsAuthenticated):

    def has_permission(self, request, view):
        return bool(request.user)
