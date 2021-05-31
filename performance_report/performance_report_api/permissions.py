from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    def has_object_permission(self, request, view, obj):
        return False