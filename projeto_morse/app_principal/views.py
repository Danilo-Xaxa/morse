from django.shortcuts import render
from .forms import Traduzir
from .models import Traducao
from .utilidades.tradutor import Tradutor as t

# Create your views here.
def index(request):
    if request.method == "POST":
        form = Traduzir(request.POST or None)
        morse = request.POST.get("morse")
        texto = t.decriptar(morse)
        return render(request, 'app_principal/index.html', {'form': form, 'texto': texto})
    else:
        form = Traduzir()
        return render(request, 'app_principal/index.html', {'form': form})
