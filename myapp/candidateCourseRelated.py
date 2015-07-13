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
from jobRelatedView import FileUploadView

#created by lijin
@csrf_exempt
@api_view(['GET','POST'])
def getCurrentElement(request):
	#connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnGetCurrentCourseElement(data['userLoginId'],data['courseMappingId'],data['direction']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")


@csrf_exempt
@api_view(['GET','POST'])
def getCandidateDetailsForCertificate(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnGetCandidateDetailsForCertificate(data['rmId'],data['courseId']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")



#created by arun
@csrf_exempt
@api_view(['GET','POST'])
def getCourseSyllabus4CandidateView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnGetCourseSyllabus4CandidateView(data['userLoginId'],data['courseMappingId']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")        