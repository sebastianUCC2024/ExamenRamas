from django.shortcuts import render


def hoja_vida(request):
    return render(request, "HojaVidaCarlos/hoja_vida.html")
