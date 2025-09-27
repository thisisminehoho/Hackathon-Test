from django.http import JsonResponse

def echo(request):
    return JsonResponse({"message": "Hello from test1!"})
