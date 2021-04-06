"""deviare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from weather.views import Home

from django.http import HttpResponse
#TODO remove this to properly include a url.

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('weather/', include('weather.urls')),
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT / 'static')

admin.site.site_header = "Deviare Backend"
admin.site.site_title = "Deviare Backend Portal"
admin.site.index_title = "Welcome to Deviare Assessment Backend"