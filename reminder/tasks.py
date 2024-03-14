# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime
from .models import Reminder


@shared_task
def send_reminders():
    """
    Task to send reminders.
    Only Via Email is notified now.
    """
    now = datetime.now()
    reminders_to_send = Reminder.objects.filter(date=now.date(), time=now.time())

    for reminder in reminders_to_send:
        if reminder.reminder_type == 'Email':
            # Send email reminder
            send_mail(
                'Reminder',
                reminder.message,
                'email@email.com',
                ['to@email.com'],
                fail_silently=False,
            )
        elif reminder.reminder_type == 'SMS':
            # Send SMS reminder
            # Implement SMS sending logic here
            pass
