from django.urls import path
from .views import CreateReminderView

urlpatterns = [
    path('set-reminder', CreateReminderView.as_view(), name='create_reminder')
]
