# Generated by Django 4.1.5 on 2023-02-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('course_name', models.CharField(db_column='c_name', max_length=20, verbose_name='Course name')),
                ('program', models.TextField(blank=True, null=True)),
                ('course_price', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
