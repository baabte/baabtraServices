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
from urlparse import urlparse




#created by jihin
#For insert domain details
@csrf_exempt
@api_view(['GET','POST'])
def InsertDomainView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnManageDomainDetails(data['domain'],data['curParent'],data['oldParent'],ObjectId(data['rm_id']));
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For insert domain details
@csrf_exempt
@api_view(['GET','POST'])
def LoadDomainView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    
    
    if request.method == 'POST':
        
        #stream = StringIO(request.body)
        #data = JSONParser().parse(stream)
        response=dbconn.system_js.fnLoadCourseDomain();
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")

@csrf_exempt
@api_view(['GET','POST'])
def getDomainView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    
    
    if request.method == 'POST':
        domain= urlparse(request.META.get('HTTP_REFERER')).hostname
        #stream = StringIO(request.body)
        #data = JSONParser().parse(stream)
        response=dbconn.system_js.fnLoadCourseDomain();
        return Response(json.dumps(domain, default=json_util.default))
    else:    
        return Response("failure")