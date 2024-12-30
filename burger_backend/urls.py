from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
# from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('menu.urls')),  # Include your menu app URLs
    #  path('make_messages/', views.make_messages, name='make_messages'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development

# Add i18n patterns for language switching
urlpatterns += i18n_patterns(
    # You can include other URLs that need internationalization
)

# Ensure set_language URL is available
urlpatterns += [
    re_path(r'^i18n/', include('django.conf.urls.i18n')),  # This includes set_language view
]
