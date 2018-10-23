from django import forms
from .models import User
from .models import Withdaraw
from .models import Deposit


class TheForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'currentBal','emergency','date','name'}



class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Withdaraw
        fields = {'amount','date','name'}


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = {'amount','date','name'}