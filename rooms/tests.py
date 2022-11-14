import json

from django.contrib.auth.models import AnonymousUser
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory

from core.enums import EventType
from events.models import Event
from rooms.models import Room

User = get_user_model()


class RoomTestCase(TestCase):

    def setUp(self):
        self.apifactory = APIRequestFactory()
        self.admin = User.objects.create(first_name="Admin", last_name="Admin", email="admin@test.com",
                                         is_active=True, is_superuser=True)
        self.customer = User.objects.create(first_name="Customer", last_name="Customer", email="customer@test.com",
                                            is_active=True)
        self.room = Room.objects.create(name="Room A", capacity=50)

    def test_api_list_no_login(self):
        """Test of the scenario list as unauthenticated user"""
        url = reverse('rooms-list')
        request = self.apifactory.get(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()
        view = resolve(url).func
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, 401)

    def test_api_list_admin(self):
        """Test of the scenario list as admin user"""
        url = reverse('rooms-list')
        request = self.apifactory.get(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.admin
        view = resolve(url).func
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, 200)

    def test_api_list_customer(self):
        """Test of the scenario list as customer user"""
        url = reverse('rooms-list')
        request = self.apifactory.get(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.customer
        view = resolve(url).func
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, 200)

    def test_api_create_no_login(self):
        """Test of the scenario create as unauthenticated user"""
        url = reverse('rooms-list')
        data = {
            'name': "test",
            'capacity': 2,
        }
        request = self.apifactory.post(url, data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()
        view = resolve(url).func
        response = view(request)
        response.render()
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 401)

    def test_api_create_customer(self):
        """Test of the scenario create as customer user"""
        url = reverse('rooms-list')
        data = {
            'name': "test",
            'capacity': 2,
        }
        request = self.apifactory.post(url, data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.customer
        view = resolve(url).func
        response = view(request)
        response.render()
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 403)

    def test_api_create_admin_empty_field(self):
        """Scenario test create as admin user and empty fields"""
        url = reverse('rooms-list')
        data = {
            'name': "",
            'capacity': "",
        }
        request = self.apifactory.post(url, data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.admin
        view = resolve(url).func
        response = view(request)
        response.render()
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 400)

    def test_api_create_admin_without_capacity(self):
        """Scenario test create as user admin and without capacity field"""
        url = reverse('rooms-list')
        data = {
            'name': "test",
            'capacity': "",
        }
        request = self.apifactory.post(url, data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.admin
        view = resolve(url).func
        response = view(request)
        response.render()
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 400)

    def test_api_create_admin(self):
        """Scenario test create as admin user"""
        url = reverse('rooms-list')
        data = {
            'name': "test",
            'capacity': 50,
        }
        request = self.apifactory.post(url, data)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.admin
        view = resolve(url).func
        response = view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Room.objects.count(), 2)

    def test_api_delete_no_login(self):
        """Test the delete as unauthenticated user scenario"""
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        request = self.apifactory.delete(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = AnonymousUser()
        view = resolve(url).func
        response = view(request, pk=self.room.pk)

        self.assertEqual(response.status_code, 401)

    def test_api_delete_customer(self):
        """Scenario test delete as customer user"""
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        request = self.apifactory.delete(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.customer
        view = resolve(url).func
        response = view(request, pk=self.room.pk)

        self.assertEqual(response.status_code, 403)

    def test_api_delete_admin(self):
        """Scenario test delete as admin user"""
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        request = self.apifactory.delete(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.admin
        view = resolve(url).func
        response = view(request, pk=self.room.pk)

        self.assertEqual(response.status_code, 204)

    def test_api_delete_with_event(self):
        """Scenario test delete as admin user and room associated to an event"""
        Event.objects.create(name="Event1", type=EventType.public, room=self.room)
        url = reverse('rooms-detail', kwargs={'pk': self.room.pk})
        request = self.apifactory.delete(url)
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        request.user = self.admin
        view = resolve(url).func
        response = view(request, pk=self.room.pk)

        self.assertEqual(response.status_code, 400)


