from django.db import models

# Create your models here.


class Reminder(models.Model):
    """
        Model to store reminder data.

        Fields:
        - date: Date of the reminder
        - time: Time of the reminder
        - message: Text message for the reminder
        - reminder_type: Type of reminder (SMS or Email)
    """

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(
        max_length=20,
        choices=[
            ('SMS', 'SMS'),
            ('Email', 'Email')
            ]
        )
