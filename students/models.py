from random import choice

from django.db import models

from core.models import PersonModel
from groups.models import Group


class Student(PersonModel):
    phone = models.CharField(max_length=25) #, null=True
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        if self.group:
            return f'{self.first_name} {self.last_name}({self.group.group_name})'
        else:
            return f'{self.first_name} {self.last_name}()'

    @classmethod
    def _generate(cls):
        groups = Group.objects.all()
        student = super()._generate()
        student.group = choice(groups)
        student.save()