from django.db import models

class contacts(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(primary_key=True,max_length=10)
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.name

