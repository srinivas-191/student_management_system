from django.db import models

# Create your models here.
class Students(models.Model):
    student_name = models.CharField(max_length=100, blank=True, null=True)
    student_email = models.CharField(max_length=253, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    student_age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'