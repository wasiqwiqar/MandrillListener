from rest_framework.generics import ListAPIView, GenericAPIView
from .models import WebhookMessage
from .serializers import WebhookMessageSerializer
from rest_framework.response import Response
from rest_framework import status


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
        # Expected format:
        # {
        #    mandrill_events: [
        #     {
        #        "event": "send",
        #     "msg": {
        #      "_id": "5f7b1c0f0c5d4c0c8c1c1c1c",
        # }
        #   ],
        # }

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
        WebhookMessage.objects.bulk_create(
            webhook_messages, ignore_conflicts=True)

        # Return a 200 response
        return Response(status=status.HTTP_200_OK)
