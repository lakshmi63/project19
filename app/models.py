from django.db import models

# Create your models here.
class Emp(models.Model):
    job=models.CharField(max_length=100,primary_key=True)
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    def __str__(self):
        return self.job


class Dept(models.Model):
    job=models.OneToOneField(Emp,on_delete=models.CASCADE)
    deptno=models.IntegerField()
    loc=models.CharField(max_length=100)
    def __str__(self):
        return self.loc

