from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView
from hello_world.core import views as core_views

urlpatterns = [
    # Redirect root URL to login
    path("", RedirectView.as_view(url='/login/', permanent=True), name='home'),

    # Protect the index view with login_required
    path("index/", login_required(core_views.index), name='index'),

    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
