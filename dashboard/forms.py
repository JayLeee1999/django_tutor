from django.forms import ModelForm

from dashboard.models import CountryData

class CountryDataForm(ModelForm):
    class Meta:
        model = CountryData
        fields = '__all__'