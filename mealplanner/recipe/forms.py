from django import forms

class EventForm(forms.Form):
    event_date = forms.DateField()