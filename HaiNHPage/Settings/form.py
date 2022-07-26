from django.forms import forms


class CommercialForm(forms.Form):
    first_text = forms.CharField(max_length=15)
    second_text = forms.CharField(max_length=50)
    thirst_text = forms.CharField(max_length=50)