from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from aircraft.models import AircraftNote
from .forms import AircraftNoteForm
from .models import AircraftNote  
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def aircraft_note_create(request):
    if request.method == 'POST':
        form = AircraftNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect after POST
    else:
        form = AircraftNoteForm()  # An unbound form

    return render(request, 'your_template.html', {'form': form})

def aircraft_note_list(request):
    notes = AircraftNote.objects.all()
    return render(request, 'your_list_template.html', {'notes': notes})


def add_data(request):
    if request.method == 'POST':
        form = AircraftNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'invalid form', 'errors': form.errors})

    form = AircraftNoteForm()  # An unbound form for GET request
    return render(request, 'index.html', {'form': form})

def unit1_notes_table(request):
    notes = AircraftNote.objects.all()
    return render(request, 'unit1table.html', {'notes': notes})

@require_POST
@csrf_exempt
def edit_note(request, note_id):
    note = get_object_or_404(AircraftNote, pk=note_id)
    form = AircraftNoteForm(request.POST, instance=note)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        print(form.errors)  # Add this line to log form errors
        return JsonResponse({'status': 'error', 'errors': form.errors})

@require_POST
def delete_note(request, note_id):
    note = get_object_or_404(AircraftNote, pk=note_id)
    note.delete()
    return JsonResponse({'status': 'success'})

