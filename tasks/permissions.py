from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit/view it.
    """
    def has_permission(self, request, view):
        # Ensure the user is authenticated for any request 
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin Role: Has full access to any task 
        if request.user.groups.filter(name='Admin').exists():
            return True
        
        # User Role: Can only access tasks they own 
        return obj.owner == request.user