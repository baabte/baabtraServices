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

#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def loadProfileData(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            userloginId = data["userloginId"]
            profileData=dbconn.system_js.fnLoadProfile(userloginId)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(profileData, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

@csrf_exempt
@api_view(['GET','POST'])
def updateUserProfileData(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            userProfileDataForUpdate = data["userProfileDataForUpdate"]
            updateResponse=dbconn.system_js.fnUpdateUserProfileDatas(userProfileDataForUpdate)    
            
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(updateResponse, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


# this service used for change password of the user
@csrf_exempt
@api_view(['GET','POST'])
def changeUserPassword(request):  
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            changePwdObj = data["changePwdObj"]
            changePwdResponse=dbconn.system_js.fnChangePassword(changePwdObj)    
            
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(changePwdResponse, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


# this service used for change password of the user
@csrf_exempt
@api_view(['GET','POST'])
def changelanguage(request):  
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            changelanguageResponse=dbconn.system_js.fnchangelanguage(datas)    
            
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(changelanguageResponse, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))