"""capston URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from tinker.views import home,events,events_catalogue,subscribers,attendees,messages,adminview,addevent

urlpatterns = [
	path('home/',home),
	path('events/',events_catalogue),
	path('events/<int:pk>/',events),
    path('subscribe/',subscribers),
    path('register/',attendees),
    path('message/',messages),
    path('adminview/',adminview),
    path('addevent/',addevent),
    path('admin/', admin.site.urls),
]
