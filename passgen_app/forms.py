
from random import choices
from django import forms
class Getinput(forms.Form):
    
    # Owner space = 
    range = forms.IntegerField()

    OPTIONS = (
        (1, "Upper Case Alphabet"),
        (2, "Small Case Alphabet"),
        (3, "Numbers"),
        (4, "Symbols"),
    )
    Choices = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          choices=OPTIONS)
