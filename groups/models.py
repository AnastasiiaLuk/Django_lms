import random

from django.db import models
from faker import Faker

from .validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(max_length=50, verbose_name='Group name')
    start_date = models.DateField(validators=[validate_start_date])
    description = models.TextField(null=True, blank=True, db_column='group_descr')

    class Meta:
        db_table = 'groups'

    @classmethod
    def generate_fake_data(cls, cnt):
        groups_name = ['Python', 'Front-end', 'Java']
        f = Faker()
        for _ in range(cnt):
            g = cls()   #g = Group
            g.group_name = f'{random.choice(groups_name)}{random.randint(1,100)}'
            g.group_start = f.date()
            g.save()