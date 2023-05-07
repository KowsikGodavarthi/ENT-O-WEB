from django.contrib import admin
from .models import Booking, Feedback


class BookingAdmin(admin.ModelAdmin):
    list_display = ['artist', 'date', 'name', 'email', 'phone']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'message']

admin.site.register(Booking, BookingAdmin)
admin.site.register(Feedback, FeedbackAdmin)
