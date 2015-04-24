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

#to load the user attendance report
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesAttReport(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnLoadMenteesAttReport(data['courseId'],data['userId'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")


#to load the user attendance report
@csrf_exempt
@api_view(['GET','POST'])
def FetchCandidateReport(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseCandidateList = dbconn.system_js.fnFetchCandidateReport(data['data'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseCandidateList, default=json_util.default))
    else:        
        return Response("failed")

#to load the user attendance report for batch
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadAllBatches4Report(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseCandidateList = dbconn.system_js.fnLoadAllBatches4Report(data['companyId'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseCandidateList, default=json_util.default))
    else:        
        return Response("failed")


#to load the attendance report under a selected batch
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadBatchAttReport(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseCandidateList = dbconn.system_js.fnLoadBatchAttReport(data['filterObj'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseCandidateList, default=json_util.default))
    else:        
        return Response("failed")