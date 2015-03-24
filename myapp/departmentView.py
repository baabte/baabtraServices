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
from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from pymongo import Connection
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

#created by jihin
#For Add Department
@csrf_exempt
@api_view(['GET','POST'])
def AddDepartmentView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        departmentResponse = dbconn.system_js.fnAddDepartment(data['departmentObject'], data['companyId'], data['rmId'])
        return Response(json.dumps(departmentResponse, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For load Department
@csrf_exempt
@api_view(['GET','POST'])
def LoadDepartmentView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        departmentResponse = dbconn.system_js.fnLoadDepartments(data['companyId'], data['branchId'])
        return Response(json.dumps(departmentResponse, default=json_util.default))
    else:    
        return Response("failure")