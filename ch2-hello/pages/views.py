from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Hello, world! This is the home view.")
