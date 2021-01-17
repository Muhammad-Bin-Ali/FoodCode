# from .models import Additive_list

#ingredient_list = "['Unbleached Enriched Flour (wheat Flour', 'Malted Barley Flour', 'Niacin', 'Reduced Iron', 'Thiamin Mononitrate', 'Riboflavin', 'Folic Acid)', 'Water', 'High Fructose Corn Syrup', 'Yeast', 'Contains 2% Or Less Of The Each Of The Following: Calcium Carbonate', 'Soybean Oil', 'Wheat Gluten', 'Salt', 'Dough Conditioners (contains One Or More Of The Following: Sodium Stearoyl Lactylate', 'Calcium Stearoyl Lactylate', 'Monoglycerides', 'Mono- And Diglycerides', 'Distilled Monoglycerides', 'Calcium Peroxide', 'Calcium Iodate', 'Datem', 'Ethoxylated Mono- And Diglycerides', 'Enzymes', 'Ascorbic Acid)', 'Vinegar', 'Monocalcium Phosphate', 'Yeast Extract', 'Modified Corn Starch', 'Sucrose', 'Sugar', 'Soy Lecithin', 'Cholecalciferol (vitamin D3)', 'Soy Flour', 'Ammonium Sulfate', 'Calcium Sulfate', 'Calcium Propionate (to Retard Spoilage).']"
#toxic = ['Unbleached Enriched Flour', 'High Fructose Corn Syrup', 'Soybean Oil']
import http.client
import mimetypes
import json

def ingredient_sort(data):
    harmfulIngredients = []
    EmptyListList = [""]
    data_ingredients = data['products'][0]['ingredients']
    product_name = data['products'][0]['product_name']
    image_url = data['products'][0]['images']
    EmptyList = ""
    if data_ingredients == EmptyList:
        harmfulIngredients.append(EmptyListList)
        return False
    characters = ['(', ')']
    for character in characters:
        data_ingredients = data_ingredients.replace(character,"")
    data_ingredients = [str(g) for g in data_ingredients.split(',')]
    LofList = len(data_ingredients)
    i = 0
    while LofList > i:
        if Additive_list.objects.filter(name__icontains = data_ingredients[i]):
            harmfulIngredients.append(data_ingredients[i]) 
            i = i+1
        else:
            i = i+1
    temp_list = [harmfulIngredients, product_name, image_url]
    return temp_list

def ingredients_api(barcode):
    conn = http.client.HTTPSConnection("world.openfoodfacts.org")
    payload = ''
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    conn.request("GET", "/api/v0/product_name/5413548283128.json?fields=ingredients_text_en", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)
    for key in json_obj:
        if (key == 'product'):
            ingredients = json_obj['product']
    
    conn.request("GET", "/api/v0/product_name/5413548283128.json?fields=product_name", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)
    for key in json_obj:
        if (key == 'product'):
            productname = json_obj['product']

    conn.request("GET", "/api/v0/product_name/5413548283128.json?fields=image_url", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    json_obj = json.loads(data)
    for key in json_obj:
        if (key == 'product'):
            imageurl = json_obj['product']
    

    

    

def ingredient_sort_local(data):
    harmfulIngredients = []
    EmptyListList = [""]
    data_ingredients = data['products'][0]['ingredients']
    product_name = data['products'][0]['product_name']
    image_url = data['products'][0]['images']
    EmptyList = ""
    if data_ingredients == EmptyList:
        harmfulIngredients.append(EmptyListList)
        return False
    characters = ['(', ')']
    for character in characters:
        data_ingredients = data_ingredients.replace(character,"")
    data_ingredients = [str(g) for g in data_ingredients.split(',')]
    LofList = len(data_ingredients)
    i = 0
    while LofList > i:
        if data_ingredients[i] in toxic:
            harmfulIngredients.append(data_ingredients[i]) 
            i = i+1
        else:
            i = i+1
    temp_list = [harmfulIngredients, product_name, image_url]
    return temp_list
      
if __name__ == '__main__':
    ingredient_sort_local(ingredient_list)