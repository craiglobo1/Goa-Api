from rest_framework import serializers
from .models import *


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'url', 'firstName', 'lastName', 'contactNo', 'vaddo')


class BuisnessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buisness
        fields = ('url', 'owner', 'houseNo',
                  'establishmentName', 'rooms', 'type', 'vaddo')


class TaxesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Taxes
        fields = ('id', 'url', 'buisness', 'tradeTax', 'boardTax',
                  'garbageTax', 'startDate', 'dueDate', 'Year')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'url', 'buisness', 'applicationNo', 'applicationDate',
                  'resolutionNo', 'resolutionDate', 'sarpanchRemark')


# class AllSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Buisness
#         fields = ('url', 'owner', 'houseNo',
#                   'establishmentName', 'rooms', 'type', 'vaddo')
