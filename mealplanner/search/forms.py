from django import forms

class queryForm(forms.Form):
    query = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class' : 'query'}))

class ingredientsForm(forms.Form):
    ingredients = forms.CharField(max_length=300, label='', widget=forms.TextInput(attrs={'class' : 'ingredients'}))

class nutrientsForm(forms.Form):
    caloriesmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Calories Max', 'class' : 'nutrientsTop'}))
    proteinmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Protein Max', 'class' : 'nutrientsTop'}))
    carbsmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Carbs Max', 'class' : 'nutrientsTop'}))
    fatmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Fat Max', 'class' : 'nutrientsTop'}))
    caloriesmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Calories Min', 'class' : 'nutrientsBottom'}))
    proteinmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Protein Min', 'class' : 'nutrientsBottom'}))
    carbsmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Carbs Min', 'class' : 'nutrientsBottom'}))
    fatmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Fat Min', 'class' : 'nutrientsBottom'}))

class complexForm(forms.Form):
    caloriesmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Calories Max', 'class' : 'nutrientsTop'}))
    proteinmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Protein Max', 'class' : 'nutrientsTop'}))
    carbsmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Carbs Max', 'class' : 'nutrientsTop'}))
    fatmax = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Fat Max', 'class' : 'nutrientsTop'}))
    caloriesmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Calories Min', 'class' : 'nutrientsBottom'}))
    proteinmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Protein Min', 'class' : 'nutrientsBottom'}))
    carbsmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Carbs Min', 'class' : 'nutrientsBottom'}))
    fatmin = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Fat Min', 'class' : 'nutrientsBottom'}))

    query = forms.CharField(required=False, max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Query', 'class' : 'query'}))
    ingredients = forms.CharField(required=False, max_length=300, label='', widget=forms.TextInput(attrs={'placeholder': 'Ingredients', 'class' : 'ingredients'}))

    cuisine = forms.CharField(required=False, max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Cuisine', 'class' : 'cuisine'}))
    diet = forms.CharField(required=False, max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Diets', 'class' : 'diet'}))
    intolerances = forms.CharField(required=False, max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Intolerances', 'class' : 'intolerances'}))