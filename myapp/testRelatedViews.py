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

#creater :Arun
@csrf_exempt
@api_view(['GET','POST'])
def SaveTestStartTimeView(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnSaveTestStartTime(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")             




#creater :Arun
@csrf_exempt
@api_view(['GET','POST'])
def SaveTestStartTimeRandomExamView(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnSaveTestStartTimeRandomExam(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")             


@csrf_exempt
@api_view(['GET','POST'])
def TestTimeReCheckView(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnTestTimeReCheck(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")                         

@csrf_exempt
@api_view(['GET','POST'])
def SubmitTestView(request):  #this service will add reseller
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnSubmitTest(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")                                 

