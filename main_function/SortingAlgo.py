from .models import Additive_list

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
    characters = ['(', ')', "  "]
    for character in characters:
        data_ingredients = data_ingredients.replace(character,", ")
    data_ingredients = [str(g) for g in data_ingredients.split(', ')]
    
    data_ingredients = [x for x in data_ingredients if x]
    for ingredient in data_ingredients:
        if ingredient[-1] == ' ' or ingredient[-1] == '  ':
            data_ingredients.remove(ingredient)
            ingredient = ingredient[:-1]
            data_ingredients.append(ingredient)
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
                