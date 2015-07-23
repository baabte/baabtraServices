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
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.files.storage import default_storage
import sys
import urllib
import os.path


@csrf_exempt
@api_view(['GET','POST'])
def fnLoadCompnayUsers(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"]
            firstId=data['firstId']
            lastId=data['lastId']
            print(lastId)
            result = dbconn.system_js.fnLoadCompanyUsers(companyId,firstId,data['type'],lastId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#service function for loading feedback lists        
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadFeedbackList(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"] 
            firstId=data['firstId']
            lastId=data['lastId']
            result = dbconn.system_js.fnLoadFeedbackList(companyId,firstId,data['type'],lastId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")


#service function for loading feedback lists        
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadFeedbackReport(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            feedbackId=data["feedbackId"] 
            result = dbconn.system_js.fnLoadFeedbackReport(feedbackId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#service function for Load Mentees For Approve  
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesForApproveView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnLoadMenteesForApprove(data["companyId"], data["statusType"], data['pageNumber'], data['nPerPage'], data['searchKey'],data['orderFormType'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")


#service function for Load Mentees For payment after enrolling  
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesForPayment(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnLoadMenteesForPayment(data["companyId"], data['pageNumber'], data['nPerPage'], data['searchKey'],data['orderFormType'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#service function for Load Mentees For Approve  
@csrf_exempt
@api_view(['GET','POST'])
def ApproveUserRequestView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnApproveUserRequest(data["userId"], data["orderFormId"], data["courseKey"], data["statusType"], data["rmId"], data['companyId'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")



#service function for Add User Nomination
@csrf_exempt
@api_view(['GET','POST'])
def addUserNominationView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            responseObject = dbconn.system_js.fnAddUserNomination(data['orderObject'] ,data["rmId"])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(responseObject, default=json_util.default))
    else:        
        return Response("failed")


#service function for Add User Nomination
@csrf_exempt
@api_view(['GET','POST'])
def loadOrderFormByIdView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            responseObject = dbconn.system_js.fnLoadOrderFormById(data['ofId'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(responseObject, default=json_util.default))
    else:        
        return Response("failed")

#service function to update the status of an order form
@csrf_exempt
@api_view(['GET','POST'])
def updateOrderFormStatusView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            data['orderForm']['_id'] = ObjectId(data['orderForm']['_id'])
            data['orderForm']['companyId'] = ObjectId(data['orderForm']['companyId'])
            data['orderForm']['crmId'] = ObjectId(data['orderForm']['crmId'])
            data['orderForm']['urmId'] = ObjectId(data['orderForm']['urmId'])
            responseObject = dbconn.system_js.fnUpdateOrderFormStatus(data['orderForm'], data['actTransactions'], data['paymentReceipt'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(responseObject, default=json_util.default))
    else:        
        return Response("failed")

#service function to load the verified users from training request
@csrf_exempt
@api_view(['GET','POST'])
def FnLoadVerifiedCandidates(request): 
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            responseObject = dbconn.system_js.fnLoadMenteesForApprove(data['companyId'],data['statusType'],'','','','')
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(responseObject, default=json_util.default))
    else:        
        return Response("failed")

#created by Akshath
@csrf_exempt
@api_view(['GET','POST'])
def fnenrollSingleUser(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)   
            result=dbconn.system_js.fnEnrollUser(data['regObject']);
        except ValueError:
            return Response(json.dumps(result, default=json_util.default))
        dbconn.system_js.fnUpdateOrderFormStatus4EnrollUser(data['courseObj'],data['regObject']['loggedusercrmid'])
        return Response(json.dumps(result, default=json_util.default))

        # return Response("success")            
    else:        
        return Response("failure")

#created by Akshath
@csrf_exempt
@api_view(['GET','POST'])
def fnenrollBulkUsers(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            for user in data['listData']:

                try:
                    result=dbconn.system_js.fnEnrollUser(user['selectedUser'])
                except ValueError:
                    return Response(json.dumps(ValueError, default=json_util.default))
                # data['courseObj']['index']=user['index']
                result=dbconn.system_js.fnUpdateOrderFormStatus4EnrollUser(user['orderFormData'],user['selectedUser']['loggedusercrmid'])
            
        except ValueError:
            return Response(json.dumps(result, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))

        # return Response("success")            
    else:        
        return Response("failure")


@csrf_exempt
@api_view(['GET','POST'])
def FetchUsersToCourseAllocateView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"]
            firstId=data['firstId']
            lastId=data['lastId']
            searchKey=data['searchKey']
            result = dbconn.system_js.fnFetchUsersToCourseAllocate(companyId,firstId,data['type'],lastId,searchKey)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")



@csrf_exempt
@api_view(['GET','POST'])
def AllocateUsersToCourseView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnAllocateUsersToCourse(data)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#created by Lijin
@csrf_exempt
@api_view(['GET','POST'])
def verifyCandidateByCourse(request):
    #connect to mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            for user in data['listData']:

                result=dbconn.system_js.fnUpdateOrderFormStatus4Verify(user['orderFormData'],user['crm'])
            
        except ValueError:
            return Response(json.dumps(result, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))

        # return Response("success")            
    else:        
        return Response("failure")

#created by lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadParents(request):  #this service will load parent users
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnLoadParents(data)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")


#created by lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnSaveCandidateMapping(request):  #this service will load parent users
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnSaveCandidateMapping(data)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

#created by lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMappedCandidatesForParent(request):  #this service will load parent users
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnLoadMappedCandidatesForParent(data)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def fetchUsersByDynamicSearchView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnFetchUsersByDynamicSearch(data['companyId'], data['firstId'], data['lastId'], data['type'], data['searchKey'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")


@csrf_exempt
@api_view(['GET','POST'])
def fnFetchFormFeildsForSearchView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnFetchFormFeildsForSearch(data['formName'], data['companyId'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def getUserCourseDetails4SyncView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)

    localDB = Connection(settings.MONGO_LOCAL_SERVER_ADDR,settings.MONGO_PORT)
    
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    localDBConn = localDB[settings.MONGO_DB]
    if request.method == 'POST':

        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnGetUserCourseDetails4Sync(data['userLoginIds'])
        except Exception, e:
            return Response(json.dumps(str(e), default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")