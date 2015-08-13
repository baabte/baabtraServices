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
from jobRelatedView import FileUploadView



#created by jihin
#For Load Branches
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadBranches(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnLoadBranches(data['branchCondition']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For Insert Branches
@csrf_exempt
@api_view(['GET','POST'])
def fnInsertBranches(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnInsertBranches(data['cmp_id'], data['branches'], data['rm_id']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")