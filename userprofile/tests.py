from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import UserProfile
from django.contrib.auth.models import User
from userprofile.views import UserProfileDetailsView
import json


class UserProfileAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'username': 'testie', 'password': 'password123'}
        self.user, created = User.objects.get_or_create(**self.user_data)
        self.user.set_password('password123')
        self.user.save()
        self.user_profile, _ = UserProfile.objects.update_or_create(
            user=self.user,
            defaults={'name': 'Test User',
                      'bio': 'I am writing my test bio. Very exciting'}
        )

        response = self.client.post(
            '/dj-rest-auth/login/', data=self.user_data)
        if response.status_code == 200:
            self.token = json.loads(response.content).get(
                'access_token')
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        else:
            self.token = None

    def test_get_user_profile(self):
        """
        Test retrieving a user's profile.
        """
        response = self.client.get(
            reverse('userprofiledetailsview', kwargs={'id': self.user_profile.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'testie')
        self.assertEqual(response.data['name'], 'Test User')
        self.assertEqual(
            response.data['bio'], 'I am writing my test bio. Very exciting')
