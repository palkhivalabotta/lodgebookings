from django.db import models
#ADMIN

class Hotels(models.Model):
    hotel_name=models.CharField(max_length=50,primary_key=True)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=20)
    contact_no=models.IntegerField()
#===================================
class roomtype(models.Model):
    name = models.CharField(max_length=10,primary_key=True)
    #name = models.CharField(max_length=50)

class check_availability(models.Model):
    #h_name=models.ForeignKey(Hotels,on_delete=models.CASCADE)
    room_type=models.ForeignKey(roomtype,on_delete=models.CASCADE)
    r_number=models.IntegerField()
    max_numbers=models.IntegerField()
    bed_option=models.CharField(max_length=50)
    price=models.IntegerField()
    #total_rooms=models.CharField(max_length=50)
    date = models.DateField()
    #check_out = models.DateField()
 #=============================================
class feedback(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    msg=models.CharField(max_length=250)

#====================================================
#USER

class register(models.Model):
    username = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=50)

class booking_room(models.Model):
    name = models.CharField(max_length=100)
    #cust_id = models.CharField(max_length=10)
    room_type = models.ForeignKey(Hotels,on_delete=models.CASCADE)
    room_number = models.IntegerField(primary_key=True)
    credit_card = models.IntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    #============================================================
class display(models.Model):
    #cust_id = models.CharField(max_length=10)
    email_id = models.ForeignKey(register, on_delete=models.CASCADE)
    #name=models.ForeignKey(booking_room,on_delete=models.CASCADE)
    room_number = models.ForeignKey(booking_room,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=10)
    total_cost = models.IntegerField()
    #=================================================================
class cancel(models.Model):
    #cust_id = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)
    room_number = models.ForeignKey(booking_room,on_delete=models.CASCADE)
    email_id = models.ForeignKey(register,on_delete=models.CASCADE)
    #=========================================================================
class after_booking(models.Model):
    cust_id = models.CharField(max_length=10)
    #username = models.CharField(max_length=100,default=True)
    room_number = models.ForeignKey(booking_room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    email_id = models.ForeignKey(register,on_delete=models.CASCADE)

