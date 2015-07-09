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

#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def addEvaluator(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            insertResp=dbconn.system_js.fnaddEvaluator(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(insertResp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def GenerateCode(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            insertResp=dbconn.system_js.fnaddGeneratedCode(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(insertResp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def retrieveExistingConf(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["comapanyId"]
            Resp=dbconn.system_js.fnretrieveExistingGlobalConf(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def removeExistingEvaluator(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnremoveExistingEvaluator(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def removeItemFromAgroup(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnremoveItemFormAgroup(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def updateExistingPrefix(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnupdateExistingPrefix(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def setSupervisors(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnsetSupervisors(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

        
#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def removeExistingSupervisors(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnremoveExistingSupervisors(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



       
#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def setMenuType(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnsetMenuType(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



       
#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def saveMenuColor(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnmenuColor(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


       
#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def saveSubMenuAndBackgrounds(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnchangeSubTitleandBack(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



       
#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def saveAttendanceAlertSettings(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnsaveAttendanceAlertSettings(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))




       
#creater :Midhun Sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def setOrderFormConfOrNot(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            datas = data["data"]
            Resp=dbconn.system_js.fnsetOrderFormConfOrNot(datas)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#created by Lijin on 20-5-2015 for updating company candidate age limit globally
@csrf_exempt
@api_view(['GET','POST'])
def fnUpdateCandidateAgeLimit(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            # data = data["data"]
            Resp=dbconn.system_js.fnUpdateCandidateAgeLimit(data['comapanyId'],data['candidateAgeLimit'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#created by Lijin on 8-5-2015 for fetching notification configuration
@csrf_exempt
@api_view(['GET','POST'])
def fnGetNotificationConfig(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            # data = data["data"]
            Resp=dbconn.system_js.fnGetNotificationConfig(data['companyId'],data['configType'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#created by Lijin on 8-5-2015 for fetching notification configuration
@csrf_exempt
@api_view(['GET','POST'])
def fnUpdateNotificationConfig(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            # data = data["data"]
            Resp=dbconn.system_js.fnUpdateNotificationConfig(data['companyId'],data['rmId'],data['config'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
