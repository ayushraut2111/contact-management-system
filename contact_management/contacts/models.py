from django.db import models

class contacts(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField(primary_key=True)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

