import random
import datetime

from django.db import models

from .validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(max_length=50, verbose_name='Group name')
    start_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    description = models.TextField(null=True, blank=True, db_column='group_descr')

    class Meta:
        db_table = 'groups'

    @classmethod
    def generate_fake_data(cls, cnt):
        groups_name = ['Python', 'Front-end', 'Java', 'C#', 'C/C++', 'DevOPS', 'PM', 'QA']
        for _ in range(cnt):
            g = cls()   #g = Group
            g.group_name = f'{random.choice(groups_name)}'
            g.save()