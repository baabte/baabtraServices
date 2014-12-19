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

#creater :midhun sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def loadFeatures(request):  #this service will retrieve all features in the database
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            features=dbconn.system_js.function_loadFeatures()    
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps(features, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#creater :midhun sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def addNewBillingPlan(request):  #this service will add new billing plans
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        NewPaln=data["NewPaln"]
        try:
            result=dbconn.system_js.function_create_newplan(NewPaln)  
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps("success", default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#creater :midhun sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def retriveCurrentPlans(request):  #this service will add new billing plans
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        
        try:
            plans=dbconn.system_js.function_retrieve_plans()  
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps(plans, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

@csrf_exempt
@api_view(['GET','POST'])
def delete_plans(request):  #this service will add new billing plans
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        plan_to_delete=data["plan_to_delete"]
        try:
            dbconn.system_js.fun_delete_plan(plan_to_delete)  
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps("success", default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
