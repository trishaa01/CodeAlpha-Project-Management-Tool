from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    NOTIF_TYPES = [
        ('task_assigned', 'Task Assigned'),
        ('comment_added', 'Comment Added'),
        ('project_invite', 'Project Invite'),
    ]

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    notif_type = models.CharField(max_length=30, choices=NOTIF_TYPES, default='task_assigned')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}"

    class Meta:
        ordering = ['-created_at']