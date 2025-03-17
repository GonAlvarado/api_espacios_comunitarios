from rest_framework import serializers
from django.contrib.auth.models import User
from EspaciosComunitarios.models import EspacioDb, DiaDb, HorarioDb, ReferenteDb, RetiroDb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

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

class EspacioDbSerializer(serializers.ModelSerializer):
    dia = DiaDbSerializer(many=True)
    horario = HorarioDbSerializer(many=True)
    referente_fk = ReferenteDbSerializer()
    retiros = RetiroDbSerializer(many=True, read_only=True)
    class Meta:
        model = EspacioDb
        fields = '__all__'