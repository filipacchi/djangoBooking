from django.db import models

class Booking(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    bookingDate = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"