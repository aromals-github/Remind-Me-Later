# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReminderSerializer
from .models import Reminder


class CreateReminderView(APIView):
    """
    API endpoint to create a reminder.

    Request data should include the following fields:
    - date: Date of the reminder (format: YYYY-MM-DD)
    - time: Time of the reminder (format: HH:MM:SS)
    - message: Text message for the reminder
    - reminder_type: Type of reminder (SMS or Email)

    Returns HTTP 201 CREATED on successful creation of the reminder.
    Returns HTTP 400 BAD REQUEST if request data is invalid.
    """
    def post(self, request):
        """
        Handle POST requests to create a reminder.

        :param request: HTTP request object containing reminder data
        :return: HTTP response with created reminder data or error messages
        """
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Handle GET requests to retrieve reminders.

        :param request: HTTP request object containing optional query parameters for filtering
        :return: HTTP response with a list of reminder data
        """
        date = request.query_params.get('date')
        time = request.query_params.get('time')
        reminder_type = request.query_params.get('reminder_type')

        reminders = Reminder.objects.all()

        # Apply filters if provided
        if date:
            reminders = reminders.filter(date=date)
        if time:
            reminders = reminders.filter(time=time)
        if reminder_type:
            reminders = reminders.filter(reminder_type=reminder_type)

        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
