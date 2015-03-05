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

#created by midhun sudhakar
#on 13-10-14
@csrf_exempt  
@api_view(['GET','POST'])
def Login(request):
    #connect to our local mongodb
        db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
        #get a connection to our database
        dbconn = db[settings.MONGO_DB]
        if request.method == 'POST':
            stream =StringIO(request.body)
            data = JSONParser().parse(stream) 
            LoginData=data["loginData"]
            try:
                
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    real_ip = x_forwarded_for.split(',')[0]
                else:
                    real_ip = request.META.get('REMOTE_ADDR')
                LoginData['ip']=real_ip
                log = dbconn.system_js.fnLogin(LoginData)
            except Exception as e:
                return Response(str(e))
            return Response(json.dumps(log, default=json_util.default))
        else:    
            return Response("failure")

@csrf_exempt
@api_view(['GET','POST'])
def logout(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        UserLogoutObjId=data["UserLogoutObjId"]
        try:
           result=dbconn.system_js.fun_logout(UserLogoutObjId)    
        except:
           return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
         
#created by midhun sudhakar
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def loadlogUserdata(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        UserDataObjId=data["UserDataObjId"]
        try:
           result=dbconn.system_js.fun_load_log_user_data(UserDataObjId)    
        except:
           return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
