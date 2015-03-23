from rest_framework import serializers
#from models import Restaurant
#from models import UserMenuMapping
#from models import CompanyRegistration
from django.core.serializers.json import DjangoJSONEncoder
from bson import objectid
# class RestaurantSerializer(serializers.Serializer):
#     id = serializers.CharField(required=True, max_length=50)
#     name = serializers.CharField(required=True, max_length=100)
#     address = serializers.CharField(required=False, max_length=200)

#     def restore_object(self, attrs, instance=None):
#         if instance:
#             instance.id = attrs.get('id', instance.id)
#             instance.name = attrs.get('name', instance.name)
#             instance.address = attrs.get('address', instance.address)
#             return instance

#         return Restaurant(attrs.get('id'),attrs.get('name'),attrs.get('address'))

#custom class for encoding objectId to the json format
class MongoAwareEncoder(DjangoJSONEncoder):
    """JSON encoder class that adds support for Mongo objectids."""
    def default(self, o):
        if isinstance(o, objectid.ObjectId):
            return str(o)
        else:
            return super(MongoAwareEncoder, self).default(o)