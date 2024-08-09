from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking, Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['Title', 'Price', 'Inventory']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['Name', 'No_of_guests', 'BookingDate']