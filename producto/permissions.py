from functools import wraps
from django.http import HttpResponseForbidden

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Usuario no autenticado")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator



