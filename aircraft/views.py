from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AircraftNote
from .forms import AircraftNoteForm  # Import the form you created
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def aircraft_note_create(request):
    if request.method == 'POST':
        form = AircraftNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some-view-name')  # Redirect after POST
    else:
        form = AircraftNoteForm()  # An unbound form

    return render(request, 'your_template.html', {'form': form})

def aircraft_note_list(request):
    notes = AircraftNote.objects.all()
    return render(request, 'your_list_template.html', {'notes': notes})

@csrf_exempt
def add_data(request):
    if request.method == 'POST':
        form = AircraftNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'invalid form', 'errors': form.errors})

    form = AircraftNoteForm()  # An unbound form for GET request
    return render(request, 'add_aircraft_note.html', {'form': form})

def unit1_notes_view(request):
    notes = AircraftNote.objects.all()
    return render(request, 'unit1table.html', {'notes': notes})

def unit1_notes_table(request):
    notes = AircraftNote.objects.all()
    return render(request, 'unit1table.html', {'notes': notes})
