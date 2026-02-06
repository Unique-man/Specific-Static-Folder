from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import *
# Create your views here.

class FactCRUD(APIView):
    def get(self,request,pk=None):
        if pk == None:
            FTO=Fact.objects.all()                   # fetches all students from DB.
            FJD=FactMS(FTO,many=True)                #converts them into Python dictionaries.
            return Response(FJD.data)                   # - DRF’s Response object wraps the serialized data.sends those dictionaries as JSON(API) to the client
        else:
            FO=Fact.objects.get(id=pk)   #get specific student object
            FJD=FactMS(FO)     # means you created a serializer object and passed a Student model instance into it.  #- DRF now knows how to translate that model instance into JSON-like data.
            return Response(FJD.data)  #- .data Property- When you access SJD.data, DRF converts the model instance into a Python dictionary that is ready to be rendered as JSON.


    def post(self,request):
        FJDO=request.data #incoming json data
        PO=FactMS(data=FJDO) #pass the json data to deserializer
        if PO.is_valid(): #validate the data
            PO.save() #save the data to db
            return Response({"msg":"Fact Created"})#return response
        return Response(PO.errors)
    
    def put(self,request,pk):
        FJDO=request.data                                #incoming json data
        FO=Fact.objects.get(id=pk)                    #get object based on id
        PO=FactMS(FO,data=FJDO)                       #pass object and json data to deserializer
        if PO.is_valid():                                #validate the data
            PO.save()                                    #save the data to db
            return Response({"msg":"Fact Updated"})      #return response
        return Response(PO.errors)

    def patch(self,request,pk):
        FJDO=request.data                                   #incoming json data
        FO=Fact.objects.get(id=pk)                       #get object based on id
        PO=FactMS(FO,data=FJDO,partial=True)             #pass object and json data to deserializer
        if PO.is_valid():                                   #validate the data
            PO.save()                                       #save the data to db
            return Response({"msg":"Fact Partially Updated"})         #return response
        return Response(PO.errors)

    def delete(self,request,pk):
        PO=Fact.objects.get(id=pk)                       #get object based on id
        PO.delete()                                         #delete the object
        return Response({"msg":"Fact Deleted"})             #return response

    
        