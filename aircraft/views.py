from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AircraftNote

def unit1_notes_view(request):
    notes = AircraftNote.objects.all()
    return render(request, 'unit1table.html', {'notes': notes})

def unit1_notes_table(request):
    notes = AircraftNote.objects.all()
    return render(request, 'unit1table.html', {'notes': notes})