from django.http import JsonResponse
from django.views.generic import View


class Authorise(View):
    """
    Authorise the user and initiate a chat.
    """

    def post(self, request):
        print(request.user)
        return JsonResponse({"status": "success"})
