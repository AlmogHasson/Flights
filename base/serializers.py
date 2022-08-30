from datetime import datetime
from xmlrpc.client import DateTime
from rest_framework.serializers import ModelSerializer
from base.models import  Airline_Company, Customer, Flight, Ticket, Country
 
 
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline_Company
        fields = '__all__'

class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class FlightSerializer(ModelSerializer):
    destination_country= CountrySerializer()
    origin_country= CountrySerializer()
    airline_company= AirlineSerializer()

    class Meta:
        model = Flight
        fields = '__all__'
   

