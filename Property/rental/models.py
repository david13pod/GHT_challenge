from tkinter import CASCADE
from django.db import models

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    rental = models.ForeignKey('Rental', related_name='rentalName', on_delete=models.CASCADE)
    reserve_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()


    def save(self, *args, **kwargs):
        id = Reservation.objects.all().count()+1
        self.reserve_id= "Res-"+str(id)+" ID"
        super(Reservation, self).save(*args, **kwargs)