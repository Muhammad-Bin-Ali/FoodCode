from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Additive_list
import requests
import urllib.request
import json
from .SortingAlgo import ingredient_sort
from django.http import JsonResponse
from django.core import serializers

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
        ingredients = []
        if ingredients:
            for ingredient in ingredients:
                if Additive_list.objects.filter(name__icontains=ingredient):
                    ingredient_ = Additive_list.objects.filter(name__icontains=ingredient).all()
                    ingredient_list_models.append(ingredient_)
        context['ingredient_list_model'] = ingredient_list_models
        context['image'] = 'https://images.barcodelookup.com/2755/27556319-1.jpg'
        context['product_name'] = 'Cuisine Camino Organic Cocoa Powder'
        print(context)
        return context

class LandingPage(TemplateView):
    template_name = 'main_function/landing_page.html'
    
class Search_ajax(View):
    def post(self, request, *args, **kwargs):
        print(**kwargs)
        if request.is_ajax:
            barcode_number = request.POST.get('barcode')
            print(barcode_number)
            ingredient_list_models = [] 
            url = "https://world.openfoodfacts.org/api/v0/product/" + barcode_number  
            with urllib.request.urlopen(url) as url:
                data = json.loads(url.read().decode())
            # return_context = ingredient_sort(data)
            # ingredients = return_context[0]
            ingredients = ['High Fructose Corn Syrup', 'Soybean Oil','Enriched Flour']
            if ingredients:
                for ingredient in ingredients:
                    if Additive_list.objects.filter(name__icontains=ingredient):
                        ingredient_ = Additive_list.objects.filter(name__icontains=ingredient).all()
                        for ingredient1_ in ingredient_:
                            name = ingredient1_.name
                            description = ingredient1_.description
                            pk = ingredient1_.pk
                            ingredient_list_models.append((name, description, pk))
            
            # serialized_qs = serializers.serialize('json', ingredient_list_models)
            # data = {"queryset" : serialized_qs}
            # data = []
            # data.append({'ingredients': ingredient_list_models})
            # print(data)
            print(ingredient_list_models)
            return JsonResponse({'harmful_ingredients': ingredient_list_models, 'image_url': 'https://static.openfoodfacts.org/images/products/007/225/001/1372/front_en.10.200.jpg', 'product_name': 'Wonder, calcium fortified enriched bread, classic white', 'barcode': barcode_number}, status=200)
        print(False)
        return False


        



