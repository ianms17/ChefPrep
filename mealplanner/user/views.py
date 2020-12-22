from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.contrib.auth.models import User


from .forms import UserInfoForm

from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe

from .forms import UserInfoForm, clearForm, deleteForm
from .calendar import Calendar, prev_month, next_month, get_date
from recipe.models import FavoriteRecipes

from allauth.socialaccount.models import SocialToken, SocialApp
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import pprint
from datetime import datetime as dt

# Create your views here.
def settings(request):
    return render(request, 'settings.html')


# create profile page with area to fill in pertinent information
def profile(request):
    try:
        user = User.objects.get(pk=request.user.id)
        prof = UserProfile.objects.get(user=user)
        form = UserInfoForm(initial={
                    'weight': prof.weight,
                    'feet': prof.feet,
                    'inches': prof.inches,
                    'age': prof.age,
                    'goal': prof.goal,
                    'location': prof.location,
                    'phone_number': prof.phone_number
                    })
    except UserProfile.DoesNotExist:
        form = UserInfoForm()
    form_delete = deleteForm()
    if request.method == 'POST':
        if 'Settings' in request.POST:
            form = UserInfoForm(request.POST)
            if form.is_valid():
                age = form.cleaned_data['age']
                weight = form.cleaned_data['weight']
                feet = form.cleaned_data['feet']
                inches = form.cleaned_data['inches']
                goal = form.cleaned_data['goal']
                location = form.cleaned_data['location']
                phone_number = form.cleaned_data['phone_number']
                colorblind = form.cleaned_data['enable_colorblind']
                
                # add user information to database
                update_profile(request, request.user.id, age, weight, feet, inches, goal, location, phone_number, colorblind)

                # redirect back to profile page
                return HttpResponseRedirect('/user/profile/')
            else:
                form = UserInfoForm()
        if 'Delete Recipe' in request.POST:
            form_delete = deleteForm(request.POST)
            if form_delete.is_valid():
                delete_id = form_delete.cleaned_data['delete_id']
                FavoriteRecipes.objects.filter(recipe_id=delete_id).delete()
                print('deleted?')



    favorite_recipes = FavoriteRecipes.objects.all().filter(user_id=request.user.id)
    recipes = []
    for i in favorite_recipes:
        recipes.append({
            'recipe_name': i.recipe_name,
            'recipe_link': i.recipe_link,
            'recipe_id': i.recipe_id,
        })
    
    context = {
        'form': form,
        'recipes': recipes,
        'form_delete': form_delete,
    }

    return render(request, 'profile.html', context)


def update_profile(request, user_id, age, weight, feet, inches, goal, location, phone_number, colorblind):
    # get the user object associated with the request that was passed
    user = User.objects.get(pk=user_id)

    userprofile, created = UserProfile.objects.update_or_create(
        user=user,
        defaults={
            # 'user_id': user_id,
            'age': age,
            'weight': weight,
            'feet': feet,
            'inches': inches,
            'goal': goal,
            'location': location,
            'phone_number': phone_number,
            'colorblind': colorblind,
        }
    )



def calendar(request):
    # put this into separate function for readability
    print('Grabbing Token: ')
    token = SocialToken.objects.get(account__user=request.user, account__provider='google')
    # pprint.pprint(token.__dict__)
    print('------------------------------------------')

    print('Generating Credentials: ')
    credentials = Credentials(
        token=token.token,
        refresh_token=token.token_secret,
        token_uri='https://oauth2.googleapis.com/token',
        client_id='47225582993-qvnoin5oo862cb8qqvahlhfghvff7k2k.apps.googleusercontent.com',
        client_secret='T0xYNrd864NbFWE5w4GjOihf')
    # pprint.pprint(credentials.__dict__)
    print('------------------------------------------')

    print('Building Calendar Service: ')
    service = build('calendar', 'v3', credentials=credentials)
    # pprint.pprint(service.__dict__)  DON'T DO THIS, SO MUCH STUFF
    print('------------------------------------------')

    print('Logic to create new calendar for ChefPrep if not already there: ')
    calendars_results = service.calendarList().list().execute()
    chefPrepCalendar = next((i for i in calendars_results['items'] if i['summary'] == 'ChefPrep'), None)
    if chefPrepCalendar == None: 
        # implement logic to create calendar
        print('Calendar not found!, creating new calendar for ChefPrep: ')
        user_timezone = service.settings().get(setting='timezone').execute()
        new_calendar_settings = {'summary': 'ChefPrep', 'timeZone': user_timezone}
        chefPrepCalendar = service.calendars().insert(body=new_calendar_settings).execute()
        print('Calendar created: ')
    else:
        print('Calendar found!')
    pprint.pprint(chefPrepCalendar)
    print('------------------------------------------')

    print('If post request from recipe page, add to events before getting it')
    clear_form = clearForm()
    if request.method == 'POST' and 'Add to Calendar' in request.POST:
        form_results = dict(request.POST)
        print(form_results)
        new_event = {
            'summary': 'ChefPrep: ' + form_results['recipe_name'][0],
            'description': 'http://chefprep.pythonanywhere.com/recipe/' + form_results['recipe_id'][0] + '/',
            'end': {
                'date': form_results['event_date'][0]
            },
            'start': {
                'date': form_results['event_date'][0]
            }
        }
        service.events().insert(calendarId=chefPrepCalendar['id'], body=new_event).execute()
    print('------------------------------------------')

    print('Getting list of events from ChefPrep calendar: ')
    events_results = service.events().list(calendarId=chefPrepCalendar['id']).execute()
    pprint.pprint(events_results['items'])
    if request.method == 'POST' and 'Clear Date' in request.POST:
        form_results = dict(request.POST)
        clear_date = form_results['clear_date'][0]
        print(clear_date)
        for i in events_results['items']:
            print(i['end']['date'])
            if i['end']['date'] == clear_date:
                print('removing?')
                service.events().delete(calendarId=chefPrepCalendar['id'], eventId=i['id']).execute()
        events_results = service.events().list(calendarId=chefPrepCalendar['id']).execute()

    print('------------------------------------------')

    print('Formatting events for calendar class: ')
    formatted_events = [{'title': i['summary'], 'description': i['description'], 'date': i['end']['date']} for i in events_results['items']]
    pprint.pprint(formatted_events)
    print('------------------------------------------')

    print('Creating calendar representation and passing it in as context: ')
    curr_date = get_date(request.GET.get('month', None))
    cal = Calendar(curr_date.year, curr_date.month, formatted_events)
    html_cal = cal.displayMonth()
    html_cal = mark_safe(html_cal)

    context = {
        'google_calendar': html_cal,
        'prev_month': prev_month(curr_date),
        'next_month': next_month(curr_date),
        'clear_form': clear_form,
    }
    return render(request, 'calendar.html', context)




