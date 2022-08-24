from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.models import Flight, Ticket
from .serializers import FlightSerializer, CustomerSerializer, TicketSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status



#------------------------------------------------------------  Login  -----------------------------------------------------------------------
#
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod  #doesnt create a class object
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['password'] = user.password #######
        return token

#----------------------------------------------------------   token  ------------------------------------------------------------------------


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#------------------------------------------------------  Homepage - Routes  -----------------------------------------------------------------

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/login/',
        '/refresh',
        '/register/',
        '/admin/',
        '/flights',

    ]
    return Response(routes)

# //from django.contrib.admin.views.decorators import //staff_member_required @staff_member_required
 
#-----------------------------------------------------------------  Registration  -----------------------------------------------------------

@api_view(['POST'])
def register(request):
    User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['pwd'],)
        # is_staff=request.data['is_staff'],
        # is_superuser=request.data['is_SU']
    return JsonResponse({"done":"tes"} )


#-----------------------------------------------  Get Details(currently customer details) ---------------------------------------------------

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDetails(request):
    user = request.user
    print(user)
    details = user.customer_set.all()
    print(details)
    serializer = CustomerSerializer(details, many=True)
    return Response(serializer.data)

#------------------------------------------------------  Add Ticket to a customer   ---------------------------------------------------------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTicket(request):
    customer=request.user.id
    print(customer)
    flight = request.data["id"]
    print(flight)
    Ticket.objects.create(flight_id=flight ,customer_id=customer)
    return JsonResponse({"test":"successful"}, )

#------------------------------------------------------  Show logged user Tickets  ---------------------------------------------------------

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def userTicketsPreview(request):
    user=request.user
    # print(user)
    products = Ticket.objects.filter(customer=user.id)
    # print(products)
    serializer = TicketSerializer(products, many=True)
    return Response(serializer.data)

#--------------------------------------------------------------  Logout  -------------------------------------------------------------------
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST )


#----------------------------------------------------------  Show All Flights  ------------------------------------------------------------
#--------------------------------------------------- at http://127.0.0.1:8000/flights/ ----------------------------------------------------

@api_view(['POST','GET'])
def allFlights(request):
    # user=request.user
    # print(user)
    flights=Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)
    
    #add get single by id
    #later add to show only future flights and maybe past flights too as an option
