from django.urls import path
from hospital.views import (
    home,
    about,
    contact,
    Login,
    logout_admin,
    index,
    view_doctor,
    delete_doctor,
    add_doctor,
    view_patient,
    add_patient,
    delete_patient,
    view_appointment,
    delete_appointment,
    add_appointment,
)


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('admin_login', Login, name='admin_login'),
    path('logout_admin/', logout_admin, name='logout_admin'),
    path('index/', index, name='dashboard'),
    path('view_doctor/', view_doctor, name='view_doctor'),
    path('delete_doctor(?P<int:pid>/)', delete_doctor, name='delete_doctor'),
    path('add_doctor/', add_doctor, name='add_doctor'),
    path('view_patient/', view_patient, name='view_patient'),
    path('add_patient/', add_patient, name='add_patient'),
    path('delete_patient(?P<int:pk>/)', delete_patient, name='delete_patient'),
    path('view_appointment/', view_appointment, name='view_appointment'),
    path('delete_appointment(?P<int:pk>/)', delete_appointment, name='delete_appointment'),
    path('add_appointment/', add_appointment, name='add_appointment')
]
