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

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def loadUserNotificationView(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)

            notificationDetails = dbconn.system_js.fnLoadUserNotification(data['fkLoginId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(notificationDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def loadUserNotifications(request):  #this service will load all notifications of a user
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)

            notificationDetails = dbconn.system_js.fnLoadUserNotificationFull(data)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(notificationDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def markNotificationAsRead(request):  #this service will update notification as read
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            id = ObjectId(data['id'])
            fkLoginId = data['fkLoginId']
            result = dbconn.clnNotification.update({'_id':id,'fkLoginId':fkLoginId},{'$set':{'read':1}})
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#creater :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def newNotification(request):  #this service will load all notifications of a user
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)

            result = dbconn.system_js.fnNewNotification(data)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

