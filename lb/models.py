from django.db import models
#ADMIN




#USER

class register(models.Model):
    username = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=50)
class check_availability(models.Model):
    room_type = models.CharField(max_length=10)
    #room_number = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    contact_no = models.IntegerField()
class booking_room(models.Model):
    name = models.CharField(max_length=100)
    cust_id = models.CharField(max_length=10)
    room_number = models.IntegerField(primary_key=True)
    credit_card = models.IntegerField()
    room_type = models.CharField(max_length=10)
    check_in = models.DateField()
    check_out = models.DateField()
class display(models.Model):
    cust_id = models.CharField(max_length=10)
    email_id = models.ForeignKey(register, on_delete=models.CASCADE)
   # username=models.ForeignKey(booking_room,on_delete=models.CASCADE)
    room_number = models.ForeignKey(booking_room,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=10)
    total_cost = models.IntegerField()
class cancel(models.Model):
    cust_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    room_number = models.ForeignKey(booking_room,on_delete=models.CASCADE)
    email_id = models.ForeignKey(register,on_delete=models.CASCADE)
class after_booking(models.Model):
    cust_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    room_number = models.ForeignKey(booking_room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    email_id = models.ForeignKey(register,on_delete=models.CASCADE)


