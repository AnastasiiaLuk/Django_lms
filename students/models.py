import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from .validators import validate_unique_email
from groups.models import Group


VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')

class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name',
                                  validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=25, null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    # email = models.EmailField(validators=[ValidateEmailDomain(*VALID_DOMAINS)])
    email = models.EmailField(validators=[validate_unique_email], default='email')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthday).years

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        group = Group.objects.all()
        for _ in range(cnt):
            s = cls()  # s = Student()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name}.{s.last_name}@{f.random.choice(VALID_DOMAINS)}'  # name.last@domain
            s.birthday = f.date()
            s.group = f.random.choice(group)
            s.save()