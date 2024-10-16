from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from EspaciosComunitarios.models import EspacioDb, DiaDb, HorarioDb, ReferenteDb, RetiroDb
from .serializers import EspacioDbSerializer, DiaDbSerializer, HorarioDbSerializer, ReferenteDbSerializer, RetiroDbSerializer, UserSerializer

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error":"invalid password"}, status = status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key, "user":serializer.data["id"]}, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class EspacioViewSet(viewsets.ModelViewSet):
    queryset = EspacioDb.objects.all()
    serializer_class = EspacioDbSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class DiaViewSet(viewsets.ModelViewSet):
    queryset = DiaDb.objects.all()
    serializer_class = DiaDbSerializer 

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class HorarioViewSet(viewsets.ModelViewSet):
    queryset = HorarioDb.objects.all()
    serializer_class = HorarioDbSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ReferenteViewSet(viewsets.ModelViewSet):
    queryset = ReferenteDb.objects.all()
    serializer_class = ReferenteDbSerializer

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class RetiroViewSet(viewsets.ModelViewSet):
    queryset = RetiroDb.objects.all()
    serializer_class = RetiroDbSerializer