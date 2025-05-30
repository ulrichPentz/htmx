from django.db import models
from django.contrib.auth.models import User
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    app_name = models.CharField(max_length=100)
    app_email = models.CharField(max_length=100)
    app_products = models.TextField()
    