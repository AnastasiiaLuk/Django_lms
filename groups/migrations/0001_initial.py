# Generated by Django 4.1.5 on 2023-01-19 22:12

from django.db import migrations, models


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
                ('start_date', models.DateField()),
                ('description', models.TextField(blank=True, db_column='group_descr', null=True)),
            ],
        ),
    ]