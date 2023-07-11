from rest_framework import permissions
from .models import *

def ObjectView(table):
    return table.objects.all()

class ViewTestNonDraft(permissions.BasePermission):
    def has_permission(self, request, view):
        obj = ObjectView(Test)
        for x in obj:
            if x.status != "Черновик":
                return True
            else:
                return bool(request.user and request.user.is_staff)

""" class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff) """