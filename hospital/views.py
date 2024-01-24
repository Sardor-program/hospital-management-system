from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from hospital.models import Doctor, Patient, Appointment

def home(request):
    return render(request, 'hospital/home.html')


def about(request):
    return render(request, 'hospital/about.html')


def contact(request):
    return render(request, 'hospital/contact.html')


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    do = 0
    pa = 0
    ap = 0
    for i in doctors:
        do += 1
    for i in patient:
        pa += 1
    for i in appointment:
        ap += 1
    context = {
        "do": do,
        "pa": pa,
        "ap": ap
    }
    return render(request, 'hospital/index.html', context)


def Login(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    context = {
          'error': error
        }
    return render(request, 'auth/login.html', context)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('auth/login')
    logout(request)
    return redirect('admin_login')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor = Doctor.objects.all()
    context = {
        "doctor": doctor
    }
    return render(request, 'hospital/view_doctor.html', context)


def delete_doctor(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def add_doctor(request):
    error = ""
    if request.method == 'POST':
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        special = request.POST["special"]
        try:
            Doctor.objects.create(name=name, mobile=mobile, special=special)
            error = "no"
        except:
            error = "yes"
    context = {
      "error": error
    }
    return render(request, 'hospital/add_doctor.html', context)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    patient = Patient.objects.all()
    context = {
        "patient": patient
    }
    return render(request, 'hospital/view_patient.html', context)



def delete_patient(request, pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('view_patient')


def add_patient(request):
    error = ""
    if request.method == 'POST':
        name = request.POST["name"]
        gender = request.POST["gender"]
        mobile = request.POST["mobile"]
        address = request.POST["address"]
        try:
            Patient.objects.create(name=name, gender=gender, mobile=mobile, address=address)
            error = "no"
        except:
            error = "yes"
    context = {
      "error": error
    }
    return render(request, 'hospital/add_patient.html', context)


#============================
def view_appointment(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    appointment = Appointment.objects.all()
    context = {
        "appointment": appointment
    }
    return render(request, 'hospital/view_appointment.html', context)



def delete_appointment(request, pk):
    if not request.user.is_staff:
        return redirect('admin_login')
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('view_appointment')



def add_appointment(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    error = ""
    if request.method == "POST":
        n = request.POST['doctor']
        p = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=n).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date=date, time=time)
            error = "no"
        except:
            error = "yes"
    context = {
        "error": error,
        "doctor": doctor1,
        "patient": patient1
    }
    return render(request, 'hospital/add_appointment.html', context)

