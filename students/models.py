import datetime

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'