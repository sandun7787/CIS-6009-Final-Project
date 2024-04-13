from django.db import models
from django.contrib.auth.models import User


from .choices import DOCTOR_STATUS

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    contact = models.ChartField(max_length=100, null=True)
    address = models.CharField(max_length=100,null=True)
    dob =  models.DataField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username  
# Create your models here.
