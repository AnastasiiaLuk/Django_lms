import random

from django.db import models

from core.models import BaseModel
from groups.models import Group
from teachers.models import Teacher


class Course(BaseModel):
    course_name = models.CharField(max_length= 20, verbose_name='Course name', db_column='c_name')
    program = models.TextField(null=True, blank=True)
    course_price = models.CharField(max_length=20)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.course_name}'

    @classmethod
    def generate_fake_data(cls, cnt):
        course_name = ['Beginner', 'Middle', 'Advanced']
        for _ in range(cnt):
            s = cls()
            s.course_name = f'{random.choice(course_name)}'
            s.save()
