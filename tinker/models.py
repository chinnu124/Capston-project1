from django.db import models

class Event(models.Model):
	event_name=models.CharField(max_length=200)
	event_date=models.DateTimeField()
	fee=models.IntegerField(default=0)
	event_venue=models.CharField(max_length=200)
	capacity=models.IntegerField(default=0)
	about=models.TextField()
	cover=models.ImageField(upload_to="events/")

	def __str__(self):
		return self.event_name

class Subscriber(models.Model):
	subscriber_name=models.CharField(max_length=200)
	subscriber_email=models.CharField(max_length=200)
	subscriber_phonenumber=models.IntegerField(default=0)
	subscription_date=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.subscriber_name

class Attendee(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phonenumber=models.IntegerField(default=0)
	event=models.ForeignKey(Event, on_delete=models.CASCADE)
	#amount_payable=models.ForeignKey(Event,on_delete=models.CASCADE)
	fee_payment_date=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name

