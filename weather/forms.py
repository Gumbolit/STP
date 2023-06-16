from .models import City
from .models import UserEvent
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


class UserEventForm(ModelForm):
    class MetaUserEvent:
        model = UserEvent
        fields = ["title", "time"]
        widget = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "time": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите время'
            })
        },
