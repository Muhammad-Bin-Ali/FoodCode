from .models import Additive_list

def ingredient_sort(data):
    harmfulIngredients = []
    data_ingredients = data['products'][0]['ingredients']
    characters = ['(', ')', "  "]
    for character in characters:
        data_ingredients = data_ingredients.replace(character,", ")
    data_ingredients = [str(g) for g in data_ingredients.split(', ')]
    for ingredient in data_ingredients:
        if ingredient == '':
            data_ingredients.remove(ingredient)
        print(ingredient)

        if ingredient[-1] == ' ':
            data_ingredients.remove(ingredient)
            ingredient = ingredient.replace(' ', '')
            data_ingredients.append(ingredient)
    print(data_ingredients)
    #if data['products'][0]['nutrition_facts']:data_nutrition = data['products'][0]['nutrition_facts']
    LofList = len(data_ingredients)
    i = 0
    while LofList > i:
        if Additive_list.objects.filter(name__icontains = data_ingredients[i]):
            harmfulIngredients.append(data_ingredients[i]) 
            i = i+1
        else:
            i = i+1
    return harmfulIngredients
                