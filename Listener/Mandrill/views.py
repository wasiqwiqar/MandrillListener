from rest_framework.generics import ListAPIView, GenericAPIView
from .models import WebhookMessage
from .serializers import WebhookMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class WebhookListener(ListAPIView, GenericAPIView):
    serializer_class = WebhookMessageSerializer
    queryset = WebhookMessage.objects.all()

    def get_queryset(self):
        type = self.request.query_params.get('type', None)
        limit = self.request.query_params.get('limit', None)

        if type is not None:
            self.queryset = self.queryset.filter(type=type)

        if limit is not None:
            self.queryset = self.queryset[:int(limit)]

        return super().get_queryset()

    def post(self, request, *args, **kwargs):
        # Expected response format is in README.md 
        # Get the events from the request
        mandrill_events = request.data.get('mandrill_events')

        # Hit the database only once, so bulk_create
        webhook_messages = []

        for event in mandrill_events:
            # Get the event type and message
            type = event.get('event')
            message = event.get('msg')
            event_id = message.get('_id')

            # Create the WebhookMessage object
            webhook_message = WebhookMessage(
                event_id=event_id, message=message, type=type)

            # Add it to the list
            webhook_messages.append(webhook_message)

        # Save the messages to the database in a single hit
        messages = WebhookMessage.objects.bulk_create(
            webhook_messages, ignore_conflicts=True)

        messages = WebhookMessage.objects.filter(event_id__in=[message.event_id for message in webhook_messages])
        open_count = messages.filter(type='open').count()

        # Send a notification to the frontend with the number of opens
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications", {
                "type": "send_notification",
                "message": f"{open_count} new opens, {len(messages)} new messages, {len(mandrill_events)} events received",
            })

        # Return a 200 response
        return Response(status=status.HTTP_200_OK)
