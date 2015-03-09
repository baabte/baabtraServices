from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from pymongo import Connection
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.mail import EmailMessage
from StringIO import StringIO
from rest_framework.parsers import JSONParser
import json
from bson import json_util

class FileRemove(APIView):
      parser_classes = (FileUploadParser,)


      def post(self, request, format=None):
          #db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
          #dbconn = db[settings.MONGO_DB]
          
          data = request.POST 
          filename = data['pathToBeDelete']
          slpos =filename.split('files/')
          path = default_storage.delete(settings.FILEUPLOAD_PATH+'/'+slpos[1])
          
          return Response("file has been removed")#Response(json.dumps(postdata, default=json_util.default))