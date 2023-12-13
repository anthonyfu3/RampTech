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
        
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if field not in self.data:
                cleaned_data.pop(field, None)
        return cleaned_data    
    
        
class EditAircraftNoteForm(forms.ModelForm):
    class Meta:
        model = AircraftNote
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditAircraftNoteForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False