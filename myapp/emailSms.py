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
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def sendEmailSmsNotification(request):  #this service will add & update course elements
    #connect to our local mongodb
    #db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    #dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:

            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            data['template']="A Mentee  Account has been created for you in " + data['userName']
            data['Heading'] = "Welcome to " + data['userName']
            data['user']=data['menteeName']
            #data['LOGO_PATH']=settings.LOGO_PATH
            message = get_template(settings.TEMPLATE_DIRS[0]+'/user_registration.html').render(Context(data))
            #send_mail('An account is created for you',message,settings.EMAIL_HOST_USER,[data['menteeEmail']],fail_silently=False,html_message=message)#for sending mail to mentee 
            email= EmailMessage('An account is created for you',message,settings.EMAIL_HOST_USER,[data['menteeEmail']])
            #email.attach_file(settings.LOGO_PATH+'Logo.png')
            email.content_subtype = 'html'
            email.send();
            data['user']=data['userName']
            data['template'] ="Successfullly created a mentee account for "+data['menteeName'] +" in "+ data['userName']
            message = get_template(settings.TEMPLATE_DIRS[0]+'/user_registration.html').render(Context(data))
            email= EmailMessage('New Account is registered',message,settings.EMAIL_HOST_USER,[data['userEmail']])
            email.content_subtype = 'html'
            email.send();
            #send_mail('New Account is registered',message,settings.EMAIL_HOST_USER,[data['userEmail']],fail_silently=False,html_message=message)#for sending mail to company 
            for item in data['evaluatorEmailLIst']:
                #print item['Name']
                #print item['Email']['userName']
                data['user']=item['Name']
                data['template'] ="A task has been assigned to you in "+data['userName'] 
                message = get_template(settings.TEMPLATE_DIRS[0]+'/user_registration.html').render(Context(data))
                #send_mail('A task has been Assigned to you',message,settings.EMAIL_HOST_USER,[data['menteeEmail']],fail_silently=False,html_message=message)#for sending mail to mentee 
                email= EmailMessage('A task has been Assigned to you',message,settings.EMAIL_HOST_USER,[item['Email']['userName']])
                email.content_subtype = 'html'
                email.send();
            #batchDetails=dbconn.system_js.fnAddNewBatches(data['batchObj'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(data, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadMenuNames(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
           # stream = StringIO(request.body)
            #data = JSONParser().parse(stream)
            resp=dbconn.system_js.fnLoadMenuNames()    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadMenuStates(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            resp=dbconn.system_js.fnLoadMenuStates(data['id'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def saveTemplates(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            resp=dbconn.system_js.fnSaveTemplates(data['template'])    
        except ValueError   :
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadTemplate(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
           # stream = StringIO(request.body)
            #data = JSONParser().parse(stream)
            resp=dbconn.system_js.fnLoadTemplates()    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(resp, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



