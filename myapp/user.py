from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import Connection
#from models import UserMenuMapping
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
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template

@csrf_exempt
@api_view(['GET','POST'])
def fnLoadCompnayUsers(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"]
            firstId=data['firstId']
            lastId=data['lastId']
            print(lastId)
            result = dbconn.system_js.fnLoadCompanyUsers(companyId,firstId,data['type'],lastId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#service function for loading feedback lists        
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadFeedbackList(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"] 
            firstId=data['firstId']
            lastId=data['lastId']
            result = dbconn.system_js.fnLoadFeedbackList(companyId,firstId,data['type'],lastId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")


#service function for loading feedback lists        
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadFeedbackReport(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            feedbackId=data["feedbackId"] 
            result = dbconn.system_js.fnLoadFeedbackReport(feedbackId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#service function for Load Mentees For Approve  
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesForApproveView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnLoadMenteesForApprove(data["companyId"])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#service function for Load Mentees For Approve  
@csrf_exempt
@api_view(['GET','POST'])
def ApproveUserRequestView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnApproveUserRequest(data["userId"])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")