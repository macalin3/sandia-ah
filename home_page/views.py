from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment
from my_secrets import secrets
import random
import string

def index(request):
    context = {
        "google_map_api": secrets.google_map_api
    }
    return render(request, "index.html", context)

def show_about(request):
    return render(request, "about.html")

def book_appointment(request):
    return render(request, "appointment.html")

def process_appointment(request):

    errors = Appointment.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/appointment")

    else:
        
        code = string.ascii_uppercase
        conf_code = ''.join(random.choice(code) for i in range(6))

        appt = Appointment()
        appt.fname = request.POST['fname']
        appt.lname = request.POST['lname']
        appt.pname = request.POST['pname']
        appt.phone = request.POST['phone']
        appt.email = request.POST['email']
        appt.preferred_date = request.POST['preferred_date']
        appt.preferred_time = request.POST['preferred_time']
        appt.confirmation = conf_code
        appt.save()
        request.session['appt_id'] = appt.id

        # print(request.POST)
        # request.session['fname'] = request.POST['fname']
        # request.session['lname'] = request.POST['lname']
        # request.session['pname'] = request.POST['pname']
        # request.session['phone'] = request.POST['phone']
        # request.session['email'] = request.POST['email']
        # request.session['preferred_date'] = request.POST['preferred_date']
        # request.session['preferred_time'] = request.POST['preferred_time']
    return redirect("/success")

def success(request):

    context = {
        "this_appt": Appointment.objects.get(id=request.session['appt_id'])
    }
    return render(request, "success.html", context)

def delete(request):
    appt = Appointment.objects.get(id=request.session['appt_id'])
    appt.delete()
    return redirect("/")

def modify_appt(request):

    context = {
        "this_appt": Appointment.objects.get(id=request.session['appt_id'])
    }
    return render(request, "modify.html", context)

def update_appt(request):

    # errors = Appointment.objects.mod_validator(request.POST)

    # if len(errors) > 0:
    #     for k, v in errors.items():
    #         messages.error(request, v)
    #     return redirect("/modify")

    # else:
        to_update = Appointment.objects.get(id=request.session['appt_id'])
        if request.POST.get('preferred_date'):
            to_update.preferred_date = request.POST.get('preferred_date')
        if request.POST.get('preferred_time'):
            to_update.preferred_time = request.POST.get('preferred_time')
        # appt.preferred_date = request.POST['preferred_date']
        # print("----------------------------------------------")
        # print(request.POST['preferred_date'])
        # appt.preferred_time = request.POST['preferred_time']
        # print(request.POST['preferred_time'])
        to_update.save()
        return redirect("/success")

def show_drsandia(request):
    return render(request, "drsandia.html")

def booking_login(request):
    return render(request, "booking_login.html")

def booking_process(request):
    appt_matching_confirmation = Appointment.objects.filter(confirmation=request.POST['confirmation']).first()
    if appt_matching_confirmation is not None:
        if request.POST['lname'] == appt_matching_confirmation.lname:
            request.session['appt_id'] = appt_matching_confirmation.id
            return redirect("/success")
        
        elif request.POST['lname'] != appt_matching_confirmation.lname:
            messages.error(request, "Unable to find appointment. Please try again.")
            return redirect("/booking_login")

    else:
        messages.error(request, "All fields are required.")
        return redirect("/booking_login")

def show_registration(request):
    return render(request, "registration.html")