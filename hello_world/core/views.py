from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aircraft.models import AircraftNote
from aircraft import views

@login_required
def index(request):
    context = {
        "title": "Django example",
    }
    notes = AircraftNote.objects.all()
    return render(request, 'index.html', {'notes': notes})

   