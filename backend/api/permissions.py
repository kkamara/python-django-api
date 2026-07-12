from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    # In `permissions.DjangoModelPermissions`,
    # `perms_map['GET']` is an empty list, which
    # means that a user with no permissions can
    # view the list of products.
    # This is not what we want.
    # We want to restrict access to users with
    # specific permissions. Which is what we do
    # here by overriding the `perms_map` attribute
    # and adding the `view` permission to the `GET`
    # method.
    # The code in 
    # `permissions.DjangoModelPermissions` has the
    # logic to check if the user has the required
    # permissions for the request method.
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
        
    # def has_permission(self, request, view):
        # Example (
        #   flawed because `generics.ListCreateAPIView`
        #   will allow a user who only has the
        #   `products.view_product` permission to view
        #   products list _and_ create a product
        # ):
        # user = request.user
        # print(user.get_all_permissions())
        # if user.is_staff:
        #     #                "appname.verb_modelname"
        #     if user.has_perm("products.add_product"):
        #         return True
        #     if user.has_perm("products.change_product"):
        #         return True
        #     if user.has_perm("products.delete_product"):
        #         return True
        #     if user.has_perm("products.view_product"):
        #         return True
        #     return False
        # return False
