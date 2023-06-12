from rest_framework import permissions
class OnlyOwnerCanView(permissions.BasePermission):
    def has_permission(self, request, view):
        def has_permission(request, view):
            if request.user.is_superuser:
                return True
            if request.user.is_authenticated:
                return True
            if  request.method in permissions.SAFE_METHODS:
                return True


    def has_object_permission(self, request, view, obj):
        def has_object_permission(request, view, obj):
            if request.user.is_superuser:
                return True
            return  obj.owner == request.user
                 