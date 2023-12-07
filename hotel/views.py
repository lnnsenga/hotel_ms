from django.shortcuts import render
from .models import User
from .forms import  RegisterForm




# Create your views here.

def login(request):
    user = User.objects.all()
    return render(request, 'registration/login.html',
                  {'user':user,
                   'browser_heading':'Login',
                   })

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', 
                  {"form": form,
                   'browser_heading':'Login',    
                   })

def index(request):
    return render(request, 'hotel/home.html',
                  {'browser_heading':'Home',                
                   }) 



def room_list(request):
    return render(request, 'hotel/room-list.html',
                  {'browser_heading':'Room List',
                   }) 

def view_room(request):
    return render(request, 'hotel/room.html',
                  {'browser_heading':'Room'
                   }) 


def book_room(request):
    return render(request, 'hotel/book.html',
                  {'browser_heading':'Booking',
                   }) 


def make_payment(request):
    return render(request, 'hotel/payment.html',
                  {'browser_heading':'Payment',
                   'notification':'Payment',
                   }) 
# def make_payment(request):
#     return render(request, 'hotel/payment.html',
#                   {'browser_heading':'Payment',
                   
#                    }) 

def make_reservation(request):
    return render(request, 'hotel/reservation.html',
                  {'browser_heading':'Reservation',
                   'notification':'Reservation',
                   }) 


def manager_dashboard(request):
    return render(request, 'dashboard/manager.html',
                  {'browser_heading':'Dashboard',
                   'navbar_colour':'black',
                   'user':'Manager',
                   }) 


def receptionist_dashboard(request):
    return render(request, 'dashboard/receptionist.html',
                  {'browser_heading':'Dashboard',
                   'navbar_colour':'darkblue',
                   'user':'Receptionist',
                   }) 
