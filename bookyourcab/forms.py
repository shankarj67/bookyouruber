from django import forms


class BookUberForm(forms.Form):
    source = forms.CharField(required=True)
    destination = forms.CharField(required=True)
    time = forms.TimeField(required=True)
    email = forms.CharField(required=True)
    
    