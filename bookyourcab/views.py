from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import BookUberForm
from .logic import calculate_google_map_timing, calculate_uber_timing, send_mail
from datetime import timedelta  
import datetime as dt


data = []
args = {}
def book_ride(request):
    if request.method == 'GET':
        form = BookUberForm()
    else:
        form = BookUberForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['source']
            destination = form.cleaned_data['destination']
            time = form.cleaned_data['time']
            email = form.cleaned_data['email']  
            print(type(time))
            try:
                google_time = calculate_google_map_timing(source, destination)
                
                f = str(dt.datetime.now().time())
                data.append(f"[{f}] - Requested Google API")
                uber_time = calculate_uber_timing(source)
                data.append(f"[{f}] - Requested Uber API ")
                delta = timedelta(minutes=google_time+uber_time)
                given_time = (dt.datetime.combine(dt.date(1,1,1),time) - delta).time()
                args['time'] = given_time

                print(given_time)
                print(type(given_time))
                now = dt.datetime.now().time()
                while True:
                    if now <= given_time:
                        send_mail(given_time, email)
                    else:
                        now = dt.datetime.now().time()
                    

            except:
                pass
            return redirect("book_ride")
    return render(request,  "book_ride.html", {'form': form, 'data': data, 'args': args})