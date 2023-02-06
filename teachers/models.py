import datetime

from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='t_f_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='t_l_name')
    birthday = models.DateField(default=datetime.date.today)
    salary = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return f'{self.first_name} {self.last_name} (${self.salary})'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            t = cls()  # t = Teacher()
            t.first_name = f.first_name()
            t.last_name = f.last_name()
            t.birthday = f.date_between(start_date='-65y', end_date='-18y')
            t.salary = f.random_int(min=10000, max=50000)
            t.save()
