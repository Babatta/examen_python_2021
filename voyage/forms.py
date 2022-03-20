from django.forms import ModelForm
from pip._internal.cli.cmdoptions import list_exclude

from .models import Voyage

class VoyageForm(ModelForm):
    class Meta:
        model=Voyage
        fields='__all__'
class VoyagesForm(ModelForm):
    class Meta:
        model = Voyage
        fields = '__all__'


