from django.db import models

# Create your models here.
class tutorial(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title=models.CharField(max_length=50)
    slug= models.CharField(max_length=70)
    createdAt= models.DateTimeField
    