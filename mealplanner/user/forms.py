from django import forms
from .models import UserProfile
from .models import User


# form to get user information
class UserInfoForm(forms.Form):
    # get user weight, height, age, ask for goal and location
    weight = forms.IntegerField(label='Weight')
    feet = forms.IntegerField(label='Feet')
    inches = forms.IntegerField(label='Inches')
    age = forms.IntegerField(label='Age')
    goal = forms.CharField(label='Goal', widget=forms.Textarea)
    location = forms.CharField(label='Location', max_length=100)
    phone_number = forms.CharField(label='Phone Number', help_text='Enter phone number without dashes')
    enable_colorblind = forms.ChoiceField(label="Enable Colorblind Mode",
                                          widget=forms.RadioSelect,
                                          choices=[(True, 'True'),
                                                   (False, 'False')]
                                          )


class clearForm(forms.Form):
    clear_date = forms.DateField()

class deleteForm(forms.Form):
    delete_id = forms.IntegerField()


