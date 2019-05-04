from django.shortcuts import render, redirect
from django.http import HttpResponse
from tinker.models import Event,Subscriber,Attendee
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
	return render(request, "home.html")

def events_catalogue(request):
	all_events=Event.objects.all()
	return render(request,"events_catalogue.html", {'events':all_events})

def events(request,pk):
	event=Event.objects.get(pk=pk)
	return render(request,"event.html",{'event':event})

def subscribers(request):
	if request.method == "POST":
		sub_name= request.POST.get('subscriber_name',None)
		sub_email= request.POST.get('subscriber_email',None)
		sub_number= request.POST.get('subscriber_phonenumber',None)
		new_subscriber = Subscriber.objects.create(subscriber_name=sub_name,subscriber_email=sub_email,
		subscriber_phonenumber=sub_number)
		return redirect(f"/home/")
	return render(request,"subscribers.html")

def attendees(request):
	events = Event.objects.all()
	if request.method == "POST":
		at_name=request.POST.get('name',None)
		at_email=request.POST.get('email',None)
		at_phonenumber=request.POST.get('phonenumber',None)
		at_event=int(request.POST.get('event',None))
		event = Event.objects.get(pk=at_event)
		event.registered += 1
		event.save()
		#at_amount=request.POST.get('amount_payable',None)
		print(at_name)
		new_attendee=Attendee.objects.create(name=at_name,email=at_email,phonenumber=at_phonenumber,event=event )
		return redirect(f"/home/")
	return render(request,"registrations.html", {"events":events})

def messages(request):

	users = Subscriber.objects.all()
	for user in users:
		#msg = EmailMessage("Look ahead for further updates and news.....", message, to=[user.subscriber_email])
		#msg.send()
		subject, from_email, to = 'Welcome to tinkercrafts', 'tinkercrafts123@gmail.com', user.subscriber_email

		html_content = render_to_string('subscribermail.html') # render with dynamic value
		text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

# create the email, and attach the HTML version as well.
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
	return HttpResponse("SUCCESS")

def addevent(request):
	events=Event.objects.all()
	if request.method == "POST":
		e_name= request.POST.get('event_name',None)
		e_date= request.POST.get('event_date',None)
		e_fee= request.POST.get('fee',None)
		e_venue= request.POST.get('event_venue',None)
		e_capacity= request.POST.get('capacity',None)
		e_about= request.POST.get('about',None)
		new_event = Event.objects.create(event_name=e_name,event_date=e_date,
		fee=e_fee,event_venue=e_venue,capacity=e_capacity,about=e_about)
		return redirect(f"/home/")
	return render(request,"addevent.html")

def adminview(request):
	event=Event.objects.all()
	return render(request,"adminview.html",{"events":event})




