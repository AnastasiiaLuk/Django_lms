import time

from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print('Process REQUEST in SimpleMiddleware')
        start = time.time()
        response = self.get_response(request)
        print('Process RESPONSE in SimpleMiddleware')
        duration = time.time() - start
        print(f'duration for track {request.path}: {round(duration, 2)} sec')
        return response


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('Process REQUEST in MyMiddleware')

    def process_response(self, request, response):
        print('Process RESPONSE in MyMiddleware')
        return response