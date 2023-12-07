from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    GENDER_CHOICES =  (
        ("Female","Female"),
        ("Male","Male"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=300, blank=False, unique=True)
    gender = models.CharField(max_length=6,choices= GENDER_CHOICES, default="Male")
    first_name = models.CharField(max_length= 60, blank=False)
    last_name = models.CharField(max_length= 60, blank=False)
    email = models.EmailField(max_length=300,blank = False, unique=True)
    phone_number = models.CharField(max_length=30, unique= True)
    email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default= False)
    is_superadmin = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar_url = models.ImageField(upload_to='media/')

    

    def __str__(self):
        return self.first_name + self.last_name


class Customer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return "Customer "+ self.id
    


class Receptionist(models.Model):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title +" "+ self.id


class Manager(models.Model):
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title +" "+ self.id



class RoomType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=150, unique= True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "RoomType" + self.id



class RoomStatus(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "RoomStatus " + self.id



class Room(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_type_id = models.ForeignKey(RoomType, unique=True, on_delete=models.SET_NULL, null = True)
    room_status_id = models.ForeignKey(RoomStatus, unique=True, on_delete=models.SET_NULL, null = True)
    room_no = models.CharField(max_length=7, unique= True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Room no."+ self.room_no
    

class PaymentType(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length= 60, unique=True, blank = False,editable=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Payment Type - "+ self.name

 
class Payment(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_type_id = models.ForeignKey(PaymentType, unique=True, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer, unique=True, on_delete=models.DO_NOTHING)
    staff_id = models.UUIDField(editable=False)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Payment "+ self.id
    

class Booking(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Room, unique=True, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer, unique=True, on_delete=models.DO_NOTHING)
    staff_id = models.UUIDField(editable=False)
    payment_id = models.ForeignKey(Payment, unique=True, on_delete=models.DO_NOTHING, editable=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Booking "+ self.id
    
    
