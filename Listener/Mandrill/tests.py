from rest_framework.test import APITestCase
from rest_framework import status
from .models import WebhookMessage


class WebhookTests(APITestCase):
    def test_webhook_post(self):
        data = {
            "mandrill_events": [
                {
                    "event": "send",
                    "msg": {
                        "_id": 1,
                        "subject": "Test Subject",
                    }
                },
                {
                    "event": "open",
                    "msg": {
                        "_id": 2,
                        "subject": "Test Subject",
                    }
                }
            ]
        }

        response = self.client.post('/webhook/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(WebhookMessage.objects.count(), 2)

    def test_webhook_list(self):
        data = {
            "mandrill_events": [
                {
                    "event": "send",
                    "msg": {
                        "_id": 1,
                        "subject": "Test Subject",
                    }
                },
                {
                    "event": "open",
                    "msg": {
                        "_id": 2,
                        "subject": "Test Subject",
                    }
                }
            ]
        }

        self.client.post('/webhook/', data, format='json')
        response = self.client.get('/webhook/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
