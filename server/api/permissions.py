from rest_framework import permissions
from .models import *



       
class ViewTestNonDraft(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create_attempt':
            return True
        
class IsAuthAndAdmin(permissions.BasePermission):
     def has_permission(self, request, view):
        return bool(
            request.user.is_staff and
            request.user.is_authenticated
        )