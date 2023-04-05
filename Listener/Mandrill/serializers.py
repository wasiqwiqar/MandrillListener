from rest_framework import serializers
from .models import WebhookMessage

class WebhookMessageSerializer(serializers.ModelSerializer):
    type = serializers.ReadOnlyField(source='get_type_display')
    event_id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    message = serializers.ReadOnlyField()

    class Meta:
        model = WebhookMessage
        fields = '__all__'