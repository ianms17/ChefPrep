from django.shortcuts import render
from .forms import queryForm, ingredientsForm, nutrientsForm, complexForm
from .api import spoonacularBasicSearch, spoonacularIngredientsSearch, spoonacularNutrientsSearch, spoonacularComplexSearch


# Create your views here.
def search(request):
    query_Form = queryForm()
    ingredients_Form = ingredientsForm()
    nutrients_Form = nutrientsForm()
    complex_Form = complexForm()
    results = []
    display = 'Query'

    if request.method == 'POST':
        if 'Query' in request.POST:
            query_Form = queryForm(request.POST)
            if query_Form.is_valid():
                response = spoonacularBasicSearch(query_Form.cleaned_data['query']).json()
                results = response['results']
                for i in results: i['image'] = response['baseUri'] + i['image']
            display = 'Query'

        elif 'Ingredients' in request.POST:
            ingredients_Form = ingredientsForm(request.POST)
            if ingredients_Form.is_valid():
                response = spoonacularIngredientsSearch(ingredients_Form.cleaned_data['ingredients']).json()
                results = response
            display = 'Ingredients'

        elif 'Nutrients' in request.POST:
            nutrients_Form = nutrientsForm(request.POST)
            if nutrients_Form.is_valid():
                nutrientParams = nutrients_Form.cleaned_data
                response = spoonacularNutrientsSearch(
                    nutrientParams['caloriesmax'],
                    nutrientParams['proteinmax'],
                    nutrientParams['carbsmax'],
                    nutrientParams['fatmax'],
                    nutrientParams['caloriesmin'],
                    nutrientParams['proteinmin'],
                    nutrientParams['carbsmin'],
                    nutrientParams['fatmin'],
                ).json()
                results = response
            display = 'Nutrients'

        elif 'Complex' in request.POST:
            complex_Form = complexForm(request.POST)
            if complex_Form.is_valid():
                complexParams = complex_Form.cleaned_data
                response = spoonacularComplexSearch(
                    complexParams['caloriesmax'],
                    complexParams['proteinmax'],
                    complexParams['carbsmax'],
                    complexParams['fatmax'],
                    complexParams['caloriesmin'],
                    complexParams['proteinmin'],
                    complexParams['carbsmin'],
                    complexParams['fatmin'],

                    complexParams['query'],
                    complexParams['ingredients'],

                    complexParams['cuisine'],
                    complexParams['diet'],
                    complexParams['intolerances'],
                ).json()
                results = response['results']
                print(results)
            display = 'Complex'
    context = {
        'query_Form': query_Form,
        'ingredients_Form': ingredients_Form,
        'nutrients_Form': nutrients_Form,
        'complex_Form': complex_Form,
        'results': results,
        'display': display
    }
    return render(request, 'search.html', context)

