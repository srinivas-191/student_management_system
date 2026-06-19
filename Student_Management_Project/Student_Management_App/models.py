from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(unique=True, max_length=253, blank=True, null=True)
    course = models.CharField(max_length=100)
    student_age = models.IntegerField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'students'