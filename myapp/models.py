from django.db import models

# Create your models here.
# class Restaurant(object):
#     def __init__(self, id, name, address):
#         self.id = id
#         self.name = name
#         self.address = address

class UserMenuMapping(object):
	def __init__(self,id,fkRoleId,fkUserLoginId,fkCompanyId,fkEmployeeId,fkConsumerId,groups,createdDate,updatedDate,crmId,urmId,activeFlag):
		self.id=id
		self.fkRoleId=fkRoleId
		self.fkUserLoginId=fkUserLoginId
		self.fkCompanyId=fkCompanyId
		self.fkEmployeeId=fkEmployeeId
		self.fkConsumerId=fkConsumerId
		self.groups=groups
		self.createdDate=createdDate
		self.updatedDate=updatedDate
		self.crmId=crmId
		self.urmId=urmId
		self.activeFlag=activeFlag


# created by:Arun R Menon 
#on 07-06-14
class CompanyRegistration(object):	#model of company registration 
	def __init__(self,id,companyName,eMail,Place,Street,Phone,Mobile,userName,createdDate,updatedDate,crmId,urmId,activeFlag):
		self.id=id
		self.companyName=companyName
		self.eMail=eMail
		self.Place=Place
		self.Street=Street
		self.Phone=Phone
		self.Mobile=Mobile
		self.userName=userName
		self.createdDate=createdDate
		self.updatedDate=updatedDate
		self.crmId=crmId
		self.urmId=urmId
		self.activeFlag=activeFlag

class RegisteredCompany(object):	#model of registered Company
	def __init__(self,id,companyName,eMail,Place,Street,Phone,Mobile,userName,createdDate,updatedDate,crmId,urmId,activeFlag):
		self.id=id
		self.companyName=companyName
		self.eMail=eMail
		self.Place=Place
		self.Street=Street
		self.Phone=Phone
		self.Mobile=Mobile
		self.userName=userName
		self.createdDate=createdDate
		self.updatedDate=updatedDate
		self.crmId=crmId
		self.urmId=urmId
		self.activeFlag=activeFlag		
