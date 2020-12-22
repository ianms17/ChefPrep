import requests

def spoonacularPriceBreakdown(id):

    url = "https://rapidapi.p.rapidapi.com/recipes/" + str(id) + "/priceBreakdownWidget.json"

    headers = {
        'x-rapidapi-key': "e78f34030emsh3a4e27bc37c13c1p1a418djsn0c6d2efdb14e",
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response


def spoonacularRecipeInfo(id):
    url = "https://rapidapi.p.rapidapi.com/recipes/" + str(id) + "/information?includeNutrition=true"
    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "e78f34030emsh3a4e27bc37c13c1p1a418djsn0c6d2efdb14e"
        }
    response = requests.request("GET", url, headers=headers)
    return response