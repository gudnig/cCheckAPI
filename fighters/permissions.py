from rest_framework import permissions

class IsTrainerOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If trainer grant access
        if request.user.fighter.is_trainer:
            return True
        # If owner grant access
        return obj.user == request.user

class IsTrainerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.fighter.is_trainer

class IsTrainer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return true

class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.fighter.is_admin

class CanPost(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.fighter.can_post_notifications