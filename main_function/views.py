from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Additive_list
import requests
import urllib.request
import json
from .SortingAlgo import ingredient_sort

class Search(TemplateView): 
    # url = 'https://api.barcodelookup.com/v2/products?barcode=072250011372&formatted=y&key=' + "ax4xj589yc5wpquahyp749dkfi4jhm"
    # # response = requests.get(url)
    # with urllib.request.urlopen(url) as url:
    #     data = json.loads(url.read().decode())
    # ingredients = ingredient_sort(data)
    template_name = 'main_function/search.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # url = 'https://api.barcodelookup.com/v2/products?barcode=072250011372&formatted=y&key=' + "ax4xj589yc5wpquahyp749dkfi4jhm"
        # with urllib.request.urlopen(url) as url:
        #     data = json.loads(url.read().decode())
        # returned_context = ingredient_sort(data)
        # ingredients = returned_context[0]
        ingredient_list_models = []
        ingredients = ['High Fructose Corn Syrup', 'Soybean Oil', 'Unbleached Enriched Flour']
        if ingredients:
            for ingredient in ingredients:
                if Additive_list.objects.filter(name__icontains=ingredient):
                    ingredient_ = Additive_list.objects.filter(name__icontains=ingredient).get()
                    ingredient_list_models.append(ingredient_)
        context['ingredient_list_model'] = ingredient_list_models
        context['image'] = 'https://images.barcodelookup.com/2755/27556319-1.jpg'
        context['product_name'] = 'Cuisine Camino Organic Cocoa Powder'
        print(context)
        return context

# Create your views here.
