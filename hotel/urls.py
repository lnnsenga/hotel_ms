from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('login',views.login,name="login"),
    path('sign-up',views.sign_up,name="sign_up"),
    path('room-list', views.room_list, name="room_list"),
    path('room', views.view_room, name="view_room"),
    path('book', views.book_room, name="book_room"),
    path('payment', views.make_payment, name="make_payment"),
    path('reservation', views.make_reservation, name="make_reservation"),
    path('dashboard/manager', views.manager_dashboard, name="manager_dashboard"),
    path('dashboard/receptionist', views.receptionist_dashboard, name="receptionist_dashboard"),
  
    
]
