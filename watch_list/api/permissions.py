from rest_framework import permissions



class IsReviewerOrReadOnly(permissions.BasePermission):
    def has_obejct_permission(self, request, view, obj):
        # ei review jodi user na likhe thake taile read only access pabe
        # jodi user review likhe thake taile read, update & delete er access pabe
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.reviewer == request.user
