from rest_framework import permissions

class CanModifyProducts(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.groups.filter(name="Employee").exists():
            if request.method == 'GET':
                return True
            else:
                return False
        else:
            return True


class CanModifySale(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.groups.filter(name="Employee").exists():
            if request.method == 'GET' or request.method == 'POST':
                return True
            else:
                return False
        else:
            return True