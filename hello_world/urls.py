from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from aircraft import views
from hello_world.core import views as core_views
from aircraft.views import delete_note, edit_note, unit1_notes_table

urlpatterns = [
    # Redirect root URL to login
    path("", RedirectView.as_view(url='/login/', permanent=True), name='home'),
    path("index/", login_required(core_views.index), name='index'),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('unit1table/', unit1_notes_table, name='unit1notes_table'),
    path('add-data-url/', views.add_data, name='add_data'),
    path('add-aircraft-note/', views.aircraft_note_create, name='add_aircraft_note'),
    path('aircraft-notes/', views.aircraft_note_list, name='aircraft_notes'),
    path('edit-note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete-note/<int:note_id>/', delete_note, name='delete_note'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
