from django.contrib import admin
from tinker.models import Event,Subscriber,Attendee

class AttendeeAdmin(admin.ModelAdmin):
	list_display=['name', 'email', 'fee_payment_date','event']
class SubscriberAdmin(admin.ModelAdmin):
	list_display=['subscriber_name','subscriber_email','subscriber_phonenumber','subscription_date']

admin.site.register(Event)
admin.site.register(Subscriber,SubscriberAdmin)
admin.site.register(Attendee, AttendeeAdmin)