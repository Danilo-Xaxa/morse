from django.shortcuts import render
from .forms import TraduzirMorse, TraduzirTexto
from .models import TraducaoMorse, TraducaoTexto
from .utilidades.tradutor import Tradutor as t

# Create your views here.
def morse_para_texto(request):
    if request.method == "POST":
        if not request.POST.get("morse").strip():
            return render(request, 'app_principal/morse_para_texto.html', {'form': TraduzirMorse(), 'msg': 'Digite algo para traduzir'})

        form = TraduzirMorse(request.POST or None)

        if form.is_valid():
            morse = form.cleaned_data["morse"]
            try:
                texto = t.decriptar(morse)
            except KeyError:
                return render(request, 'app_principal/morse_para_texto.html', {'form': TraduzirMorse(), 'msg': 'Digite um código morse válido'})
            traducao = TraducaoMorse(morse=morse, texto=texto)
            traducao.save()
            return render(request, 'app_principal/morse_para_texto.html', {'form': form, 'msg': texto})
        else:
            return render(request, 'app_principal/morse_para_texto.html', {'form': form, 'msg': 'Digite 500 caracteres ou menos'})

    else:
        return render(request, 'app_principal/morse_para_texto.html', {'form': TraduzirMorse()})


def texto_para_morse(request):
    if request.method == "POST":
        if not request.POST.get("texto").strip():
            print('lol haha')
            return render(request, 'app_principal/texto_para_morse.html', {'form': TraduzirTexto(), 'msg': 'Digite algo para traduzir'})

        form = TraduzirTexto(request.POST or None)

        if form.is_valid():
            texto = form.cleaned_data["texto"]
            try:
                morse = t.encriptar(texto)
            except KeyError:
                return render(request, 'app_principal/texto_para_morse.html', {'form': TraduzirTexto(), 'msg': 'Digite um texto válido'})
            traducao = TraducaoTexto(morse=morse, texto=texto)
            traducao.save()
            return render(request, 'app_principal/texto_para_morse.html', {'form': form, 'msg': morse, 'piscar_morse': True})
        else:
            return render(request, 'app_principal/texto_para_morse.html', {'form': form, 'msg': 'Digite 500 caracteres ou menos'})

    else:
        return render(request, 'app_principal/texto_para_morse.html', {'form': TraduzirTexto()})
