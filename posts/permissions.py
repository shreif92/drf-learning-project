# posts/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # السماح بالقراءة لأي مستخدم
        if request.method in permissions.SAFE_METHODS:
            return True
        # السماح بالتعديل فقط للمؤلف الأصلي
        return obj.author == request.user
