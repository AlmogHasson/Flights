from http.client import HTTPResponse
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Ticket
from .serializers import Serializer

#Login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod  #doesnt create a class object
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['username'] = user.password
        return token
 
#login token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 

#Homepage - Routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/login/',
        '/refresh',
        '/register/',
        '/admin/',

    ]
    return Response(routes)

# //from django.contrib.admin.views.decorators import //staff_member_required @staff_member_required
 
#Registration
@api_view(['POST'])
def register(request):
    User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['pwd'],)
        # is_staff=request.data['is_staff'],
        # is_superuser=request.data['is_SU']
    return JsonResponse({"done":"tes"} )


#Get Details(currently customers)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDetails(request):
    user = request.user
    print(user)
    details = user.customer_set.all()
    print(details)
    serializer = Serializer(details, many=True)
    return Response(serializer.data)

 
#Add Ticket to a customer
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTicket(request):
    Ticket.objects.create(
        
        
    )
    # user = request.user
    # (body=request.data["notebody"],user=user)
    # # notes = user.note_set.all()
    # # print(notes)
    # # serializer = NoteSerializer(notes, many=True)
    # return Response(serializer.data)
