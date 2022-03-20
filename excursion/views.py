from django.shortcuts import render
from django.http import HttpResponse
from destination.models import Destination
from excursion.models import Excursion
from voyage.models import Voyage


# Create your views here.
def Liste_excursion(request,pk):
    excur = Excursion.objects.get(id=pk)
    voyagesex = Voyage.objects.filter(excursion=pk)
    #destinations = Destination.objects.all()
    excursions = Excursion.objects.all()
    context = {'excursions': excursions, 'voyages': voyagesex,'excur':excur}
    return render(request,'excursion/list_excursion.html',context)