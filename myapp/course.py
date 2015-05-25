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

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def saveCourseObjectView(request):  #this service will save add and update coures details
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            if len(data['courseId']) > 0:
                data['courseId'] = ObjectId(data['courseId'])

            data['courseObj']['crmId'] = ObjectId(data['courseObj']['crmId'])
            data['courseObj']['companyId'] = ObjectId(data['courseObj']['companyId'])
            data['courseObj']['urmId'] = ObjectId(data['courseObj']['urmId'])
            coureDetails=dbconn.system_js.fnAddCourseDetails(data['courseObj'],data['courseId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(coureDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def saveCourseTimelineEelementView(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            coureDetails=dbconn.system_js.fnAddCourseTimelineElement(ObjectId(data['courseId']),data['courseElement'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(coureDetails, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def removeCourseElementView(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnRemoveCourseElement(ObjectId(data['courseId']), data['courseElemName'], data['tlPoint'], data['index'], ObjectId(data['rmId']))    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def editCourseElementView(request):  #this service will add & update course elements
    #connect to our local MONGO_DB
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnEditCourseElement(ObjectId(data['courseId']), data['courseElemName'], data['tlPoint'],data['courseObj'], ObjectId(data['rmId']))    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def loadDraftedCoursesView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            draftedCourses=dbconn.system_js.fnGetDraftedCourses(ObjectId(data['cmp_id']))
        except ValueError:
            return Response(json.dumps(data, default=json_util.default))
        return Response(json.dumps(draftedCourses, default=json_util.default))
    else:        
        return Response("failed")

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def deleteDraftedCourseView(request):  #this service will delete drafted course
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            draftedCourses = dbconn.system_js.fnDeleteDraftedCourse(data['manageType'],ObjectId(data['courseId']),ObjectId(data['urmId']), data['courseType'], ObjectId(data['companyId']))
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(draftedCourses, default=json_util.default))
    else:        
        return Response("failed")

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def loadCourseDetailsView(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseDetils = dbconn.system_js.fnGetCourseDetailsById(ObjectId(data['courseId']))
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courseDetils, default=json_util.default))
    else:        
        return Response("failed")

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def SaveCourseElementFieldsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database 
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            try:
                data['element']['_id'] = ObjectId(data['element']['_id'])
                pass
            except KeyError:
                a = 1
            data['element']['crmId'] = ObjectId(data['element']['crmId'])
            data['element']['urmId'] = ObjectId(data['element']['urmId'])
            response = dbconn.system_js.fnSaveCourseElementFields(data['element'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response("failed")

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def DeleteCourseElementFieldsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database 
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)

            response = dbconn.system_js.fnDeleteCourseElementFields(ObjectId(data['elementId']), data['manageType'], ObjectId(data['urmId']))
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response("failed")

#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def GetCourseElementFieldsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database 
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            CourseElementFields = dbconn.system_js.fnGetCourseElementFields()
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(CourseElementFields, default=json_util.default))
    else:        
        return Response("failed")

#creater :Arun
@csrf_exempt
@api_view(['GET','POST'])
def FetchCourseListView(request):  #this service will load courses list 
   #connect to our local mongodb
   db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
   #get a connection to our database
   dbconn = db[settings.MONGO_DB]

   if request.method == 'POST':
       try:
           stream = StringIO(request.body)
           data = JSONParser().parse(stream)
           result = dbconn.system_js.fnfetchCourseList(data)
       except ValueError:
           return Response(json.dumps(ValueError, default=json_util.default))
       return Response(json.dumps(result, default=json_util.default))
   else:        
       return Response("failed") 

#creater :Midhun
@csrf_exempt
@api_view(['GET','POST'])
def loadPublishedCourses(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            companyId=data["companyId"]
            PublishedCourses = dbconn.system_js.fun_load_publishedCourses(companyId,data["searchKey"],data["lastId"],data["type"],data["firstId"], data['courseType'])
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(PublishedCourses, default=json_util.default))
    else:        
        return Response("failed")


#creater :Midhun
@csrf_exempt
@api_view(['GET','POST'])
def loadCourseData(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseid=data["courseid"]
            userLoginId=data["userLoginId"]
            roleid=data["roleid"]
            Courses = dbconn.system_js.fnLoadCourseData(courseid,userLoginId,roleid)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Courses, default=json_util.default))
    else:        
        return Response("failed")

#creater : Jihin
@csrf_exempt
@api_view(['GET','POST'])
def courseByKeywordsView(request):  #this service will load course suggestions
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)

            courses = dbconn.system_js.fnCourseByKeyWord(data["companyId"],data["searchKey"])   
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(courses, default=json_util.default))
    else:        
        return Response("failed")


#creater :Midhun
@csrf_exempt
@api_view(['GET','POST'])
def loadCoursesForCandidates(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseId=data["courseId"]
            Courses = dbconn.system_js.fnloadCoursesForCandidates(courseId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Courses, default=json_util.default))
    else:        
        return Response("failed")


#creater :Midhun
@csrf_exempt
@api_view(['GET','POST'])
def FetchCourseData(request):  #this service will load Drafted courses
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            courseId=data["courseId"]
            Course = dbconn.system_js.fnFetchCourseData(courseId)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(Course, default=json_util.default))
    else:        
        return Response("failed")


#created by :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def saveAnswer(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnSaveUserAnswer(ObjectId(data['courseId']),ObjectId(data['userLoginId']),data['keyName'],data['tlPointInmins'],data['outerIndex'],data['innerIndex'],data['answerObj'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))



#created by :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def ExistingMaterialsView(request):  #this service will add & update course elements
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnExistingMaterialsFetch(data)    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#created by :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def getCourseSyllabus(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnGetCourseSyllabus(data['courseId'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))


#created by :Lijin
@csrf_exempt
@api_view(['GET','POST'])
def saveMarksheetElements(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            response = dbconn.system_js.fnSaveMarksheetElements(data['courseId'],data['markSheetElements'])    
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(response, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))




#creater :jihin
@csrf_exempt
@api_view(['GET','POST'])
def  duplicateCourseView(request):  #this service will delete drafted course
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            draftedCourses = dbconn.system_js.fnDuplicateCourse(data)
        except ValueError:
            return Response(json.dumps(ValueError, default=json_util.default))
        return Response(json.dumps(draftedCourses, default=json_util.default))
    else:        
        return Response("failed")