import requests

def spoonacularBasicSearch(query):
    url = "https://rapidapi.p.rapidapi.com/recipes/search"

    querystring = {
        "query":query,
        "number":"10",
        "offset":0,
    }

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "e78f34030emsh3a4e27bc37c13c1p1a418djsn0c6d2efdb14e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def spoonacularIngredientsSearch(query):
    url = "https://rapidapi.p.rapidapi.com/recipes/findByIngredients"

    querystring = {
        "ingredients":query,
        "number":"10",
        "ranking":"1",
        "ignorePantry":"true"
    }

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "e78f34030emsh3a4e27bc37c13c1p1a418djsn0c6d2efdb14e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def spoonacularNutrientsSearch(caloriesmax, caloriesmin, proteinmax, proteinmin, carbsmax, carbsmin, fatmax, fatmin):
    url = "https://rapidapi.p.rapidapi.com/recipes/findByNutrients"

    querystring = {"number":"10"}
    if caloriesmax != '': querystring["maxCalories"] = caloriesmax
    if caloriesmin != '': querystring["minCalories"] = caloriesmin
    if proteinmax != '': querystring["maxProtein"] = proteinmax
    if proteinmin != '': querystring["minProtein"] = proteinmin
    if carbsmax != '': querystring["maxCarbs"] = carbsmax
    if carbsmin != '': querystring["minCarbs"] = carbsmin
    if fatmax != '': querystring["maxFat"] = fatmax
    if fatmin != '': querystring["minFat"] = fatmin

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "e78f34030emsh3a4e27bc37c13c1p1a418djsn0c6d2efdb14e"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def spoonacularComplexSearch(caloriesmax, caloriesmin, proteinmax, proteinmin, carbsmax, carbsmin, fatmax, fatmin, query, ingredients, cuisine, diet, intolerances):
    url = "https://rapidapi.p.rapidapi.com/recipes/searchComplex"

    querystring = {"number":"10", }
    if caloriesmax != '': querystring["maxCalories"] = caloriesmax
    if caloriesmin != '': querystring["minCalories"] = caloriesmin
    if proteinmax != '': querystring["maxProtein"] = proteinmax
    if proteinmin != '': querystring["minProtein"] = proteinmin
    if carbsmax != '': querystring["maxCarbs"] = carbsmax
    if carbsmin != '': querystring["minCarbs"] = carbsmin
    if fatmax != '': querystring["maxFat"] = fatmax
    if fatmin != '': querystring["minFat"] = fatmin
    if query != '': querystring["query"] = query
    if ingredients != '': querystring["ingredients"] = ingredients
    if cuisine != '': querystring["cuisine"] = cuisine
    if diet != '': querystring["diet"] = diet
    if intolerances != '': querystring["intolerances"] = intolerances

    headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "e78f34030emsh3a4e27bc37c13c1p1a418djsn0c6d2efdb14e"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response