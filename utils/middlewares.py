
from django.http import HttpResponse


class MiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lógica antes de la vista
        if not request.user.is_authenticated:
            return HttpResponse("No estás autenticado.")

        response = self.get_response(request)
        # Lógica después de la vista
        return response
