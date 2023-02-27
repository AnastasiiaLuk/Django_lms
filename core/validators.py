from datetime import date

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')

def validate_email_domain(value):
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError(f'Emails domain "{domain}" is not correct.')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError(f'Emails domain "{domain}" is invalid.')


def validate_unique_email(st_email):
    from students.models import Student
    if Student.objects.filter(email=st_email).exists():
        raise ValidationError(f'Email {st_email} already exists.')


def validate_start_date(start_date):
    if start_date < date.today():
        raise ValidationError(f"Group can't start on {start_date}.")