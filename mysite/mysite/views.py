from django.http import HttpResponse
def options(request):
    body = f"<h1>You are at homepage</h1>"
    return HttpResponse(body)