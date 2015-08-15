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
import xlsxwriter
import random
import string
from pymongo import MongoClient
from bson.objectid import ObjectId
from django.conf import settings
from django.core.mail import EmailMessage
import os
import xlrd
import os.path

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

#to load the user attendance report
@csrf_exempt
@api_view(['GET','POST'])
def FetchCandidateRegisteredReport(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseCandidateList = dbconn.system_js.fnFetchCandidateRegistrationReport(data['data'])
  
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




#to load the user attendance report for batch
@csrf_exempt
@api_view(['GET','POST'])
def fetchUserResultsView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"]
            searchKey=data['searchKey']
            testDetails=data['testDetails']
            date=data['date']
            UserResults = dbconn.system_js.fnfetchUserResultReport(companyId,searchKey,testDetails,date)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(UserResults, default=json_util.default))
    else:        
        return Response("failed")


# #to load the user attendance report for batch
# @csrf_exempt
# @api_view(['GET','POST'])
# def fetchUserResultReportView(request):  #this service will load Drafted courses
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]

#     if request.method == 'POST':
#         try:
#             stream = StringIO(request.body)
#             data = JSONParser().parse(stream)
#             companyId=data["companyId"]
#             searchKey=data['searchKey']
#             testDetails=data['testDetails']
#             date=data['date']
#             UserResults = dbconn.system_js.fnfetchUserResultReport(companyId,searchKey,testDetails,date)        
#             # Create a workbook and add a worksheet.
#             # print UserResults['userList']

#             if UserResults['userList'] != None:

#                 rand =''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))


#                 filename='userReport'+rand+'.xlsx'
#                 filepath='Reports/UserResults/'+filename
#                 workbook = xlsxwriter.Workbook('uploaded/'+filepath,{'in_memory': True})
#                 # workbook = xlsxwriter.Workbook(filename, {'tmpdir': '/home/user/tmp'})

#                 worksheet = workbook.add_worksheet()
#                 out = eval(json.dumps(UserResults['userList'], default=json_util.default))
#                 out = tuple(out)

#                 # print out

#                 # Add a bold format to use to highlight cells.
#                 bold = workbook.add_format({'bold': True})

#                 # Start from the first cell. Rows and columns are zero indexed.
#                 worksheet.write('A1', 'SL No', bold)
#                 worksheet.write('B1', 'Name', bold)
#                 worksheet.write('C1', 'College', bold)
#                 worksheet.write('D1', 'Mark', bold)
#                 worksheet.write('E1', 'Year Of Pass Out', bold)
#                 worksheet.write('F1', 'Stream', bold)



#                 row = 1
#                 col = 0

#                 # Iterate over the data and write it out row by row.
#                 for name,college,mark,year,stream in (out):
#                     worksheet.write(row, col,row)                
#                     worksheet.write(row, col+ 1,name)
#                     worksheet.write(row, col+ 2,college)
#                     worksheet.write(row, col+ 3,mark)
#                     worksheet.write(row, col+ 4,year)
#                     worksheet.write(row, col+ 5,stream)

#                     row += 1

#                 workbook.close()

#                 UserResults['filepath']=filepath
#         except ValueError:
#             return Response(json.dumps(ValueError, default=json_util.default))
#         return Response(json.dumps(UserResults, default=json_util.default))
#     else:        
#         return Response("failed")




# view for creating the detailed result report

@csrf_exempt
@api_view(['GET','POST'])
def fetchUserResultReportView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"]
            searchKey=data['searchKey']
            testDetails=data['testDetails']
            date=data['date']
            UserResults = dbconn.system_js.fnfetchUserResultReport(companyId,searchKey,testDetails,date)        
            # Create a workbook and add a worksheet.
            # print UserResults['userList']

            if UserResults['userList'] != None:

                rand =''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

                curpath = os.path.abspath(os.curdir)
                # print "Current path is: %s" % (curpath)



                filename='userReport'+rand+'.xlsx'
                filepath='Reports/UserResults/'+filename
                workbook = xlsxwriter.Workbook(curpath+'/'+settings.FILEUPLOAD_PATH+'/'+filepath,{'in_memory': True})
                # workbook = xlsxwriter.Workbook(filename, {'tmpdir': '/home/user/tmp'})

                worksheet = workbook.add_worksheet()
                out = eval(json.dumps(UserResults['userList'], default=json_util.default))
                out = tuple(out)

                # print out

                # Add a bold format to use to highlight cells.
                bold = workbook.add_format({'bold': True})

                # Start from the first cell. Rows and columns are zero indexed.
                worksheet.write('A1', 'SL No', bold)
                worksheet.write('B1', 'Name', bold)
                worksheet.write('C1', 'College', bold)
                worksheet.write('D1', 'Mark', bold)
                worksheet.write('E1', 'Year Of Pass Out', bold)
                worksheet.write('F1', 'Stream', bold)
                worksheet.write('G1', 'Branch', bold)
                worksheet.write('H1', 'mobile', bold)
                worksheet.write('I1', 'District', bold)
                worksheet.write('J1', 'Location', bold)
                worksheet.write('K1', 'PreferredWorkingLocations', bold)


                row = 1
                col = 0

                # Iterate over the data and write it out row by row.
                for name,college,mark,year,stream,branch,mobile,District,Location,PreferredWorkingLocations in (out):
                    worksheet.write(row, col,row)                
                    worksheet.write(row, col+ 1,name)
                    worksheet.write(row, col+ 2,college)
                    worksheet.write(row, col+ 3,mark)
                    worksheet.write(row, col+ 4,year)
                    worksheet.write(row, col+ 5,stream)
                    worksheet.write(row, col+ 6,branch)
                    worksheet.write(row, col+ 7,mobile)
                    worksheet.write(row, col+ 8,District)
                    worksheet.write(row, col+ 9,Location)
                    worksheet.write(row, col+ 10,PreferredWorkingLocations)

                    row += 1

                workbook.close()

                UserResults['filepath']=filepath
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(UserResults, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def fetchUsersReportBasedOnDynamicSearchView(request):  #this service fetch Users Report Based On Dynamic Search
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            result = dbconn.system_js.fnFetchUsersReportBasedOnDynamicSearch(data['companyId'], data['firstId'], data['lastId'], data['type'], data['searchKey'])
            filename = os.path.join('uploaded/Reports/UserResults/', 'userReport.xls')
            workbook = xlrd.open_workbook(filename, on_demand=True)

        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(result, default=json_util.default))
    else:        
        return Response("failed")
