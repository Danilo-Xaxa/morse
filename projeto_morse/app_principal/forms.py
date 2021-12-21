from django import forms


class Traduzir(forms.Form):
    morse = forms.CharField(label="morse", max_length=500)
    