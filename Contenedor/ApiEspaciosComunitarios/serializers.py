from rest_framework import serializers
from django.contrib.auth.models import User
from EspaciosComunitarios.models import EspacioDb, DiaDb, HorarioDb, ReferenteDb, RetiroDb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class EspacioDbSerializer(serializers.ModelSerializer):
    retiros = serializers.StringRelatedField(many=True)
    class Meta:
        model = EspacioDb
        fields = '__all__'

class DiaDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaDb
        fields = '__all__'

class HorarioDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDb
        fields = '__all__'

class ReferenteDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenteDb
        fields = '__all__'

class RetiroDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetiroDb
        fields = '__all__'