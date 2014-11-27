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





#created by Lijin
#For posting jobs as company admin
@csrf_exempt
@api_view(['GET','POST'])
def postCompanyJobs(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    companyJobCollection = dbconn['clnCompanyJobs']

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        data['companyId']=ObjectId(data['companyId']);
        data['crmId']=ObjectId(data['crmId']);
        data['urmId']=ObjectId(data['urmId']);
        response=dbconn.system_js.fnPostJob(data);
        #Result = companyJobCollection.insert(data);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")

#created by Lijin
#For fetching posted jobs for company website API
@csrf_exempt
@api_view(['GET','POST'])
def APIgetCompanyJobs(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    companyJobCollection = dbconn['clnCompanyJobs']

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        skipVal=data["pageNum"]*5;
        companyCode=data["companyCode"]
        jobsCln = list(companyJobCollection.find({'fk_company_obj_id':ObjectId(companyCode)}).skip( skipVal ).limit(5))
        return Response(json.dumps(jobsCln, default=json_util.default))
    else:    
        return Response("failure")

#created by Lijin
#For fetching posted jobs for company account
@csrf_exempt
@api_view(['GET','POST'])
def getCompanyJobs(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    companyJobCollection = dbconn['clnCompanyJobs']

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        data['cmp_id']=ObjectId(data['cmp_id'])
        #limitVal=10
        #skipVal=data["pageNum"]*limitVal 
        #companyCode=data["companyCode"]
        response=dbconn.system_js.fnListJobs(data['cmp_id'],data['search_key'],data['search_range']);
        return Response(json.dumps(response, default=json_util.default))
    else:    
        return Response("failure")


#created by Jihin 
#For updating posted jobs for company account
@csrf_exempt
@api_view(['GET','POST'])
def UpdateJobDetailsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response  = dbconn.system_js.fnUpdateJobDetails(ObjectId(data['jobId']),data['jobDetails']);
        return Response(StringIO(response))
    else:    
        return Response("failure")

#created by Jihin 
#For hide posted jobs for company account
@csrf_exempt
@api_view(['GET','POST'])
def HideJobDetailsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        response  = dbconn.system_js.fnHideJobDetails(ObjectId(data['jobId']),data['jobStaus']);
        return Response(StringIO(response))
    else:    
        return Response("failure")