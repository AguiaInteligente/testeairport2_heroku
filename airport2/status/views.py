from django.shortcuts import render
# from .models import smarteagle

def leituraView(request):
    #\\leitura_completa = smarteagle.objects.all()
   # tudo = {'all_items': leitura_completa}
    return render(request,'todo.html')