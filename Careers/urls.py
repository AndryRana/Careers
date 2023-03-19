"""Careers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from job import views
from Careers import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
# ==============================Frontend==========================================
    path('', views.home, name="home"),
    # Path to render opportunities page
    path('opportunities', views.opportunities, name="opportunities"),
    #login &logout
    path('login/', include('django.contrib.auth.urls')),
    #Support
    path('support', views.support, name="support"),
    #send Message
    path('send_message', views.send_message, name="send_message"),
    #waiting list
    path('waiting_list', views.waiting_list, name="waiting_list"),
# ==============================SEND EMAIL==========================================
    # Path to send frontend form
    path('frontend_email', views.frontend_email, name="frontend_email"),
    # Path to send backend form
    path('backend_email', views.backend_email, name="backend_email"),
    # Path to send fullstack form
    path('fullstack_email', views.fullstack_email, name="fullstack_email"),
    # Path to send Intern form
    path('intern_email', views.intern_email, name="intern_email"),
    
# ==============================Backend==========================================
    # Backend panel control
    path('backend/', views.backend, name="backend"),
    # Notepad
    path('notepad', views.notepad, name="notepad"),
    # Job openings
    path('openings', views.openings, name="openings"),
    # Vacancies
    path('vacancies', views.vacancies, name="vacancies"),
    # Vacancies Description
    path('description/<int:vacancy_id>', views.description, name="description"),
    #Countdown
    path('countdown', views.countdown, name="countdown"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
