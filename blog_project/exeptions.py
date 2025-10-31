from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            'error': response.data.get('detail', 'An error occurred'),
            'status_code': response.status_code,
            'errors': response.data
        }
        response.data = custom_response_data

    return response