from rest_framework.permissions import BasePermission
from .models import User

class EmpsPermissions(BasePermission):
    def has_permission(self, request, view):
        print(request.user.role)
        return bool(request.user and request.user.is_authenticated and request.user.role=="Level S")
    

class EmpaPermissions(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role=="Level A")
    


class SuperUserPermissions(BasePermission):
    def has_permission(self, request, view):
        print(request.user, request.user.is_superuser)
        return bool(request.user and request.user.is_superuser)
    
class EmpS_Plus_SuperUserPermissions(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.role=="Level S" or request.user.is_superuser))