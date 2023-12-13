from django.db import models
from django.utils import timezone

class AircraftNote(models.Model):
    STATUS_CHOICES = [
        ('incoming', 'Incoming'),
        ('departing', 'Departing'),
        ('quickturn', 'Quickturn'),
        ('off_ramp', 'Off-Ramp'),
        ('standby', 'Standby'),
        ('maintenance', 'Maintenance'),
        ('overnight', 'Overnight'),
    ]

    LOCATION_CHOICES = [
        ('hanger_1', 'H1'),
        ('hanger_2', 'H2'),
        ('hanger_3', 'H3'),
        ('hanger_4', 'H4'),
        ('row_1', 'R1'),
        ('row_2', 'R2'),
        ('row_3', 'R3'),
        ('row_4', 'R4'),
        ('row_5', 'R5'),
        ('row_6', 'R6'),        
        ('tie_down', 'T-D'),
        ('gama', 'Gama'),
        ('off_ramp', 'O-R'),
        ('customs', 'Cstm'),
        ('netjets', 'NJ'),
        
    ]

    FUEL_FORMAT_CHOICES = [
        ('lbs', 'lbs'),
        ('kgs', 'kgs'),
        ('gallons', 'gallons'),
    ]

    FUEL_TYPE_CHOICES = [
        ('jet_a_neg', 'Jet-'),
        ('jet_a_pos', 'Jet+'),
        ('avgas', 'Avgas'),
    ]

    LAV_STATUS_CHOICES = [
        ('none', 'None'),
        ('fwr', 'Fwr'),
        ('aft', 'Aft'),
        ('fwr_aft', 'Fwr & Aft'),
        ('completed', 'Completed'),
    ]

    LAV_TYPE_CHOICES = [
        ('full', 'Full'),
        ('dump', 'Dump'),
        ('rinse', 'Rinse'),
    ]

    WATER_SERVICE_STATUS_CHOICES = [
        ('none', 'None'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    GPU_STATUS_CHOICES = [
        ('none', 'None'),
        ('stage', 'Stage'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    Oil_STATUS_CHOICES = [
        ('none', 'None'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    CUSTOMER_TYPE_CHOICES = [
        ('none', 'None'),
        ('based_tenant', 'Based Tenant'),
        ('signature_silver', 'Signature Status Silver'),
        ('signature_gold', 'Signature Status Gold'),
        ('signature_platinum', 'Signature Status Platinum'),
    ]

    TRANSPORTATION_STATUS_CHOICES = [
        ('none', 'None'),
        ('personal', 'Personal'),
        ('driver', 'Driver'),
        ('rental', 'Rental'),
        ('self-park', 'Self-Park'),
        ('Ride Share', 'Ride Share'),
    ]
    
    CATERING_STATUS_CHOICES = [
        ('none', 'None'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    OIL_STATUS_CHOICES = [
        ('none', 'None'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    VACUUM_STATUS_CHOICES = [
        ('none', 'None'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    LADDER_STATUS_CHOICES = [
        ('none', 'None'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]



    tail_number = models.CharField(max_length=10 ,null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES ,null=True, blank=True)
    service_time = models.DateTimeField(verbose_name='Service Time' ,null=True, blank=True)
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES ,null=True, blank=True)
    aircraft_model = models.CharField(max_length=50 ,null=True, blank=True)
    eta = models.DateTimeField(verbose_name='Estimated Time of Arrival', null=True, blank=True)
    etd = models.DateTimeField(verbose_name='Estimated Time of Departure', null=True, blank=True)
    passenger_count = models.IntegerField(null=True, blank=True)
    fuel_qty = models.IntegerField(verbose_name='Fuel Quantity', null=True, blank=True)
    fuel_format = models.CharField(max_length=10, choices=FUEL_FORMAT_CHOICES, null=True, blank=True)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES, null=True, blank=True)
    lav_status = models.CharField(max_length=10, choices=LAV_STATUS_CHOICES, null=True, blank=True)
    lav_type = models.CharField(max_length=10, choices=LAV_TYPE_CHOICES, null=True, blank=True)
    lav_gallons = models.IntegerField(null=True, blank=True)
    water_service_status = models.CharField(max_length=10, choices=WATER_SERVICE_STATUS_CHOICES, null=True, blank=True)
    gpu_status = models.CharField(max_length=10, choices=GPU_STATUS_CHOICES, null=True, blank=True)
    transportation_status = models.CharField(max_length=10, choices=TRANSPORTATION_STATUS_CHOICES, null=True, blank=True)
    catering_status = models.CharField(max_length=10, choices=CATERING_STATUS_CHOICES, null=True, blank=True)
    catering_number = models.CharField(max_length=50, null=True, blank=True)
    pic = models.CharField(max_length=50, null=True, blank=True)  # PIC stands for Paper, Ice, Coffee
    customer_type = models.CharField(max_length=30, choices=CUSTOMER_TYPE_CHOICES, null=True, blank=True)
    oil_status = models.CharField(max_length=10, choices=OIL_STATUS_CHOICES, null=True, blank=True)
    oil_type = models.CharField(max_length=50, null=True, blank=True)
    oil_qty = models.IntegerField(null=True, blank=True)
    ladder_status = models.CharField(max_length=10, choices=LADDER_STATUS_CHOICES, null=True, blank=True)
    vacuum_status = models.CharField(max_length=10, choices=VACUUM_STATUS_CHOICES, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now ,null=True, blank=True)