from rest_framework import serializers
#from models import Restaurant
from models import UserMenuMapping
from models import CompanyRegistration
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
class UserMenuMappingSerializer(serializers.Serializer):

    id = serializers.CharField(required=True, max_length=50)
    fkRoleId = serializers.IntegerField(required=True)
    fkUserLoginId = serializers.IntegerField(required=True)
    fkCompanyId = serializers.IntegerField(required=True)
    fkEmployeeId = serializers.IntegerField(required=True)
    fkConsumerId = serializers.IntegerField(required=True)
    groups = serializers.CharField(required=True, max_length=800)
    createdDate = serializers.DateTimeField()
    updatedDate = serializers.DateTimeField()
    crmId = serializers.IntegerField(required=True)
    urmId = serializers.IntegerField(required=True)
    activeFlag= serializers.IntegerField(required=True)
    

    def restore_object(self, attrs, instance=None):

        if instance:
            instance.id = attrs.get('id', instance.id)
            instance.fkRoleId = attrs.get('fkRoleId', instance.fkRoleId)
            instance.fkUserLoginId = attrs.get('fkUserLoginId', instance.fkUserLoginId)
            instance.fkCompanyId = attrs.get('fkCompanyId', instance.fkCompanyId)
            instance.fkEmployeeId = attrs.get('fkEmployeeId', instance.fkEmployeeId)
            instance.fkConsumerId = attrs.get('fkConsumerId', instance.fkConsumerId)
            instance.groups = attrs.get('groups', instance.groups)
            instance.createdDate = attrs.get('createdDate', instance.createdDate)
            instance.updatedDate = attrs.get('updatedDate', instance.updatedDate)
            instance.crmId = attrs.get('crmId', instance.crmId)
            instance.urmId = attrs.get('urmId', instance.urmId)
            instance.activeFlag = attrs.get('activeFlag', instance.activeFlag)
            return instance

        return UserMenuMapping(attrs.get('id'),attrs.get('fkRoleId'),attrs.get('fkUserLoginId'),attrs.get('fkUserLoginId'),attrs.get('fkCompanyId'),attrs.get('fkEmployeeId'),attrs.get('fkConsumerId'),attrs.get('groups'),attrs.get('createdDate'),attrs.get('updatedDate'),attrs.get('crmId'),attrs.get('urmId'),attrs.get('activeFlag'))

# created by:Arun R Menon 
#on 07-06-14
class CompanyRegistrationSerializer(serializers.Serializer):  #serializer for company registration

    id = serializers.CharField(required=True, max_length=50)
    companyName = serializers.CharField(required=True, max_length=50)
    eMail = serializers.CharField(required=True, max_length=50)
    Place = serializers.CharField(required=True, max_length=50)
    Street = serializers.CharField(required=True, max_length=50)
    Phone = serializers.IntegerField(required=True)
    Mobile = serializers.IntegerField(required=True)
    userName = serializers.CharField(required=True)
    createdDate = serializers.DateTimeField()
    updatedDate = serializers.DateTimeField()
    crmId = serializers.IntegerField(required=True)
    urmId = serializers.IntegerField(required=True)
    activeFlag= serializers.IntegerField(required=True)
    

    def restore_object(self, attrs, instance=None):

        if instance:
            instance.id = attrs.get('id', instance.id)
            instance.companyName = attrs.get('companyName', instance.companyName)
            instance.eMail = attrs.get('eMail', instance.eMail)
            instance.Place = attrs.get('Place', instance.Place)
            instance.Street = attrs.get('Street', instance.Street)
            instance.Phone = attrs.get('Phone', instance.Phone)
            instance.userName = attrs.get('userName', instance.userName)
            instance.createdDate = attrs.get('createdDate', instance.createdDate)
            instance.updatedDate = attrs.get('updatedDate', instance.updatedDate)
            instance.crmId = attrs.get('crmId', instance.crmId)
            instance.urmId = attrs.get('urmId', instance.urmId)
            instance.activeFlag = attrs.get('activeFlag', instance.activeFlag)
            return instance

        return CompanyRegistration(attrs.get('id'),attrs.get('companyName'),attrs.get('eMail'),attrs.get('Place'),attrs.get('Street'),attrs.get('Phone'),attrs.get('Mobile'),attrs.get('userName'),attrs.get('createdDate'),attrs.get('updatedDate'),attrs.get('crmId'),attrs.get('urmId'),attrs.get('activeFlag'))


#custom class for encoding objectId to the json format
class MongoAwareEncoder(DjangoJSONEncoder):
    """JSON encoder class that adds support for Mongo objectids."""
    def default(self, o):
        if isinstance(o, objectid.ObjectId):
            return str(o)
        else:
            return super(MongoAwareEncoder, self).default(o)