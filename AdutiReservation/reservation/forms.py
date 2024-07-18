from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError

def validate_contact(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Le contact doit contenir exactement 10 chiffres.')

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nom', 'prenom', 'contact', 'annee_sortie', 'diner_precedent']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'block w-full p-0.75 border border-gray-300 rounded mb-4'}),
            'prenom': forms.TextInput(attrs={'class': 'block w-full p-0.75 border border-gray-300 rounded mb-4'}),
            'contact': forms.TextInput(attrs={'class': 'block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6', 'placeholder':"0585987652"}),
            'annee_sortie': forms.DateInput(attrs={'type': 'date', 'class': 'block w-full p-0.75 border border-gray-300 rounded mb-4'}),
            'diner_precedent': forms.Select(attrs={'class': 'block w-full p-0.75 border border-gray-300 rounded mb-4'}),
        }

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        validate_contact(contact)
        return contact

