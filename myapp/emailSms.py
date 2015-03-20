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
from django.core.mail import send_mail
import requests
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def sendEmailSmsNotification(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #print(data['phone'])
            #print(data['email'])
            #print(data['senderId'])
            #print(data['smsKey'])
            payload = {'workingkey':data['smsKey'],'method':'sms','sender':data['senderId'],'to':data['phone'],'message':"testing sms sending"}
            resp=requests.get(settings.EBENSMSURL,params=payload)
            #send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
            send_mail('Welcome to Baabtra.com','Your account is registered in baabtra.com',settings.EMAIL_HOST_USER,[data['email']],fail_silently=False) 
            #print(resp_email);
            #batchDetails=dbconn.system_js.fnAddNewBatches(data['batchObj'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(resp_email, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
