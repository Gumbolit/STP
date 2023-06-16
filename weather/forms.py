from .models import City
from django.forms import ModelForm, TextInput


class CitiForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'from-control',
                                            'name': 'city',
                                            'id': 'city',
                                            'placeholder': 'Введите город'
                                            })}
