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
#For global values
@csrf_exempt
@api_view(['GET','POST'])
def LoadGlobalValuesView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnGetGlobals(data['key']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For upload profile picture 
@csrf_exempt
@api_view(['GET','POST'])
def UploadProfilePicView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)

        response=dbconn.system_js.fnUploadProfilePic(data['path'],ObjectId(data['urmId']));
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")


#created by jihin
#For upload profile picture 
@csrf_exempt
@api_view(['GET','POST'])
def SaveAppSettingsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response=dbconn.system_js.fnSaveAppSettings(ObjectId(data["companyId"]),data["appSettings"],ObjectId(data["rmId"]));
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For upload profile picture 
@csrf_exempt
@api_view(['GET','POST'])
def RemoveFileFromServerView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        
        myfile = data["pathToBeDelete"]
        response = default_storage.delete(myfile)
        #response=dbconn.system_js.fnSaveAppSettings(ObjectId(data["companyId"]),data["appSettings"],ObjectId(data["rmId"]));
        return Response(response)
    else:    
        return Response("failure")

#created by jihin
#For load mentees by company
@csrf_exempt
@api_view(['GET','POST'])
def loadMenteesView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        menteesResponse = dbconn.system_js.fnLoadMenteesByCompanyId(data["companyId"]);
        return Response(json.dumps(menteesResponse, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For load Load Role Under a Company
@csrf_exempt
@api_view(['GET','POST'])
def LoadRoleUnderCompanyView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        menteesResponse = dbconn.system_js.fnLoadRolesUnderCompany(data["companyId"]);
        return Response(json.dumps(menteesResponse, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For load Load Role Under a Company
@csrf_exempt
@api_view(['GET','POST'])
def LoadUserCardDetailsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        menteesResponse = dbconn.system_js.fnLoadUserCardDetail(data["rmId"]);
        return Response(json.dumps(menteesResponse, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For load Load Users Under a Role
@csrf_exempt
@api_view(['GET','POST'])
def LoadUsersUnderRoleView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        userResponse = dbconn.system_js.fnLoadUsersUnderRole(data["roleId"],data['companyId']);
        return Response(json.dumps(userResponse, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For Load Company Customer Details
@csrf_exempt
@api_view(['GET','POST'])
def LoadCompanyCustomerDetailsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        userResponse = dbconn.system_js.fnLoadCompanyCustomerDetails(data["eMailId"], data['companyId'], data['type']);
        return Response(json.dumps(userResponse, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For Load Company Customer Details
@csrf_exempt
@api_view(['GET','POST'])
def LoadInterviewQuestionBankView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        QuestionBank = dbconn.system_js.fnLoadInterviewQuestionBank(data['interviewQuestionObj']);
        return Response(json.dumps(QuestionBank, default=json_util.default))
    else:    
        return Response("failure")

#created by jihin
#For Load Company domain details
@csrf_exempt
@api_view(['GET','POST'])
def checkDomainExitsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        DomainExits = dbconn.system_js.fnCheckDomainExits(data['domainName']);
        return Response(json.dumps(DomainExits, default=json_util.default))
    else:    
        return Response("failure")


#created by Arun
#For Load Company domain details
@csrf_exempt
@api_view(['GET','POST'])
def checkRegDomainExitsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        DomainExits = dbconn.system_js.fnCheckRegDomainExits(data['domainName']);
        return Response(json.dumps(DomainExits, default=json_util.default))
    else:    
        return Response("failure")

#Created by Jihin
#For save academic year
@csrf_exempt
@api_view(['GET','POST'])
def saveAcademicYearView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        DomainExits = dbconn.system_js.fnSaveAcademicYear(data);
        return Response(json.dumps(DomainExits, default=json_util.default))
    else:    
        return Response("failure")

#Created by Jihin
#For save academic year
@csrf_exempt
@api_view(['GET','POST'])
def loadAcademicYearView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        DomainExits = dbconn.system_js.fnLoadAcademicYear(data);
        return Response(json.dumps(DomainExits, default=json_util.default))
    else:    
        return Response("failure")

#Created by Jihin
#For save Financial year
@csrf_exempt
@api_view(['GET','POST'])
def saveFinancialYearView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        financialYearResponse = dbconn.system_js.fnSaveFinancialYear(data);
        return Response(json.dumps(financialYearResponse, default=json_util.default))
    else:    
        return Response("failure")

#Created by Jihin
#For save financial year
@csrf_exempt
@api_view(['GET','POST'])
def loadFinancialYearView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        DomainExits = dbconn.system_js.fnLoadFinancialYear(data);
        return Response(json.dumps(DomainExits, default=json_util.default))
    else:    
        return Response("failure")