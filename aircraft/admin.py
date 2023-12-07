from django.contrib import admin
from .models import AircraftNote

@admin.register(AircraftNote)
class AircraftNoteAdmin(admin.ModelAdmin):
    list_display = ('tail_number', 'status', 'location', 'aircraft_model', 'service_time')  # Fields to display in the list view
    list_filter = ('status', 'location')  # Fields to filter by in the admin
    search_fields = ('tail_number', 'aircraft_model')  # Fields to search by in the admin
    ordering = ('service_time',)  # Default ordering
    date_hierarchy = 'service_time'  # Navigate through dates
    # Further customization as needed