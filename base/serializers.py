from rest_framework.serializers import ModelSerializer
from base.models import Customer, Airline_Company, Ticket
 
 
class Serializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TicketSerializer(ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

