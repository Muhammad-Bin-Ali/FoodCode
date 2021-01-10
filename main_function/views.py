from django.shortcuts import render
from django.views.generic import View
import requests
import urllib.request
import json

class Search(View):
    template_name = 'main_function/search.html'
    url = 'https://api.barcodelookup.com/v2/products?barcode=072250011372&formatted=y&key=' + "jmxudd59y0evlndm0o0rwq6h2dmmzr"
    response = requests.get(url)

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        print(data)


# Create your views here.
