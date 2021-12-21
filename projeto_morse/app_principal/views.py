from django.shortcuts import render
from .forms import Traduzir
from .models import Traducao
from .utilidades.tradutor import Tradutor as t

# Create your views here.
def index(request):
    if request.method == "POST":
        if not request.POST.get("morse").strip():
            return render(request, 'app_principal/index.html', {'form': Traduzir(), 'texto': 'Digite algo para traduzir'})

        form = Traduzir(request.POST or None)

        if form.is_valid():
            morse = form.cleaned_data["morse"]
            try:
                texto = t.decriptar(morse)
            except KeyError:
                return render(request, 'app_principal/index.html', {'form': Traduzir(), 'texto': 'Digite um código morse válido'})
            traducao = Traducao(morse=morse, texto=texto)
            traducao.save()
            return render(request, 'app_principal/index.html', {'form': form, 'texto': texto})
        else:
            return render(request, 'app_principal/index.html', {'form': form, 'texto': 'Erro no formulário'})

    else:
        return render(request, 'app_principal/index.html', {'form': Traduzir()})
