from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    '''
    Allows access only to superuers.
    '''
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser