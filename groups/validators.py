from datetime import date
from django.core.validators import ValidationError

def validate_start_date(start_date):
    if start_date < date.today():
        raise ValidationError(f"Group can't start on {start_date}.")