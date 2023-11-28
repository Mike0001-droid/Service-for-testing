from rest_framework import permissions
from .models import *



       
class ViewTestNonDraft(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create_attempt':
            print(request.META)
            return True
        
