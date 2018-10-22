from django import forms
from .models import User

class TheForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'currentBal','emergency','date','name'}
