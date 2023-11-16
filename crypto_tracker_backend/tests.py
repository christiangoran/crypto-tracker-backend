from django.test import TestCase
from django.contrib.auth import get_user_model
from .serializers import CurrentUserSerializer


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
