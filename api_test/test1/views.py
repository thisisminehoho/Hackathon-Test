from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def echo(request):
    user_input = request.data.get("query", "")
    return Response({"response": f"You said: {user_input}"})
