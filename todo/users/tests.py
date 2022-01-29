import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserModelViewSet
from .models import User as users


class TestUserViewSet(TestCase):
    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'user8', 'firstname': 'user8', 'lastname': 'user8',
                                               'email': 'user8@user8.com'}, format='json')
        admin = User.objects.create_superuser('superadmin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_user(self):
        user = users.objects.create(username='user8', firstname='user8', lastname='user8', email='user8@user8.com')
        client = APIClient()
        admin = User.objects.create_superuser('superadmin', 'admin@admin.com', 'admin123456')
        client.login(username='superadmin', password='admin123456')
        response = client.put(f'/api/users/{user.uuid}/',
                              {'username': 'user8', 'firstname': 'user888', 'lastname': 'user8',
                               'email': 'user8@user8.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = users.objects.get(uuid=user.uuid)
        self.assertEqual(user.firstname, 'user888')
        client.logout()


class TestUserViewSet2(APITestCase):
    def test_edit_random_user(self):
        user = mixer.blend(users, username='user9')
        admin = User.objects.create_superuser('superadmin2', 'admin@admin.com', 'admin123456')
        self.client.login(username='superadmin2', password='admin123456')
        response = self.client.put(f'/api/users/{user.uuid}/',
                                   {'username': 'user999', 'firstname': 'user999', 'lastname': 'user9',
                                    'email': 'user9@user9.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = users.objects.get(uuid=user.uuid)
        self.assertEqual(user.username, 'user999')
