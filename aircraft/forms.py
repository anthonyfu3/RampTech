from django import forms
from .models import AircraftNote

class AircraftNoteForm(forms.ModelForm):
    class Meta:
        model = AircraftNote
        fields = '__all__'  # Or list specific fields if you don't need all
        widgets = {
            'service_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'eta': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'etd': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            "created_at": forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }