#---------------------------
#Sample service
#created by : Akshath kumar M
#Created on : 04-10-14
#-----------------------------

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import Connection
#from models import UserMenuMapping
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
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template

@csrf_exempt  
@api_view(['GET','POST'])
def InsertUserMenu(request):
    def test(menu,sub):
        if sub == None:
            sub=0
        if sub<len(menu):
            if 'fkMenuId' in menu[sub]:
                menu[sub]['fkMenuId']=ObjectId(menu[sub]['fkMenuId'])
                pass
            if 'childMenuStructure' in menu[sub]:    
                if len(menu[sub]['childMenuStructure'])>0:
                    test(menu[sub]['childMenuStructure'],None)
                    pass
                pass
            sub=sub+1
            test(menu,sub)
            pass                                   #for Inserting menu items for specific user
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    clnUserMenuMapping = dbconn['clnUserMenuMapping']

    if request.method == 'GET':
        #get our collection
        UserMenuMappingList = []
        
        docs_list  = list(clnUserMenuMapping.find())
        return Response(json.dumps(docs_list, default=json_util.default))
    elif request.method == 'POST':   #for post request
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        #data["fkMenuId"]=ObjectId(data["fkMenuId"])
        test(data["menus"],None)
        try:
            docs_list  = dbconn.system_js.fnSaveUserMenus(ObjectId(data['fkUrmId']),ObjectId(data["fkUserRoleMappingId"]),ObjectId(data["fkMenuRegionId"]),data["menus"]) 
        except:
            return Response(request.body)
        return Response(StringIO(docs_list))

@csrf_exempt  
@api_view(['GET','POST'])
def UserRoleMenuMappingView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    userMenuCollection = dbconn['tblUserMenuMapping']

    if request.method == 'GET':
        #get our collection
        UserMenuMappingList = []
        docs_list  = list(userMenuCollection.find())
        #return Response(json.dumps(docs_list, default=json_util.default))
        #for r in userMenuCollection.find():
        #    UserMenuMappingView = UserMenuMapping(r["_id"],r['fkRoleId'],r['fkUserLoginId'],r['fkCompanyId'],r['fkEmployeeId'],r['fkConsumerId'],r['groups'],r['createdDate'],r['updatedDate'],r['crmId'],r['urmId'],r['activeFlag'])
        #    UserMenuMappingList.append(UserMenuMappingView)
        #serializedList = UserMenuMappingSerializer(UserMenuMappingList, many=True)
        
        return Response(json.dumps(docs_list, default=json_util.default))
    elif request.method == 'POST':
        #get data from the request and insert the record
        #received_json_data=json.loads(request.body)
        #name = request.POST["_content"]
        #address = 'calicut' #request.POST["address"]
        try:
            userMenuCollection.insert({"fkUserRoleMappingId":100,"menuStructure": [{"fkmenuRegionId": 1,"regionMenuStructure": [{"fkMenuId": 1,"MenuName": "sample","MenuIcon": "fa_users","childMenuStructure": [{ }] }] }],"createdDate": datetime.now(),"updatedDate": datetime.now(),"crmId": 111,"urmId": 111,"activeFlag": 1})
        except:
            return Response(response.POST)
        #for r in restaurantCollection.find():
        #    restaurant = Restaurant(r["_id"],r["name"],r["address"])
        #    restaurants.append(restaurant)
        #serializedList = RestaurantSerializer(restaurants, many=True)
        return Response({"result":"success"})

@csrf_exempt  
@api_view(['GET','POST'])
def FnGetCompanyDetailsView(request):
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    stream = StringIO(request.body)
    data = JSONParser().parse(stream)
    if request.method == 'POST':
        try:
            docs_list  = dbconn.system_js.fnGetCompanyDetails(data['roleId'],data['companyId'],data['range'],data['prefix']);
        except:
            return Response(request.body)
        return Response(json.dumps(docs_list, default=json_util.default))
    else:
        return Response(docs_list)       
# #created by Arun.R.Menon
# #on 07-10-14
# @csrf_exempt
# @api_view(['GET','POST'])
# def CompanyRegistrationView(request):
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]
#     #companyCollection = dbconn['clnCompany']
#     #userloginCollection = dbconn['clnUserLogin']
#     if request.method == 'POST':      
#         stream = StringIO(request.body)
#         data = JSONParser().parse(stream)
#         data['fksectorId']=ObjectId(data['fksectorId'])
#         data['fkcountryId']=ObjectId(data['fkcountryId'])
#         data['fkstateId']=ObjectId(data['fkstateId'])
#         data['fkdistrictId']=ObjectId(data['fkdistrictId'])
#         data['loggedusercrmid']=data['loggedusercrmid']
#         result = dbconn.system_js.fnComRegInsert(data);
#         email=result.get('cmail')
#         email = EmailMessage('Company Registered','Welcome to baabtra.com', to=[email])
#         email.send()
#         return Response(json.dumps(result, default=json_util.default))
#     else:        
#         return Response("failure")


#START===============================================================JIHIN RAJU===================================================================

#created by JIHIN RAJU
#on 07-10-14
@csrf_exempt  
@api_view(['GET','POST'])
def GetAllRolesView(request):#for get all the roles based on company_id
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)#reads the data passed along with the request
        data = JSONParser().parse(stream)#converts to json
        try:
            docs_list  = dbconn.system_js.fnGetAllRoles(data['rm_id'],ObjectId(data['cmp_id']),data['range'],data['roleVal']);
        except:
            return Response(request.body)    
        return Response(json.dumps(docs_list, default=json_util.default)) #dumps corresponding data in the response
    else:
        return Response(docs_list)

#created by JIHIN RAJU
#on 26-11-14
@csrf_exempt  
@api_view(['GET','POST'])
def FnLoadTopLevelRolesView(request):#for get all the roles based on company_id
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        #stream = StringIO(request.body)#reads the data passed along with the request
        #data = JSONParser().parse(stream)#converts to json
        try:
            docs_list  = dbconn.system_js.fnLoadTopLevelRoles();
        except:
            return Response(request.body)    
        return Response(json.dumps(docs_list, default=json_util.default)) #dumps corresponding data in the response
    else:
        return Response(docs_list)        

#created by JIHIN RAJU 
#on 07-10-14
@csrf_exempt  
@api_view(['GET','POST'])
def GetRoleMenusView(request):#for get all menus of selected user
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)#reads the data passed along with the request
        data = JSONParser().parse(stream)#converts to json
        try:
            docs_list  = dbconn.system_js.fnGetCurrentMenusById(data['fkRoleId'],data['type']);
        except:
            return Response(request.body)
        return Response(json.dumps(docs_list, default=json_util.default,sort_keys=True)) #dumps corresponding data in the response
    else:
        return Response(request.body)

#created by JIHIN RAJU
#on 07-10-14
@csrf_exempt  
@api_view(['GET','POST'])
def GetAllMenusView(request):#for get all menus of loged user
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    stream = StringIO(request.body)#reads the data passed along with the request
    data = JSONParser().parse(stream)#converts to json
    if request.method == 'POST':
        try:
            docs_list  = dbconn.system_js.fnGetCurrentMenusById(ObjectId(data['rm_id']),data['type']);
        except:
            return Response(request.body)
        return Response(json.dumps(docs_list, default=json_util.default,sort_keys=True)) #dumps corresponding data in the response
    else:
        return Response(request.body)

#created by JIHIN RAJU
#on 05-11-14
@csrf_exempt  
@api_view(['GET','POST'])
def FnGetCompanyDetailsJiView(request):#for get company details
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    stream = StringIO(request.body)#reads the data passed along with the request
    data = JSONParser().parse(stream)#converts to json
    if request.method == 'POST':
        try:
            docs_list  = dbconn.system_js.fnGetCompanyDetailsJi(data['range'],data['cmp_name']);
        except:
            return Response(request.body)
        return Response(json.dumps(docs_list, default=json_util.default)) #dumps corresponding data in the response
    else:
        return Response(docs_list)

#created by JIHIN RAJU
#on 07-10-14
@csrf_exempt  
@api_view(['GET','POST'])
def SaveNewRoleMenu(request): #for Insert or update menu items for specific user and role
    def test(menu,sub):
        if sub == None:
            sub=0
        if sub<len(menu):
            if 'fkMenuId' in menu[sub]:
                menu[sub]['fkMenuId']=ObjectId(menu[sub]['fkMenuId'])
                del menu[sub]['actionMaster']
                if 'actionStatus' in menu[sub]:
                    del menu[sub]['actionStatus']
                    pass
                pass
            if 'childMenuStructure' in menu[sub]:    
                if len(menu[sub]['childMenuStructure'])>0:
                    test(menu[sub]['childMenuStructure'],None)
                    pass
                pass
            sub=sub+1
            test(menu,sub)
            pass
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)#reads the data passed along with the request
        data = JSONParser().parse(stream)#converts to json
        response=""
        
        test(data["menus"],None)

        if response=="":
            try:            
                response=dbconn.system_js.fnSaveUserMenuMapping(data['rm_id'],data['role_id'],data['menus']); 
                response=dbconn.system_js.fnSaveRoleMenuMapping(data['rm_id'],data['role_id'],data['menus']);
            except:
                return Response(json.dumps("", default=json_util.default))
        pass
        return Response(StringIO(response))
    else:
        return Response(request.body)

#END===============================================================JIHIN RAJU=========================================================================
     
#------------------------------
#created by anu
#---------------------------
@csrf_exempt  
@api_view(['GET','POST'])
def GetMenuItems(request):                #for Inserting menu items for specific user
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    userMenuCollection = dbconn['clnUserMenuMapping']
    if request.method == 'GET':
        #get our collection
        UserMenuMappingList = []
        docs_list  = list(userMenuCollection.find())
        return Response({"name":"success"})      
    elif request.method == 'POST':
        stream = StringIO(request.body)  #reads the data passed along with the request
        data = JSONParser().parse(stream)   #converts to json
        docs_list  = dbconn.system_js.fnGetMenuItemsById(ObjectId(data['fkUserRoleMappingId'])); #calls the stored js function to find the corresponding menu

        try:
            return Response(json.dumps(docs_list, default=json_util.default)) #dumps corresponding data in the response
        except:
            return Response(json.dumps("", default=json_util.default))
       
        return Response(json.dumps(docs_list, default=json_util.default));

#-----------------------------


@csrf_exempt  
@api_view(['GET','POST'])
def LoadUsers(request): #Loading All the users based on compny id supplied
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        try:
            docs_list  = dbconn.system_js.fnSearchUsers(data['companyId'],data['prefix'],data["range"]);
        except:
            return Response(json.dumps("", default=json_util.default))
        return Response(json.dumps(docs_list, default=json_util.default)) #return the response here
    else:
        return Response("")

@csrf_exempt  
@api_view(['GET','POST'])
def LoadExMenuItems4AUMMapping(request): #Loading the existing user menu items
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        try:
            docs_list  = dbconn.system_js.fnLoadExMenusForUsers(data['fkUserRoleMappingId'],data['companyId'],data['roleId']);
        except:
            return Response(json.dumps("", default=json_util.default))
        return Response(json.dumps(docs_list, default=json_util.default))
    else:
        return Response("Get") #dbconn.system_js.myAddFunction(2,2)
@csrf_exempt  
@api_view(['GET','POST'])
def LoadMenuItems4AUMMapping(request): #Loding the Menu items for adding specific user
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    clnRoleMenuMapping = dbconn['clnRoleMenuMapping']

    if request.method == 'POST':

        try:
            stream = StringIO(request.body)
            data = JSONParser().parse(stream)
            #data['fkRoleId']=ObjectId(data['fkRoleId'])
            docs_list  = dbconn.system_js.fnGetCurrentRoleMenus(data['fkRoleId']);            
        except:
            return Response(json.dumps("", default=json_util.default))
        return Response(json.dumps(docs_list, default=json_util.default))
    else:
        return Response({"result":"success"})


    

##created by Arun.R.Menon
#on 09-10-14
@csrf_exempt
@api_view(['GET','POST'])
def RegisteredCompanyView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    #companyCollection = dbconn['clnCompany']

    if request.method == 'POST':
        #get our collection
        try:
            companyList=dbconn.system_js.fnViewRegisteredCompany()
        except:
            return Response("error")
        return Response(json.dumps(companyList, default=json_util.default))
    else:        
        return Response("failure")

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def CompanySectorView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    sectorCollection = dbconn['clnSectors']

    if request.method == 'POST':
        #get our collection
        docs_list  = list(sectorCollection.find())
        return Response(json.dumps(docs_list, default=json_util.default))
    else:    
        return Response("failure")


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def CountryStateDistrictView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    CountryStateDistrictCollection = dbconn['clnCountryStateDistrict']

    if request.method == 'POST':
        #get our collection
        
        docs_list  = list(CountryStateDistrictCollection.find())
        return Response(json.dumps(docs_list, default=json_util.default))
    else:    
        return Response("failure")

# #created by midhun sudhakar
# #on 13-10-14
# @csrf_exempt  
# @api_view(['GET','POST'])
# def Login(request):
#     #connect to our local mongodb
#         db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#         #get a connection to our database
#         dbconn = db[settings.MONGO_DB]
#         if request.method == 'POST':
#             stream =StringIO(request.body)
#             data = JSONParser().parse(stream) 
#             LoginData=data["loginData"]
#             try:
                
#                 x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#                 if x_forwarded_for:
#                     real_ip = x_forwarded_for.split(',')[0]
#                 else:
#                     real_ip = request.META.get('REMOTE_ADDR')
#                 LoginData['ip']=real_ip
#                 log = dbconn.system_js.fnLogin(LoginData);
#             except Exception as e:
#                 return Response(str(e))
#             return Response(json.dumps(log, default=json_util.default))
#         else:    
#             return Response("failure")
           


#created by MIDHUN SUDHAKAR
#on 10-10-14
@csrf_exempt  
@api_view(['GET','POST'])
def ManageRolesOfCompany(request): #this webservice add roles of particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)    #get a connection to our database
    dbconn =db[settings.MONGO_DB]
    if request.method == 'POST':
        #docs_list  = list(userMenuCollection.find({"fkRoleId":ObjectId("542d498fcf19c1514235f69d")}))
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        roles=data['roles']
        try:
            dbconn.system_js.fun_add_new_roles(roles);
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps("success", default=json_util.default))
    else:
        return Response(json.dumps("failed", default=json_util.default))  
#created by MIDHUN SUDHAKAR
#on 12-10-14

@csrf_exempt
@api_view(['GET','POST'])
def ManageRolesOfCompanyView(request):  #this service will retrieve all roles of particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        userdata=data["userdata"]
        try:
            rolls=dbconn.system_js.function_retriveCompany_Roles(userdata)    
        except:
            return Response(json.dumps("error", default=json_util.default))
        # return Response(json.dumps(rolls, default=json_util.default))
        return Response(json.dumps(rolls, default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))
#created by MIDHUN SUDHAKAR
#on 16-10-14

@csrf_exempt
@api_view(['GET','POST'])
def UpdateCompanyRole(request):  #this service will update all roles of particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        RoleId=data["_id"]
        role=data["role"]
        data=data["data"]
        try:
            dbconn.system_js.fun_update_company_role(RoleId,role,data)
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps("success", default=json_util.default))
    else:
         return Response(json.dumps("failed", default=json_util.default)) 


#created by MIDHUN SUDHAKAR
#on 16-10-14

@csrf_exempt
@api_view(['GET','POST'])
def DeleteCompanyRole(request):  #this service will change active flag of role of a particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    CompanyRoles = dbconn['ClnRoleMaster']  #ClnRoleMaster is the collection that stores roles

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        try:
            dbconn.system_js.fun_delete_company_role(data)    
        except:
            return Response(json.dumps("error", default=json_util.default))
        return Response(json.dumps("success", default=json_util.default))
    else:        
        return Response(json.dumps("failed", default=json_util.default))

#created by Arun.R.Menon
#to delete a company
@csrf_exempt
@api_view(['GET','POST'])
def CompanyDeleteView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        dbconn.system_js.fnDeleteCompany(data);
        return Response("success")
    else:    
        return Response("failure")

#created by Arun.R.Menon
#to delete a company
@csrf_exempt
@api_view(['GET','POST'])
def CompanyEditView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    companyCollection = dbconn['clnCompany']

    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        dbconn.system_js.fnEditCompany(data);
        return Response("success")
    else:    
        return Response("failure")


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def UserNameValidView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    UserLoginCollection = dbconn['clnUserLogin']

    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnUserNameValid(data);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")

#created by midhun
#on 22-10-14
# @csrf_exempt
# @api_view(['GET','POST'])
# def show_more_company_role(request):  #this service will change active flag of role of a particular company
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]
    
#     if request.method == 'POST':
#         stream = StringIO(request.body)
#         data = JSONParser().parse(stream) 
#         showtime=data["showtime"]
#         companyId=data["companyId"]       
#         try:
#             maore_roles=dbconn.system_js.fn_show_more_roles(companyId,showtime)
#         except:
#             return Response("error")
#         return Response(json.dumps(maore_roles, default=json_util.default))
#     else:
#         return Response("failed")
        
#---------------------------------------------------------------------
#created by  : Akshath kumar M.
#created date: 24-10-14
#Description : getting the user details for reporting.   
#---------------------------------------------------------------------      
@csrf_exempt
@api_view(['GET','POST'])
def getRptUserDetails(request):  #this service will change active flag of role of a particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream) 
        userRoleMappingId=data["userRoleMappingId"]       
        try:
            role=dbconn.system_js.fnGetRptUserDetails(userRoleMappingId)
        except:
            return Response("error")
        return Response(json.dumps(role, default=json_util.default))

#created by Arun
#on 22-10-14
@csrf_exempt
@api_view(['GET','POST'])
def showMoreCompaniesView(request):  #this service will change active flag of role of a particular company
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':
        stream = StringIO(request.body)
        data = JSONParser().parse(stream) 
        showtime=data["showtime"]       
        try:
            company=dbconn.system_js.fnShowMoreCompany(showtime)
        except:
            return Response("error")
        return Response(json.dumps(company, default=json_util.default))
    else:        
        return Response("failure")

#created by midhun
#on 22-10-14
# @csrf_exempt
# @api_view(['GET','POST'])
# def find_company_id(request):  #this service will find the company id of current session
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]
    
#     if request.method == 'POST':
#         stream = StringIO(request.body)
#         data = JSONParser().parse(stream) 
#         fkUserLoginId=data["fkUserLoginId"]
#         try:
#             role=dbconn.system_js.fun_companyid_mappings(fkUserLoginId)
#             cmpid=role.get('fkCompanyId')
#         except:
#             return Response("error")
#         return Response(json.dumps(cmpid, default=json_util.default))
#     else:        
#         return Response("failed")
#created by suhail pallimalil
#on 22-10-14
@csrf_exempt
@api_view(['GET','POST'])
def EmailAlreadyRegisterdorNot(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    UserLoginCollection = dbconn['clnUserLogin']

    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnCheckEmailExist(data['email'],data['fbId']);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")

@csrf_exempt
@api_view(['GET','POST'])
def LinkAccountWithFacebook(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    UserLoginCollection = dbconn['clnUserLogin']

    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnLinkwithFacebook(data);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")        


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def SelectedCompanyView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnSelectedCompany(data);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")   

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def SearchCompanyView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnSearchCompany(data);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")   

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def GetUserPlanView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnGetUserPlan(data);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")   

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def GetPlansView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        result = dbconn.system_js.fnGetPlans();
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")   


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def GetFeaturesView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnGetFeatures(data);
        return Response(json.dumps(result, default=json_util.default))            
    else:        
        return Response("failure")   

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def ChangeUserPlanView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result = dbconn.system_js.fnChangeUserPlan(data)
        return Response(json.dumps(result, default=json_util.default))               
    else:        
        return Response("failure")   

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def EditPricingView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        dbconn.system_js.fnEditPricing(data);
        return Response("success")            
    else:        
        return Response("failure")                                            


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def AddFeatureView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnAddFeature(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")   


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def DeleteFeatureView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnDeleteFeature(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")            

        

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def EditBillingView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnEditBilling(data);
        # return Response(json.dumps(result, default=json_util.default))  
        return Response("success")            
    else:        
        return Response("failure")  


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def GetFeaturesConfigView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnGetFeaturesConfig(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")          

# #created by midhun sudhakar
# #on 13-10-14
# @csrf_exempt
# @api_view(['GET','POST'])
# def loadlogUserdata(request):
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]
    
#     if request.method == 'POST':      
#         stream = StringIO(request.body)
#         data = JSONParser().parse(stream)
#         UserDataObjId=data["UserDataObjId"]
#         try:
#            result=dbconn.system_js.fun_load_log_user_data(UserDataObjId)    
#         except:
#            return Response(json.dumps("error", default=json_util.default))
#         return Response(json.dumps(result, default=json_util.default))
#     else:        
#         return Response(json.dumps("failed", default=json_util.default))

# @csrf_exempt
# @api_view(['GET','POST'])
# def logout(request):
#     #connect to our local mongodb
#     db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
#     #get a connection to our database
#     dbconn = db[settings.MONGO_DB]
    
#     if request.method == 'POST':      
#         stream = StringIO(request.body)
#         data = JSONParser().parse(stream)
#         UserLogoutObjId=data["UserLogoutObjId"]
#         try:
#            result=dbconn.system_js.fun_logout(UserLogoutObjId)    
#         except:
#            return Response(json.dumps("error", default=json_util.default))
#         return Response(json.dumps("success", default=json_util.default))
#     else:        
#         return Response(json.dumps("failed", default=json_util.default))
         



#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def SaveFeaturesConfigView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnSaveFeaturesConfig(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")        

        

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def GetFeaturesConfigValues(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnGetFeaturesConfigValues(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")          


#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def GetExitCriteriaView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        result =dbconn.system_js.fnGetExitCriteria();
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")           
        

#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def SaveCourseElementFormView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnSaveCourseElementForm(data);
        # return Response(json.dumps(result, default=json_util.default))  
        return Response("success")            
    else:        
        return Response("failure")                  


#created by midhun sudhakar
#on 31-12-2014
@csrf_exempt
@api_view(['GET','POST'])
def forgotPassword(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        user_email=data["user_email"]
        try:
            userdata=dbconn.system_js.fun_check_user_email_exists(user_email);
            if userdata["result"]>0:
                data = {
                'username': userdata["userdata"]["userName"],
                'password': userdata["userdata"]["password"]
                }
                message = get_template(settings.TEMPLATE_DIRS[0]+'/forgot_password.html').render(Context(data))
                email = EmailMessage('baabtra.com accont password',message, to=[userdata["userdata"]["userName"]])
                email.content_subtype = 'html'
                a=email.send()
                return Response(json.dumps("success", default=json_util.default))
            else:
                return Response(json.dumps("no_username", default=json_util.default))
        except :
           return Response(json.dumps("error", default=json_util.default))
        
    else:        
        return Response(json.dumps("failed", default=json_util.default))  




#created by Arun.R.Menon
@csrf_exempt
@api_view(['GET','POST'])
def GetCourseElementsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    stream = StringIO(request.body)
    data = JSONParser().parse(stream)
    if request.method == 'POST':      
        result =dbconn.system_js.fnGetCourseElements(data['courseElementName']);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")  


#created by Arun.R.Menon
@csrf_exempt
@api_view(['GET','POST'])
def DeleteCourseElementView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result =dbconn.system_js.fnDeleteCourseElement(data);
        # return Response(json.dumps(result, default=json_util.default))  
        return Response("success")            
    else:        
        return Response("failure")  



#created by Arun.R.Menon
#on 13-10-14
@csrf_exempt
@api_view(['GET','POST'])
def SaveExitCriteriaView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':      
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)
        result =dbconn.system_js.fnSaveExitCriteria(data);
        # return Response(json.dumps(result, default=json_util.default))  
        return Response("success")            
    else:        
        return Response("failure")             


#created by Arun.R.Menon
@csrf_exempt
@api_view(['GET','POST'])
def DeleteExitCriteriaView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result =dbconn.system_js.fnDeleteExitCriteria(data);
        # return Response(json.dumps(result, default=json_util.default))  
        return Response("success")            
    else:        
        return Response("failure")       

#created by Arun.R.Menon
@csrf_exempt
@api_view(['GET','POST'])
def RegisterUserView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnRegisterUser(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")                 


#created by Arun.R.Menon
@csrf_exempt
@api_view(['GET','POST'])
def FetchUserDetailsView(request):
    #connect to our local mongodb
    db = Connection(settings.MONGO_SERVER_ADDR,settings.MONGO_PORT)
    #get a connection to our database
    dbconn = db[settings.MONGO_DB]
    
    if request.method == 'POST':   
        stream = StringIO(request.body)
        data = JSONParser().parse(stream)   
        result=dbconn.system_js.fnFetchUserDetails(data);
        return Response(json.dumps(result, default=json_util.default))  
        # return Response("success")            
    else:        
        return Response("failure")     


