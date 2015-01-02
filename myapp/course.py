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

#creater :midhun sudhakar
@csrf_exempt
@api_view(['GET','POST'])
def loadTechnologies(request):  #this service will return all the technologies available
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        try:
            technologies=dbconn.system_js.function_loadTechnologies()    
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps(technologies, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))