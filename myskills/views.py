import requests
import json

from django.http import JsonResponse


# Create your views here.
def get_endpoint_data(request):
    url = "https://newsapi.org/v2/top-headlines?country=cu&language=es&apiKey=33b6de14b85345a8b0142a85128ffe59"
    sess = requests.Session()
    response = sess.get(url)
    content = json.loads(response.content.decode('utf-8'))
    return JsonResponse(data=content, safe=False, status=200)
