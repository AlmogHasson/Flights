from rest_framework.serializers import ModelSerializer
from base.models import Customer, Flight, Ticket
 
 
class Serializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

class FlightSerializer(ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'



