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

#creater :midhun sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def loadInputTypes(request):  #this service will retrieve all roles of particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]


    if request.method == 'POST':
    	stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        name=data["name"]
        try:
            inputTypes=dbconn.system_js.function_loadInputTypes()    
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps(inputTypes, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

@csrf_exempt
@api_view(['GET','POST'])
def newFeatureCreation(request):  #this service will retrieve all roles of particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]


    if request.method == 'POST':
    	stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        newFeature=data["newFeature"]
        try:
            dbconn.system_js.function_create_newFeature(newFeature)    
        except:
            return Response(json.dumps("newFeature", default=json_util.default))
        return Response(json.dumps("success", default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))