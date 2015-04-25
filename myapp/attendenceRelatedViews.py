from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import Connection
from serializers import MongoAwareEncoder
from datetime import datetime
import json
from bson import json_util
from StringIO import StringIO
from rest_framework.parsers import JSONParser
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
from django.core.mail import EmailMessage

#creater :Arun \\\@///
@csrf_exempt
@api_view(['GET','POST'])
def courseElementsByAttendenceView(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fncourseElementsByAttendence(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")             

#creater :Arun \\\@///
@csrf_exempt
@api_view(['GET','POST'])
def MarkAttendenceView(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnMarkAttendence(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")

#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesBlindFromBatch(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnLoadMenteesBlindFromBatch(data['batchMappingId'],data['date']);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")


#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def saveCandidatesAttendance(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result=dbconn.system_js.saveCandidateAttendance(data['dataObj']);
        return Response(result)
        # return Response("success")            
    else:        
        return Response("failure")

#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def updateCandidatesAttendance(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result=dbconn.system_js.updateCandidateAttendance(data['dataObj']);
        return Response(result)
        # return Response("success")            
    else:        
        return Response("failure")

#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesMarkedAttendanceFromBatch(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnLoadMenteesMarkedAttendanceFromBatch(data['batchMappingId'],data['date']);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")