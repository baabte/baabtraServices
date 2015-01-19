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

class PaymentView(APIView):
      parser_classes = (FileUploadParser,)


      def post(self, request, format=None):
          db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
          dbconn = db[settings.MONGO_DB]
          postdata=request.body
          stream = StringIO(postdata)
          #data = JSONParser().parse(stream)
          #email = EmailMessage('Payment',stream, to=["jihin@baabte.com"])
          #email.content_subtype = 'html'
          #a=email.send()
          #response=dbconn.system_js.fnInsertPaymentHistory(str(postdata))
          return Response(stream)#Response(json.dumps(postdata, default=json_util.default))



#creater :jihin
# @csrf_exempt
# @api_view(['GET','POST'])
# def userRegisterationPaymentView(request):
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]

#     if request.method == 'POST':
#         try:
#             stream = StringIO(request.body)
#             #data = JSONParser().parse(stream)
#             email = EmailMessage('Payment',request.body, to=["jihin@baabte.com"])
#             email.content_subtype = 'html'
#             a=email.send()
#             #response=dbconn.system_js.fnInsertPaymentHistory(data)
#             #email = EmailMessage('Payment',StringIO(response), to=["jihin@baabte.com"])
#             #email.content_subtype = 'html'
#             #a=email.send()
               
#         except ValueError:
#             return Response(json.dumps(ValueError, default=json_util.default))
#         return Response(json.dumps("response", default=json_util.default))
#     else:        
#         return Response(json.dumps("failed", default=json_util.default))
