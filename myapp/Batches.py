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

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def saveNewBatches(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            data['batchObj']['crmId'] = ObjectId(data['batchObj']['crmId'])
            data['batchObj']['urmId'] = ObjectId(data['batchObj']['urmId'])
            data['batchObj']['companyId'] = ObjectId(data['batchObj']['companyId'])
            batchDetails=dbconn.system_js.fnAddNewBatches(data['batchObj'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadBatches(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #data['courseId']=ObjectId(data['courseId'])
            batchDetails=dbconn.system_js.fnLoadBatches(data['cmpId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadExistingCoursesUnderBatch(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            batchDetails=dbconn.system_js.fnLoadExistingCoursesUnderBatch(data['id'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def addCoursesToBatch(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            data['batch']['_id']=ObjectId(data['batch']['_id'])
            data['batch']['crmId'] = ObjectId(data['batch']['crmId'])
            data['batch']['urmId'] = ObjectId(data['batch']['urmId'])
            data['batch']['companyId'] = ObjectId(data['batch']['companyId'])
            batchDetails=dbconn.system_js.fnAddCoursesToBatch(data['batch'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
        

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def loadCourseRelatedBatches(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #data['courseId']=ObjectId(data['courseId'])
            batchDetails=dbconn.system_js.fnLoadCourseRelatedBatches(data['cmpId'],data['courseId'],data['joinDate'],data['courseType'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#function to load batches for view
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadBatchesForView(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #data['courseId']=ObjectId(data['courseId'])
            batchDetails=dbconn.system_js.fnLoadBatchesForView(data['companyId'],data['firstId'],data['type'],data['lastId'],data['searchKey'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#function to load batches for view
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesForView(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #data['courseId']=ObjectId(data['courseId'])
            batchDetails=dbconn.system_js.fnLoadMenteesForView(data['companyId'],data['firstId'],data['type'],data['lastId'],data['searchKey'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



#function to load batches for view
@csrf_exempt
@api_view(['GET','POST'])
def fnloadCourses4AssigningCourseMaterial(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #data['courseId']=ObjectId(data['courseId'])
            batchDetails=dbconn.system_js.fnloadCourses4AssigningCourseMaterial(data['companyId'],data['urmId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

@csrf_exempt
@api_view(['GET','POST'])
def fnloadCourseMaterial4multiSelect(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnLoadCourseMaterialsById(data['courseId'],data['urmId'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")


@csrf_exempt
@api_view(['GET','POST'])
def fnAssignCourseMaterial2timeline(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.funAssignCourseMaterial(data['courseId'],data['urmId'],data['courseObj'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")


@csrf_exempt
@api_view(['GET','POST'])
def fnloadBatchDetails4assignment(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnLoadBatchMenteeList(data['companyId'],data['batchMappingId'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def fnloadCourseMaterial4Batch(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnLoadCourseMaterials4Batch(ObjectId(data['batchMappingId']))
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def fnAssignCourseMaterials4Batch(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnAssignCourseMaterials4Batch(data['batchMappingId'],data['courseObj'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")

        

@csrf_exempt
@api_view(['GET','POST'])
def fnloadCoursesMaterials4menteeAtt(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnloadCoursesMaterials4menteeAtt(data['userCourseId'],data['urmId'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def fnloadCourseMaterials4batchAtt(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnloadCourseMaterials4batchAtt(data['batchMappingId'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")

@csrf_exempt
@api_view(['GET','POST'])
def fnloadMentees4batchAtt(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnloadMentees4batchAtt(data['batchMappingId'],data['batchObj'])
        
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def deleteBatch(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            batchDetails=dbconn.system_js.fnDeleteBatch(data['id'],data['cmpId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def editBatch(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            batchDetails=dbconn.system_js.fnLoadExistingCoursesUnderBatch(data['id'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: vineeth C
@csrf_exempt
@api_view(['GET','POST'])
def updateBatch(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            data['batchObj']['_id']=ObjectId(data['batchObj']['_id'])
            data['batchObj']['crmId'] = ObjectId(data['batchObj']['crmId'])
            data['batchObj']['urmId'] = ObjectId(data['batchObj']['urmId'])
            data['batchObj']['companyId'] = ObjectId(data['batchObj']['companyId'])
            # print data['batchObj']
            batchDetails=dbconn.system_js.fnUpdateBatch(data['batchObj'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: Jihin
@csrf_exempt
@api_view(['GET','POST'])
def LoadCoureBatchByBatchIdView(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            batchDetails=dbconn.system_js.fnLoadCoureBatchByBatchId(data['coureBatchId'],data['companyId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(batchDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: Jihin
@csrf_exempt
@api_view(['GET','POST'])
def saveBatchTimelineChangesView(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnSaveBatchTimelineChanges(data['coureBatchId'],data['courseTimeline'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: Jihin
@csrf_exempt
@api_view(['GET','POST'])
def LoadUserCourseDetailsView(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetails = dbconn.system_js.fnLoadUserCourseDetails(data['usersList'],data['courseId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))




#created by: Lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadBatchesByCourse(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetails = dbconn.system_js.fnLoadBatchesByCourse(data['companyId'],data['courseId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



#created by: Lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnLoadMenteesByBatch(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetails = dbconn.system_js.fnLoadMenteesByBatch(data['companyId'],data['batchMappingId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: Lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnMoveMenteeToAnotherBatch(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetails = dbconn.system_js.fnMoveMenteeToAnotherBatch(data['companyId'],data['fromBatchMappingId'],data['toBatchMappingId'],data['userMappings'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by: Lijin
@csrf_exempt
@api_view(['GET','POST'])
def fnGetUnallocatedCandidatesByCourse(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetails = dbconn.system_js.fnGetUnallocatedCandidatesByCourse(data['companyId'],data['courseId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


        

#created by: Arun
@csrf_exempt
@api_view(['GET','POST'])
def ChangeBatchStatus(request):  #this service will load batch details by batch id
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetails = dbconn.system_js.fnChangeBatchStatus(data)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
