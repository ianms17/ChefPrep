from django.shortcuts import render, HttpResponseRedirect
from .charts import ingredientsChart, nutrientsChart
from .api import spoonacularPriceBreakdown, spoonacularRecipeInfo
from pychartjs import Color


from . import message
# from twilio.rest import Client 

# account_sid = "AC4157c6a3350d28f5f501fd02e64e496b" #Anh account sid
# auth_token = "6621fa871edb37a1f26494d6f383d33e" #Anh account token

# Create your views here.
from .forms import EventForm
from .models import FavoriteRecipes

# Create your views here.
def recipe(request, recipe_id):
    form = EventForm()

    results = spoonacularRecipeInfo(recipe_id).json()
    results['nutrition']['nutrients'] = results['nutrition']['nutrients'][:8]
    results_prices = spoonacularPriceBreakdown(recipe_id).json()
    results['pricePerServing'] = str(int(results_prices['totalCost']) / 100)

    for i in results['extendedIngredients']:
        i['amount'] = str(round(float(i['amount']), 1))
    

    ingredients_Chart = ingredientsChart()
    labels_i = []
    prices = []
    for ingredient in results_prices['ingredients']:
        labels_i.append(ingredient['name'])
        prices.append(str(int(ingredient['price']) / 100))
    ingredients_Chart.data.data = prices
    ingredients_Chart.labels.grouped = labels_i
    ingredients_Chart.data.backgroundColor = Color.Palette(Color.Hex('#34cfeb'), n=len(prices), generator='lightness')
    ingredients_Chart_get = ingredients_Chart.get()

    nutrients_Chart = nutrientsChart()
    labels_n = []
    percentage = []
    for nutrient in results['nutrition']['nutrients']:
        labels_n.append(nutrient['title'])
        percentage.append(nutrient['percentOfDailyNeeds'])
    nutrients_Chart.data.data = percentage
    nutrients_Chart.data.label = "Percentage of Daily Needs"
    nutrients_Chart.labels.grouped = labels_n
    nutrients_Chart.data.backgroundColor = Color.Palette(Color.Hex('#34cfeb'), n=len(percentage), generator='lightness')
    nutrients_Chart_get = nutrients_Chart.get()


    if request.method == 'POST':
        if 'Favorite' in request.POST:
            form_results = dict(request.POST)
            print('recipe id:', form_results['recipe_id'][0])
            print('recipe name:', form_results['recipe_name'][0])
            print('user:', request.user)
            print('user id:', request.user.id)

            save_recipe = FavoriteRecipes(
                user_id=int(request.user.id), 
                recipe_name=form_results['recipe_name'][0], 
                recipe_link='chefprep.pythonanywhere.com/recipe/'+form_results['recipe_id'][0]+'/', 
                recipe_id=int(form_results['recipe_id'][0])
            )
            save_recipe.save()
        elif 'Sendmsg' in request.POST:
            # print("https://chefprep.pythonanywhere.com"+request.path)
            message.send_message("9794221082","This is the current text XXXXX \n https://chefprep.pythonanywhere.com"+request.path)
            print("Message")

    context = {
        'results': results,
        'ingredients_Chart_get': ingredients_Chart_get,
        'nutrients_Chart_get': nutrients_Chart_get,
        'form': form,
    }
    return render(request, 'recipe.html', context)

