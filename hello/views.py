from django.http import HttpResponse
from .models import Greeting


def hello_view(request):
    msg = Greeting.objects.first()
    text = msg.message if msg else 'Hello, CI/CD!'
    return HttpResponse(text)
