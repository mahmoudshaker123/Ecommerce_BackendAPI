from django.http import JsonResponse
from rest_framework.response import Response 


def handler404(request,exception):
    message = ('Path not found')
    response = JsonResponse(data={'error':message})
    response.status_code = 404
    return response


def handler500(request):
    message = ('Internal server error mahmoud.')
    response = JsonResponse(data={'error':message})
    response.status_code = 500
    return response