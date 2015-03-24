from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from pymongo import Connection
import json
from bson import json_util
from StringIO import StringIO
from rest_framework.parsers import JSONParser
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
from django.core.mail import EmailMessage
import xlrd
from xlrd import open_workbook,error_text_from_code
import os
import tempfile
import random
import string
import datetime
import dateutil
import dateutil.parser as parser
from dateutil import parser as date_parser
#service function for bulk enrollment

@csrf_exempt  
@api_view(['GET','POST'])
def fnBulkEnroll(request):
	input_file=request.FILES['file']
	#connect to our local mongodb
	db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
	#get a connection to our database
	dbconn = db[settings.MONGO_DB]
	
	fd, tmp = tempfile.mkstemp()
	try:
		#stream = StringIO(request.POST)
		data = request.POST#JSONParser().parse(stream) 
	      
		#fd, tmp = tempfile.mkstemp()
		with os.fdopen(fd, 'w') as out:
			out.write(input_file.read())
		wb = xlrd.open_workbook(tmp)
		# do what you have to do
		values=[]
		ObjList=[]
		#data['mandatoryData']={}
		for s in wb.sheets():
			#print 'Sheet:',s.name
			
			for row in range(1, s.nrows):
				dataObj={}
				#dataObj=data;
				#print(data['batch']['batchName']);
				streambatch = StringIO(data['batch'])
				streamcourse = StringIO(data['course'])
				streamrole = StringIO(data['role'])
				streameval =StringIO(data['evaluator'])
				dataObj['batch']=JSONParser().parse(streambatch)
				dataObj['role']=JSONParser().parse(streamrole)
				dataObj['course']=JSONParser().parse(streamcourse)
				dataObj['loggedusercrmid']=data['loggedusercrmid']
				dataObj['companyId']=data['companyId']
				dataObj['batchId']=data['batchId']
				dataObj['evaluator']=data['evaluator']   
				#dataObj['mandatoryData']={}
				col_names = s.row(0)
				col_value = []
				mandatoryData={}
				result={}
				if (s.nrows-1 > dataObj['batch']['seats']) :
					result['data']=1
					result['totalRows']	=s.nrows-1
					result['seats']	= dataObj['batch']['seats']			 
				else: 
					#randomCourse=['54c85c28ef14f722f489060f', '54d8b364ef14f722f48907b2', '54d5e6c8ef14f722f489076e', '54d94e5bef14f722f48907f9', '54d951aeef14f722f48907fa']
					for name, col in zip(col_names, range(s.ncols)):
						value  = (s.cell(row,col).value)
						try : value = str(int(value))
						except : pass
						col_value.append((name.value, value))
						ident=name.value
						mandatoryData[name.value]=value
						mandatoryData['password']=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
						#print(mandatoryData)
						json_size = len(mandatoryData)					
						if json_size == 3 :
							dt=datetime.datetime.strptime(value,'%d/%m/%Y').date() 				#coverting date format
							date=(parser.parse(datetime.date.strftime(dt, "%a %b %d %Y 00:00:00 GMT+0530 (IST)")))   #converting to datetime format
							mandatoryData[name.value]= date.isoformat()
							#if json_size == 6 :
							#dt=datetime.datetime.strptime(value,'%d/%m/%Y').date() 				#coverting date format
							#dataObj[name.value]=datetime.date.strftime(dt, "%a %b %d %Y 00:00:00 GMT+0530 (IST)")   #converting to datetime format
						if json_size == 4 :	
							mandatoryData[name.value]=value	
						if json_size == 5 :	
							mandatoryData[name.value]=value	
							#dataObj['course']={}
							#dataObj['course']['_id']=value#random.choice(randomCourse)
							#dataObj['mandatoryData']=mandatoryData
							#dataObj=json.load(dataObj)
							dataObj['mandatoryData']=mandatoryData
							
							result = dbconn.system_js.fnRegisterUser(dataObj);
			ObjList.append(json.dumps(result, default=json_util.default))
	finally:
		os.unlink(tmp)  # delete the temp file no matter what
	return Response(ObjList)

#created by Arun.R.Menon
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadUserReport(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnLoadUserReport(data);
        print(data)
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")   


@csrf_exempt  
@api_view(['GET','POST'])
def fnBulkEnrollavailable(request):
	input_file=request.FILES['file']
	#connect to our local mongodb
	db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
	#get a connection to our database
	dbconn = db[settings.MONGO_DB]
	
	fd, tmp = tempfile.mkstemp()
	try:
		#stream = StringIO(request.POST)
		data = request.POST#JSONParser().parse(stream) 
	      
		#fd, tmp = tempfile.mkstemp()
		with os.fdopen(fd, 'w') as out:
			out.write(input_file.read())
		wb = xlrd.open_workbook(tmp)
		# do what you have to do
		values=[]
		ObjList=[]
		#data['mandatoryData']={}
		for s in wb.sheets():
			#print 'Sheet:',s.name
			
			for row in range(1, int(data['seats'])):
				dataObj={}
				#dataObj=data;
				#print(data['batch']['batchName']);
				streambatch = StringIO(data['batch'])
				streamcourse = StringIO(data['course'])
				streamrole = StringIO(data['role'])
				streameval =StringIO(data['evaluator'])
				dataObj['batch']=JSONParser().parse(streambatch)
				dataObj['role']=JSONParser().parse(streamrole)
				dataObj['course']=JSONParser().parse(streamcourse)
				dataObj['loggedusercrmid']=data['loggedusercrmid']
				dataObj['companyId']=data['companyId']
				dataObj['batchId']=data['batchId']
				dataObj['evaluator']=data['evaluator']   
				#dataObj['mandatoryData']={}
				col_names = s.row(0)
				col_value = []
				mandatoryData={}
				result={} 
					#randomCourse=['54c85c28ef14f722f489060f', '54d8b364ef14f722f48907b2', '54d5e6c8ef14f722f489076e', '54d94e5bef14f722f48907f9', '54d951aeef14f722f48907fa']
				for name, col in zip(col_names, range(s.ncols)):
					value  = (s.cell(row,col).value)
					try : value = str(int(value))
					except : pass
					col_value.append((name.value, value))
					ident=name.value
					mandatoryData[name.value]=value
					mandatoryData['password']=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
					#print(mandatoryData)
					json_size = len(mandatoryData)					
					if json_size == 3 :
						dt=datetime.datetime.strptime(value,'%d/%m/%Y').date() 				#coverting date format
						date=(parser.parse(datetime.date.strftime(dt, "%a %b %d %Y 00:00:00 GMT+0530 (IST)")))   #converting to datetime format
						mandatoryData[name.value]= date.isoformat()
						#dataObj['mandatoryData']=mandatoryData
					if json_size == 4 :	
							mandatoryData[name.value]=value	
					if json_size == 5 :	
						mandatoryData[name.value]=value		
						#print(dataObj['mandatoryData'])
						dataObj['mandatoryData']=mandatoryData
						result=dbconn.system_js.fnRegisterUser(dataObj);
			ObjList.append(json.dumps(result, default=json_util.default))
	finally:
		os.unlink(tmp)  # delete the temp file no matter what
	return Response(ObjList)
