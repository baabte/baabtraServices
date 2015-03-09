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

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def saveNewBatches(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            data['batchObj']['urmId'] = ObjectId(data['batchObj']['urmId'])
            data['batchObj']['ucrmId'] = ObjectId(data['batchObj']['crmId'])
            data['batchObj']['companyId'] = ObjectId(data['batchObj']['companyId'])
            batchDetails=dbconn.system_js.fnAddNewBatches(data['batchObj'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadBatches(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            batchDetails=dbconn.system_js.fnLoadBatches(data['cmpId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

