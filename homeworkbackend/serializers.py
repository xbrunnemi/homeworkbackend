from rest_framework import serializers

from swengs.homeworkbackend.models import Country
from swengs.homeworkbackend.models import Soldier


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class SoldierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soldier
        fields = ['id',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'arm_of_service',
                  'country']
