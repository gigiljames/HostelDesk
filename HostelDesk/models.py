from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Login_cred(models.Model):
    U_Id = models.CharField(primary_key=True, max_length=9, validators=[MinLengthValidator(9)])
    Password = models.CharField(max_length=30)
    R_Id = models.IntegerField()

class Course_details(models.Model):
    Course_Id = models.IntegerField(primary_key=True)
    Course_Name = models.CharField(max_length=50)


class Student_details(models.Model):
    Name = models.CharField(max_length=40)
    Roll_No = models.CharField(primary_key=True, max_length=9, validators=[MinLengthValidator(9)])
    Gender = models.CharField(max_length=1, validators=[MinLengthValidator(1)])
    Course_Id = models.ForeignKey(Course_details,to_field="Course_Id", on_delete=models.CASCADE, default=0)
    Ph_No = models.BigIntegerField()
    Email = models.EmailField()
    P_Name = models.CharField(max_length=40)
    P_Ph_No = models.BigIntegerField()

class Hostel_details(models.Model):
    H_Id = models.IntegerField(primary_key=True)
    H_Name = models.CharField(max_length=30)
    Free_Room = models.IntegerField()

# class Mess_details(models.Model):
#     M_Id = models.IntegerField(primary_key=True)
#     M_Name = models.CharField(max_length=50)
#     Allocated = models.IntegerField()
#     Capacity = models.IntegerField()
#     Accepted_Gender = models.IntegerField(default=3)

class Room_details(models.Model):
    H_Id = models.IntegerField()
    Floor_Id = models.IntegerField()
    Room_Id = models.IntegerField()
    Status = models.IntegerField()

class Hostel_manager(models.Model):
    Hm_Id = models.IntegerField(primary_key=True, validators=[MinLengthValidator(9)])
    Name = models.CharField(max_length=50)
    H_Id = models.ForeignKey(Hostel_details,to_field="H_Id", on_delete=models.CASCADE)


class Student_allocation_h(models.Model):
    H_Id = models.IntegerField()
    Floor_Id = models.IntegerField()
    Room_Id = models.IntegerField()
    Roll_No = models.IntegerField()

class Mess_details(models.Model):
    M_Id = models.IntegerField(primary_key=True)
    M_Name = models.CharField(max_length=50)
    Allocated = models.IntegerField()
    Capacity = models.IntegerField()
    Accepted_Gender = models.IntegerField()

class Mess_manager(models.Model):
    Mm_Id = models.IntegerField(primary_key=True, max_length=9, validators=[MinLengthValidator(9)])
    Name = models.CharField(max_length=40)
    M_Id = models.ForeignKey(Mess_details,to_field="M_Id", on_delete=models.CASCADE)

class Student_allocation_m(models.Model):
    M_Id = models.IntegerField()
    Roll_No = models.IntegerField()
