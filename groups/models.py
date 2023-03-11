import random
import datetime

from django.db import models

from core.models import BaseModel
from core.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    group_name = models.CharField(max_length=50, verbose_name='Group name')
    start_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    description = models.TextField(null=True, blank=True, db_column='group_descr')
    headman = models.OneToOneField('students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')
    course = models.OneToOneField('courses.Course', on_delete=models.SET_NULL, null=True, blank=True, related_name='course_group')
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='groups')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name}'

    def get_name(self):
        return self.teachers.all()


    @classmethod
    def generate_fake_data(cls, cnt):
        groups_name = ['Python', 'Front-end', 'Java', 'C#', 'C/C++', 'DevOPS', 'PM', 'QA']
        for _ in range(cnt):
            g = cls()   #g = Group
            g.group_name = f'{random.choice(groups_name)}'
            g.save()