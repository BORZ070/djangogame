from django import forms

from tbot.models import SupportQ


class SupportQForm(forms.ModelForm):
    class Meta:
        model = SupportQ
        fields = ['email','question']

