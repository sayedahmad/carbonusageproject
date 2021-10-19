from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usage(models.Model):
    """ The model stores carbon usage data"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usage')
    usage_type_id=models.ForeignKey('UsageType', on_delete=models.CASCADE, related_name='usage_type')
    usage_at=models.DateTimeField()
    amount=models.FloatField()

    def __str__(self):
        return str(self.usage_type_id)+" "+str(self.amount)


class UsageType(models.Model):
    """ the model stores the types of carbon usage """
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    unit=models.CharField(max_length=100, null=True)
    factor=models.FloatField(max_length=50, null=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.unit