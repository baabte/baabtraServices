from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
#created by lijin
#For applying for a job as candidate (Now it is open to all)
class FileUploadView(APIView):
      parser_classes = (FileUploadParser,)


      def post(self, request, format=None):
          file_obj = request.FILES['file']#['candidate']
          postdata=request.POST
          filename=file_obj.name.replace(' ', '')
          path = default_storage.save(settings.FILEUPLOAD_PATH+'/resume/'+filename, file_obj)
          filenameArray=path.split('/')
          actualfilename=filenameArray[len(filenameArray)-1]
          #file_move_safe(file_obj, "/tmp/new_file")
          # ...
          # do some staff with uploaded file
          # ...
          return Response(settings.RESUME_PATH+actualfilename)
      def put(self, request, filename, format=None):
          file_obj = request.FILES['file']
          # ...
          # do some staff with uploaded file
          # ...
          return Response('hai')