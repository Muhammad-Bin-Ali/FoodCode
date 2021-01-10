from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Additive_list
import requests
import urllib.request
import json
from .SortingAlgo import ingredient_sort

class Search(TemplateView): 
    template_name = 'main_function/search.html'
    # url_2 = 'https://api.spoonacular.com/food/ingredients/search'
    # headers = {
    #     'x-rapidapi-key': "c960144edbdc4b9e829ac4bbc47eea81",
    #     'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    #     }
    # query = 'Wonder'
    # response = requests.request("GET", url_2, headers=headers, params=query)


    # with urllib.request.urlopen(url_2) as url:
    #     data = json.loads(url.read().decode())
    #     print(data)
    
    url = 'https://api.barcodelookup.com/v2/products?barcode=072250011372&formatted=y&key=' + "7shrk8q51g3ppmj9cear54gu70r1lj"
    response = requests.get(url)

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    ingredients = ingredient_sort(data)
    print(ingredients)
# Create your views here.
