from django.db import models

from .validators import validate_start_date

class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name'
    )
    start_date = models.DateField(validators=[validate_start_date])
    description = models.TextField(null=True, blank=True, db_column='group_descr')

    class Meta:
        db_table = 'groups'