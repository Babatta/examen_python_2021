from django.shortcuts import render, HttpResponse,redirect
from destination.models import Destination
from excursion.models import Excursion
from voyage.models import Voyage
from .forms import VoyageForm, VoyagesForm


# Create your views here.

def home(request):
    voyages = Voyage.objects.all()
    destinations = Destination.objects.all()
    excursions = Excursion.objects.all()
    context={'destinations':destinations,'excursions':excursions,'voyages':voyages}
    return render(request,'voyage/accueil.html',context)
def index_voyage(request,pk):
    voyage=Voyage.objects.get(id=pk)
    excursions = voyage.excursion_set.all()
    # destina = Destination.objects.filter(id=pk)
    #excursions = Excursion.objects.all()
    context={'voyage':voyage,'excursions': excursions}
    return render(request,'voyage/indexvoyage.html',context)
def modifier_voyage(request,pk):
    voyage = Voyage.objects.get(id=pk)
    form=VoyageForm(instance=voyage)
    if request.method=='POST':
        form=VoyageForm(request.POST,instance=voyage)
        if form.is_valid():
            form.save()
            return redirect('/')


    excursions = voyage.excursion_set.all()
    context = {'voyage': voyage, 'excursions': excursions,'form':form}
    return render(request, 'voyage/modifier_voyage.html', context)
def supprimer_voyage(request,pk):
    voyage = Voyage.objects.get(id=pk)
    if request.method=='POST':
      voyage.delete()
      return redirect('/')
    context = {'item': voyage}
    return render(request, 'voyage/supprimer_voyage.html',context)
def add_voyage(request,pk):
    voyages = Voyage.objects.all()
    destination = Destination.objects.get(id=pk)
    print(destination)
    if request.method == 'POST':
        form = VoyagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.photo = form.cleaned_data['photo']
            form = VoyagesForm(request.POST,request.FILES).save()
        return redirect('/')
    else:
        print("------------------pas bon----------------------")
        form = VoyagesForm()
    context = {'destination': destination,'voyages':voyages,'form': form}
    return render(request, 'voyage/ajouter_voyage.html', context)
