from django.shortcuts import render
from app2 import  models
# Create your views here.
def books(request):
    a=models.book.objects.all()
    return render(request,"index.html",{"xianshi":a})

