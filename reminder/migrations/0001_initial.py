# Generated by Django 5.0.3 on 2024-03-14 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('reminder_type', models.CharField(choices=[('SMS', 'SMS'), ('Email', 'Email')], max_length=20)),
            ],
        ),
    ]
