"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from web_project.views import SystemView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard urls
    path("", include("apps.dashboards.urls")),

    # layouts urls
    path("", include("apps.layouts.urls")),

    # Auth urls
    path("", include("apps.authentication.urls")),
 
    # Misiones urls
    path('misiones/', include('apps.misiones.urls', namespace='misiones')),
 
    # Biblioteca urls
    path('biblioteca/', include('apps.biblioteca.urls', namespace='biblioteca')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)