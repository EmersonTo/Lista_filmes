from django.shortcuts import render
from .models import NomeFilme
# Create your views here.


def homepage(request):
    return render(
        request=request,
        template_name="home.html",
        context={"filmes": NomeFilme.objects.all}
    )
