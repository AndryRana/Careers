from django.contrib import admin
from .models import Registered_email, Support, Message, Notepad, Openings, Countdown, WaitingList, Vacancies
from django.utils.html import format_html

#A) Register your models here.
class Registered_emailAdmin(admin.ModelAdmin):
    readonly_fields = ['email']
    list_display = ['email']
    search_fields = ['email']
    list_per_page = 15

admin.site.register(Registered_email, Registered_emailAdmin)

#B) Send Message
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'message' )
    list_filter = ['situation']
    list_display = ['id', 'status','created_at', '_']
    list_per_page = 10
    
 # Function to change the icons (Read - Unread)
    def _(self, obj):
        if obj.situation == 'Read':
            return True
        else:
            return False
    _.boolean = True

    # Function to color the text (Read - Unread)
    def status(self, obj):
        if obj.situation == 'Read':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(Message, MessageAdmin)

#C) Support
class SupportAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'email', 'terms', 'message', 'person', 'option')
    list_filter = ['situation', 'person']
    list_display = ['person', 'email', 'option', 'created_at', 'status', '_']
    search_fields = ['person', 'option']
    list_per_page = 10
    
    #Pending or Done icons
    def _(self, obj):
        if obj.situation == 'Done':
            return True
        else:
            return False
    _.boolean = True
    
    #Pending or Done text color
    def status(self, obj):
        if obj.situation == 'Done':
            color = "#70BF2B"
        else:
            color = '#f90074'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(Support, SupportAdmin)

#D) Notepad
class NotepadAdmin(admin.ModelAdmin):
    list_display = ['title']
    # Function to allow only one record
    def has_add_permission(self, *arg, **kwargs):
        return not Notepad.objects.exists()
admin.site.register(Notepad, NotepadAdmin)

#E) job openings
class OpeningsAdmin(admin.ModelAdmin):
    list_display = [ 'backend', 'frontend', 'fullstack', 'intern']
    # Function to allow only one record
    def has_add_permission(self, *arg, **kwargs):
        return not Openings.objects.exists()
admin.site.register(Openings, OpeningsAdmin)

#F) Countdown
class CountdownAdmin(admin.ModelAdmin):
    list_display = ['timer']
    # Function to allow only one record
    def has_add_permission(self, *arg, **kwargs):
        return not Countdown.objects.exists()
admin.site.register(Countdown, CountdownAdmin)

#E) Wait-list
class WaitingListAdmin(admin.ModelAdmin):
    readonly_fields = ('post', 'email', 'message', 'document')
    list_filter = ['situation', 'post']
    list_display = ['post', 'email', 'created_at', 'status', '_']
    search_fields = ['email']
    list_per_page = 10
    
    # Function to change the icons (Read - Unread)
    def _(self, obj):
        if obj.situation == 'Read':
            return True
        else:
            return False
    _.boolean = True

    # Function to color the text (Read - Unread)
    def status(self, obj):
        if obj.situation == 'Read':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(WaitingList, WaitingListAdmin)

#F) Vacancies Description
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ['id', 'dataTarget', 'title']
    search_fields = ['dataTarget']
    
admin.site.register(Vacancies, VacanciesAdmin)
    