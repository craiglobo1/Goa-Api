from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import *
from .serializers import *
import requests

baseUrl = 'http://localhost:3000/api/'


def getId(dict, field):
    return dict[field].split('/')[-2]


class AllList(APIView):
    def get(self, request, id, format=None):

        try:
            buisnessSerializer = BuisnessSerializer(
                Buisness.objects.get(houseNo=id), many=False, context={'request': request})

            ownerId = getId(buisnessSerializer.data, 'owner')
            ownerSerializer = OwnerSerializer(Owner.objects.get(
                id=ownerId), many=False, context={'request': request})

            taxesSerializer = TaxesSerializer(
                Taxes.objects.filter(buisness=id), many=True, context={'request': request})

            applicationSerializer = ApplicationSerializer(
                Application.objects.filter(buisness=id), many=True, context={'request': request})

            return Response({'buisness': buisnessSerializer.data, 'owner': ownerSerializer.data,
                             'taxes': taxesSerializer.data, 'application': applicationSerializer.data})
        except Exception as e:
            print(type(e))
            return Response({'Error': str(e)},status=)
    def post():

        


class OwnerView(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class BuisnessView(viewsets.ModelViewSet):
    queryset = Buisness.objects.all()
    serializer_class = BuisnessSerializer


class TaxesView(viewsets.ModelViewSet):
    queryset = Taxes.objects.all()
    serializer_class = TaxesSerializer


class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/task-list/',
#         'Detail View': '/task-detail/<str:pk>/',
#         'Create': '/task-create/',
#         'Update': '/task-update/<str:pk>/',
#         'Delete': '/task-delete/<str:pk>/',
#     }
#     return Response(api_urls)


# @api_view(['GET'])
# def houseIdList(request):
#     buisness = Buisness.objects.all()
#     serializer = BuisnessSerializer(buisness, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def houseIdDetail(request, id):
#     buisness = Buisness.objects.get(houseNo=id)
#     serializer = BuisnessSerializer(buisness, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def houseCreate(request):
#     print(type(request.data))
#     serializer = BuisnessSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
