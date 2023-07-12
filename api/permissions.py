from rest_framework import permissions
from .models import *


class ViewTestNonDraft(permissions.BasePermission):
    def has_permission(self, request, view):
        obj = Test.objects.all()
        for x in obj:
            if x.status == "Опубликован":
                return True
            else:
                return bool(request.user and request.user.is_staff)
