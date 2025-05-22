from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions allowed to anyone
        if request.method in SAFE_METHODS:
            return True

        # Write permissions only to owner
        return obj.owner == request.user
