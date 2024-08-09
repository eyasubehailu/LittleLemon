# from django.test import TestCase

# class MenuViewTest(TestCase):
from django.test import TestCase
from restaurant.models import Menu

from restaurant.serializers import MenuSerializer
from rest_framework import status
from django.urls import reverse

class MenuViewTest(TestCase):

    def setUp(self):
        # Add a few test instances of the Menu model
        self.menu1 = Menu.objects.create(name='Breakfast', description='Morning meals', price=5.99)

    def test_getall(self):
        # Make a GET request to retrieve all Menu objects
        response = self.client.get(reverse('menu-list'))
        
        # Serialize the Menu objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Assert that the response data matches the serialized data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
