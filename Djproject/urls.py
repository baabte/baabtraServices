from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import View, TemplateView
from rest_framework.views import APIView
from myapp.jobRelatedView import FileUploadView
from myapp.companyRegisterRelatedView import companyRegisterView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^InsertUserMenu/$', 'myapp.views.InsertUserMenu', name='InsertUserMenu'),                                     #url for routing to the InsertUserMenu() function inside view.py
    url(r'^FnGetCompanyDetails/$', 'myapp.views.FnGetCompanyDetailsView', name='FnGetCompanyDetails'),#Author:Jihin ; Purpose:Get Registed company details for role menu mapping
    url(r'^FnGetCompanyDetailsJi/$', 'myapp.views.FnGetCompanyDetailsJiView', name='FnGetCompanyDetailsJi'),#Author:Jihin ; Purpose:Get Registed company details for role menu mapping
    url(r'^GetAllRoles/$', 'myapp.views.GetAllRolesView', name='GetAllRoles'),
    url(r'^FnLoadTopLevelRoles/$', 'myapp.views.FnLoadTopLevelRolesView', name='FnLoadTopLevelRoles'),
    url(r'^CompanyRegistration/$',companyRegisterView.as_view(), name='CompanyRegistration'),
    url(r'^LoadUsers/$', 'myapp.views.LoadUsers', name='LoadUsers'),                                                    #url for routing to the LoadUsers() function inside view.py
    url(r'^LoadExMenuItems4AUMMapping/$', 'myapp.views.LoadExMenuItems4AUMMapping', name='LoadExMenuItems4AUMMapping'), #url for routing to the LoadExMenuItems4AUMMapping() function inside view.py
    url(r'^LoadMenuItems4AUMMapping/$', 'myapp.views.LoadMenuItems4AUMMapping', name='LoadMenuItems4AUMMapping'),   #url for routing to the LoadMenuItems4AUMMapping() function inside view.py
    url(r'^GetRoleMenus/$', 'myapp.views.GetRoleMenusView', name='GetRoleMenus'),
	url(r'^RegisteredCompanies/$', 'myapp.views.RegisteredCompanyView', name='RegisteredCompanies'),
 	url(r'^CompanySector/$', 'myapp.views.CompanySectorView', name='CompanySector'),
 	url(r'^CountryStateDistrict/$', 'myapp.views.CountryStateDistrictView', name='CountryStateDistrict'),
    url(r'^Login/$', 'myapp.views.Login', name='Login'),  #URL for the login,added by suhail
    url(r'^ViewManageCompanyRole/$', 'myapp.views.ManageRolesOfCompanyView', name='ViewManageCompanyRole'), #created by midhun
    url(r'^ManageCompanyRole/$', 'myapp.views.ManageRolesOfCompany', name='ManageCompanyRole'), #created by midhun
    url(r'^UpdateCompanyRole/$', 'myapp.views.UpdateCompanyRole', name='UpdateCompanyRole'), #created by midhun
    url(r'^DeleteCompanyRole/$', 'myapp.views.DeleteCompanyRole', name='DeleteCompanyRole'), #created by midhun
    url(r'^GetAllMenus/$', 'myapp.views.GetAllMenusView', name='GetAllMenus'),
    url(r'^SaveNewRoleMenu/$', 'myapp.views.SaveNewRoleMenu', name='SaveNewRoleMenu'),
	url(r'^GetMenuItems/$', 'myapp.views.GetMenuItems', name='GetMenuItems'),
    url(r'^UserNameValid/$', 'myapp.views.UserNameValidView', name='UserNameValid'),
    url(r'^CompanyDelete/$', 'myapp.views.CompanyDeleteView', name='CompanyDelete'),
    url(r'^CompanyEdit/$', 'myapp.views.CompanyEditView', name='CompanyEdit'),
    url(r'^show_more_company_role/$', 'myapp.views.show_more_company_role', name='show_more_company_role'),#created by midhun
    url(r'^APIgetCompanyJobs/$', 'myapp.companyJobView.APIgetCompanyJobs', name='APIgetCompanyJobs'), #Author:Lijin,Purpose:get list of jobs under a company
    url(r'^postCompanyJobs/$', 'myapp.companyJobView.postCompanyJobs', name='postCompanyJobs'), #Author:Lijin,Purpose:post jobs as company,
    url(r'^APIapplyCompanyJobs/$', FileUploadView.as_view(), name='myapp.FileUploadView.FileUploadView'), #Author:Lijin,Purpose:Add feature for candidates to apply for the jobs,
    url(r'^getRptUserDetails/$', 'myapp.views.getRptUserDetails', name='getRptUserDetails'), #Author:Akshath kumar,description: Retrving of users details for google chart reporting.
    url(r'^ShowMoreCompanies/$', 'myapp.views.showMoreCompaniesView', name='ShowMoreCompanies'),
    url(r'^find_company_id/$', 'myapp.views.find_company_id', name='find_company_id'),
    url(r'^getCompanyJobs/$', 'myapp.companyJobView.getCompanyJobs', name='getCompanyJobs'), #Author:Jihin
    url(r'^UpdateJobDetails/$', 'myapp.companyJobView.UpdateJobDetailsView', name='UpdateJobDetails'), #Author:Jihin
    url(r'^HideJobDetails/$', 'myapp.companyJobView.HideJobDetailsView', name='HideJobDetails'), #Author:Jihin
    url(r'^EmailAlreadyRegisterdorNot/$', 'myapp.views.EmailAlreadyRegisterdorNot', name='EmailAlreadyRegisterdorNot'),
    url(r'^LinkAccountWithFacebook/$', 'myapp.views.LinkAccountWithFacebook', name='LinkAccountWithFacebook')
    
    
)+ static('/files/', document_root=settings.FILEUPLOAD_PATH)
