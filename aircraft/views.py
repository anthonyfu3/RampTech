from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from aircraft.models import AircraftNote
from .forms import AircraftNoteForm
from .models import AircraftNote  
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required
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

@login_required
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

@login_required
def unit1_notes_table(request):
    notes = AircraftNote.objects.all()
    context = {
        'notes': notes,
        'status_choices': AircraftNote.STATUS_CHOICES,
        'location_choices': AircraftNote.LOCATION_CHOICES,
        'fuel_format_choices': AircraftNote.FUEL_FORMAT_CHOICES,
        'fuel_type_choices': AircraftNote.FUEL_TYPE_CHOICES,
        'lav_status_choices': AircraftNote.LAV_STATUS_CHOICES,
        'lav_type_choices': AircraftNote.LAV_TYPE_CHOICES,
        'water_service_status_choices': AircraftNote.WATER_SERVICE_STATUS_CHOICES,
        'gpu_status_choices': AircraftNote.GPU_STATUS_CHOICES,
        'transportation_status_choices': AircraftNote.TRANSPORTATION_STATUS_CHOICES,
        'catering_status_choices': AircraftNote.CATERING_STATUS_CHOICES,
        'customer_type_choices': AircraftNote.CUSTOMER_TYPE_CHOICES,
        'oil_status_choices': AircraftNote.OIL_STATUS_CHOICES,
        'ladder_status_choices': AircraftNote.LADDER_STATUS_CHOICES,
        'vacuum_status_choices': AircraftNote.VACUUM_STATUS_CHOICES,
    }
    return render(request, 'unit1table.html', context)

@login_required
@require_POST
def edit_note(request, note_id):
    note = get_object_or_404(AircraftNote, pk=note_id)

    # Create a form instance with POST data, but don't bind it to the note instance yet
    form = AircraftNoteForm(request.POST)

    # Create a dictionary to hold updated data
    updated_data = {}

    # Loop through the form fields
    for field in form.fields:
        if field in request.POST and request.POST[field].strip():
            # Add only non-empty fields to the updated_data
            updated_data[field] = request.POST[field]

    # Now bind the form with updated_data and the note instance
    form = AircraftNoteForm(updated_data, instance=note)

    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})


@login_required
@require_POST
def delete_note(request, note_id):
    note = get_object_or_404(AircraftNote, pk=note_id)
    note.delete()
    return JsonResponse({'status': 'success'})

