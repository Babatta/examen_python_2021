from django.shortcuts import render
from django.http import HttpResponse
from destination.models import Destination
from excursion.models import Excursion
from voyage.models import Voyage
# Create your views here.
def Liste_destination(request,pk):
    destination = Destination.objects.get(id=pk)
    voyages = Voyage.objects.filter(id_destination=pk)
    destinations = Destination.objects.all()
    excursions = Excursion.objects.all()
   #corresponds = Correspond.objects.all()
    context = {'destinations': destinations, 'excursions': excursions, 'voyages': voyages,'destination':destination,}
    return render(request, 'destination/list_destination.html',context)