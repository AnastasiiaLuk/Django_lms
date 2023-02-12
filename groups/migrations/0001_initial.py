# Generated by Django 4.1.5 on 2023-02-12 16:07

import datetime
from django.db import migrations, models
import groups.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50, verbose_name='Group name')),
                ('start_date', models.DateField(default=datetime.date.today, validators=[groups.validators.validate_start_date])),
                ('description', models.TextField(blank=True, db_column='group_descr', null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]
