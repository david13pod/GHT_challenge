
from urllib import response
from django.urls import reverse
from django.test import TestCase, Client
from .models import Rental, Reservation
from .views import reservations_table
from datetime import date


# Create your tests here.
class TestReservation(TestCase):
    
    def setUp(self):
        self.rent1 = Rental.objects.create(
            name = "Rental-1" 
        )
        self.rent2 = Rental.objects.create(
            name = "Rental-2" 
        )
        self.table_url=reverse('reserved_tables')
        self.client=Client()

        self.reserver1= Reservation.objects.create(
            rental = self.rent1,
            checkin_date = date(2022,1,1),
            checkout_date = date(2022,1,13),
        )

        self.reserver2= Reservation.objects.create(
            rental = self.rent1,
            checkin_date = date(2022,1,20),
            checkout_date = date(2022,2,10),
        )

        self.reserver3= Reservation.objects.create(
            rental = self.rent1,
            checkin_date = date(2022,2,20),
            checkout_date = date(2022,3,10),
        )

        self.reserver4= Reservation.objects.create(
            rental = self.rent2,
            checkin_date = date(2022,1,2),
            checkout_date = date(2022,1,20),
        )

        self.reserver5= Reservation.objects.create(
            rental = self.rent2,
            checkin_date = date(2022,1,20),
            checkout_date = date(2022,2,11),
        )

    def test_previous_reserve_table(self):

        response = self.client.get(self.table_url)
        # response = reservations_table()
        # print(response.json()['Previous reservation ID'])
        self.assertEqual(response.json()['Previous reservation ID'][0],'-' )
        self.assertEqual(response.json()['Previous reservation ID'][3],'-' )

