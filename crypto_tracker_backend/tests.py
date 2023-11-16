from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from .serializers import CurrentUserSerializer
from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from .permissions import IsOwnerOrReadOnly


class CurrentUserSerializerTest(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            username='Testy McPerson', password='12345')
        self.profile = self.user.userprofile

    def test_contains_expected_fields(self):
        serializer = CurrentUserSerializer(instance=self.user)
        data = serializer.data

        expected_fields = set([
            'username', 'email', 'profile_id', 'profile_image',
            'first_name', 'last_name', 'pk'
        ])
        self.assertEqual(set(data.keys()), expected_fields)
        self.assertEqual(data['profile_id'], self.profile.id)


class LogoutRouteTest(APITestCase):
    def test_logout_route_clears_cookies(self):
        response = self.client.post('/dj-rest-auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn('jwt_auth_cookie', response.cookies)
        self.assertNotIn('jwt_auth_refresh_cookie', response.cookies)


class RootRouteTest(APITestCase):
    def test_root_route_returns_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Crypto Tracker API"})


class IsOwnerOrReadOnlyTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Testyroonie', password='password123')
        self.other_user = get_user_model().objects.create_user(
            username='hacker', password='password123')
        self.permission = IsOwnerOrReadOnly()
        self.factory = RequestFactory()

    def test_safe_method_by_any_user(self):
        request = self.factory.get('/')
        request.user = self.other_user
        self.assertTrue(self.permission.has_object_permission(
            request, None, obj=self.user))
