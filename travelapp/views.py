from django.shortcuts import render
from django.http import HttpResponse

from travelapp.models import Team


# from . models import Team
# Create your views here.
def demo(request):
    obj=Team.objects.all()
    return render(request,'index.html',{'result':obj})