from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from swengs.homeworkbackend.models import Country
from swengs.homeworkbackend.serializers import CountrySerializer

from swengs.homeworkbackend.models import Soldier
from swengs.homeworkbackend.serializers import SoldierSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        country = Country.objects.all()
        serializer = CountrySerializer(country, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def country_update(request, id):

    try:
        country = Country.objects.get(pk=id)
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def soldier_list(request):
    if request.method == 'GET':
        soldier = Soldier.objects.all()
        serializer = SoldierSerializer(soldier, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SoldierSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def soldier_update(request, id):

    try:
        soldier = Soldier.objects.get(pk=id)
    except Soldier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SoldierSerializer(soldier)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SoldierSerializer(soldier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        soldier.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
