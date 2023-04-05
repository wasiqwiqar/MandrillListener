from django.db import models
from django.utils import timezone

# Create your models here.


class WebhookMessage(models.Model):
    event_id = models.CharField(unique=True, max_length=48)
    message = models.JSONField()
    # not using auto_add_now intentionally
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    # Going to save some values from the message for faster querying
    SEND = 'send'
    DEFERRAL = 'deferral'
    HARD_BOUNCE = 'hard_bounce'
    SOFT_BOUNCE = 'soft_bounce'
    DELIVERED = 'delivered'
    OPEN = 'open'
    CLICK = 'click'
    SPAM = 'spam'
    UNSUB = 'unsub'
    REJECT = 'reject'

    TYPE_CHOICES = [
        (SEND, 'Send'),
        (DEFERRAL, 'Deferral'),
        (HARD_BOUNCE, 'Hard Bounce'),
        (SOFT_BOUNCE, 'Soft Bounce'),
        (DELIVERED, 'Delivered'),
        (OPEN, 'Open'),
        (CLICK, 'Click'),
        (SPAM, 'Spam'),
        (UNSUB, 'Unsub'),
        (REJECT, 'Reject'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        ordering = ['-created_at']
