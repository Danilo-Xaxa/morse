from django import forms


class TraduzirMorse(forms.Form):
    morse = forms.CharField(label="morse", max_length=500)
    
class TraduzirTexto(forms.Form):
    texto = forms.CharField(label="texto", max_length=500)
    