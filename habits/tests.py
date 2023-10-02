from rest_framework import status
from rest_framework.test import APITestCase
from user.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('password')
        self.user.save()
        response = self.client.post(
            '/user/token/',
            {'email': 'test@test.com', 'password': 'password'}
        )

        self.token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_habit(self):
        """ testing habit creation and list"""
        data = {
            "user": "test@test.com",
            "place": "room",
            "time": "10:00",
            "action": "jumps",
            "time_for_complete": "00:01:00",
            "is_pleasant": False,
            "is_public": False,
        }

        response = self.client.post(
            "/create/",
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'user': 'test@test.com', 'place': 'room', 'time': '10:00:00', 'action': 'jumps',
             'is_pleasant': False, 'periodicity': 1, 'reward': None, 'time_for_complete': '00:01:00',
             'is_public': False, 'related_habit': None}
        )

        response = self.client.get(
            '/my_list/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [{'id': 1, 'user': 'test@test.com',
                                                                      'place': 'room', 'time': '10:00:00',
                                                                      'action': 'jumps', 'is_pleasant': False,
                                                                      'periodicity': 1, 'reward': None,
                                                                      'time_for_complete': '00:01:00',
                                                                      'is_public': False, 'related_habit': None}]}
        )
