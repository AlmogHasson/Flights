from rest_framework.serializers import ModelSerializer
from base.models import Customer, Airline_Company
 
 
class Serializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class Serializer(ModelSerializer):

    class Meta:
        model = Airline_Company
        fields = '__all__'

