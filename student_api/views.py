from django.http import JsonResponse
from .tasks import greet_student

def greet_view(request):
    greet_student.delay('Ezra')
    return JsonResponse({"message": "Greeting task has been triggered."})
