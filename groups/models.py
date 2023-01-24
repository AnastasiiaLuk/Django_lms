from django.db import models

class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name'
    )
    start_date = models.DateField()
    description = models.TextField(null=True, blank=True, db_column='group_descr')

    class Meta:
        db_table = 'groups'