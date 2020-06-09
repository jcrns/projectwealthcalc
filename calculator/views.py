from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Assets, Liabilities, Expenses
from .serializers import AssetsSerializers, LiabilitiesSerializers, ExpensesSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
# @api_view(['GET'])
# def getAllUserInfo(request):

#     # Getting token
#     token = str(request.META['HTTP_AUTHORIZATION'])[6:]

#     # Getting User
#     token = Token.objects.get(key=token)
    
#     user = token.user

#     # Creating an object to return
#     assets = Assets.objects.filter(user=token.user)
#     assets = model_to_dict(assets)

#     liabilities = Liabilities.objects.filter(user=token.user)
#     liabilities = model_to_dict(liabilities)

#     expenses = Expenses.objects.filter(user=token.user)
#     expenses = model_to_dict(expenses)
    

#     returnDict = dict()
#     returnDict['assets'] = assets
#     returnDict['liabilities'] = liabilities
#     returnDict['expenses'] = expenses

#     return Response(returnDict)

class GetAllUserInfo(generics.RetrieveAPIView,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, pk=None):
        returnDict = dict()

        # Getting token
        token = str(request.META['HTTP_AUTHORIZATION'])[6:]

        # Getting User
        token = Token.objects.get(key=token)
        
        user = token.user

        # Creating an object to return
        assets = Assets.objects.filter(user=token.user).values()
        assets = list(assets)
        print(assets)

        liabilities = Liabilities.objects.filter(user=token.user).values()
        liabilities = list(liabilities)

        expenses = Expenses.objects.filter(user=token.user).values()
        expenses = list(expenses)
        
        # Calculating statistics
        
        # Assets estimates
        assetsTotal = 0
        for asset in assets:
            assetsTotal += asset['worth']

        # Liabilities estimates
        liabilityTotal = 0
        for liability in liabilities:
            liabilityTotal += liability['worth']

        # Expenses estimates (per month)
        expensesTotal = 0
        for expense in expenses:
            expensesTotal += expense['worth']

        
        # Net Worth
        netWorth = float(assetsTotal - liabilityTotal)
        print(netWorth)
        # Stats object
        statsDict =  { 'netWorth' : netWorth }

        returnDict['stats'] = statsDict

        returnDict['assets'] = assets
        returnDict['liabilities'] = liabilities
        print(liabilities)
        returnDict['expenses'] = expenses
        returnDict['results'] = 'success'

        return Response(returnDict)

class AssetsView(viewsets.ModelViewSet):
    queryset =  Assets.objects.all()
    serializer_class = AssetsSerializers
    permission_classes = [IsAuthenticated]

    def list(self, request, pk=None):
        
        token = str(request.META['HTTP_AUTHORIZATION'])[6:]
        print(token)
        
        # Getting user with token
        token = Token.objects.get(key=token)

        # Serializing all of the users' listed assets
        serializer = AssetsSerializers(Assets.objects.filter(user=token.user), many=True)

        return Response(serializer.data)

    def create(self, request):

        # Getting token
        token = str(request.META['HTTP_AUTHORIZATION'])[6:]

        # Getting User
        token = Token.objects.get(key=token)

        # Getting user obj
        user = token.user

        # Creating result var
        result = { 'result' : 'failed'}
        
        # Creating obj in db
        asset = Assets.objects.create(
            name=request.data['name'],
            worth=float(request.data['worth']),
            type_of_object=request.data['type_of_object'],
            user=user
        )

        # Serializing and returning initial data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        result = serializer.data
        
        return Response(result)

class LiabilitiesView(viewsets.ModelViewSet):
    queryset =  Liabilities.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = LiabilitiesSerializers

    def create(self, request):

        # Getting token
        token = str(request.META['HTTP_AUTHORIZATION'])[6:]

        # Getting User
        token = Token.objects.get(key=token)

        # Getting user obj
        user = token.user

        # Creating result var
        result = { 'result' : 'failed'}
        # Creating obj in db
        liability = Liabilities.objects.create(
            name=request.data['name'],
            worth=float(request.data['worth']),
            type_of_object=request.data['type_of_object'],
            user=user
        )

        # Serializing and returning initial data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        result = serializer.data
        
        return Response(result)

class ExpensesView(viewsets.ModelViewSet):
    queryset =  Expenses.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExpensesSerializers

    def create(self, request):

        # Getting token
        token = str(request.META['HTTP_AUTHORIZATION'])[6:]

        # Getting User
        token = Token.objects.get(key=token)

        # Getting user obj
        user = token.user

        # Creating result var
        result = { 'result' : 'failed'}
        
        # Creating obj in db
        expenses = Expenses.objects.create(
            name=request.data['name'],
            worth=float(request.data['worth']),
            type_of_object=request.data['type_of_object'],
            user=user
        )

        # Serializing and returning initial data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        result = serializer.data
        
        return Response(result)