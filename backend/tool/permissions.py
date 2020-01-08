from rest_framework.permissions import BasePermission


class IsLogin(BasePermission):
    def has_permission(self, request, view):
        pass
