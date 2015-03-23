from rest_framework import serializers
# from models import Restaurant
# from models import UserMenuMapping
# from models import CompanyRegistration
from django.core.serializers.json import DjangoJSONEncoder
from bson import objectid


#custom class for encoding objectId to the json format
class MongoAwareEncoder(DjangoJSONEncoder):
    """JSON encoder class that adds support for Mongo objectids."""
    def default(self, o):
        if isinstance(o, objectid.ObjectId):
            return str(o)
        else:
            return super(MongoAwareEncoder, self).default(o)