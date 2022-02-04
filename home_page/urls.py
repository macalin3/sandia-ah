from django.urls import path
from . import views

app_name = 'main_page'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.show_about, name="about"),
    path('appointment', views.book_appointment, name="appointment"),
    path('process_appointment', views.process_appointment, name="process_appointment"),
    path('success', views.success, name="success"),
    path('cancel', views.delete, name="cancel"),
    path('modify', views.modify_appt, name="modify"),
    path('update_appt', views.update_appt, name="update_appt"),
    path('drsandia', views.show_drsandia, name="drsandia"),
    path('booking_login', views.booking_login, name="booking_login"),
    path('booking_process', views.booking_process, name="booking_process"),
    path('new-pet-registration', views.show_registration),
]