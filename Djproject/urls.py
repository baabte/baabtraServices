from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import View, TemplateView
from rest_framework.views import APIView
from myapp.jobRelatedView import FileUploadView
from myapp.fileUploadView import CourseFileUploadView 
from myapp.paymentRelatedViews import PaymentView
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
    url(r'^LoadMenus/$', 'myapp.menuRelatedView.LoadMenuView', name='LoadMenus'),
    url(r'^AddMenus/$', 'myapp.menuRelatedView.AddMenuView', name='AddMenus'),
    url(r'^UpdateMenus/$', 'myapp.menuRelatedView.UpdateMenuView', name='UpdateMenus'),
    url(r'^RemoveMenu/$', 'myapp.menuRelatedView.RemoveMenuView', name='RemoveMenu'),
	url(r'^RegisteredCompanies/$', 'myapp.views.RegisteredCompanyView', name='RegisteredCompanies'),
 	url(r'^CompanySector/$', 'myapp.views.CompanySectorView', name='CompanySector'),
 	url(r'^CountryStateDistrict/$', 'myapp.views.CountryStateDistrictView', name='CountryStateDistrict'),
    url(r'^Login/$', 'myapp.loginLogoutRealted.Login', name='Login'),  #URL for the login,added by suhail
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
    url(r'^APIgetCompanyJobs/$', 'myapp.companyJobView.APIgetCompanyJobs', name='APIgetCompanyJobs'), #Author:Lijin,Purpose:get list of jobs under a company
    url(r'^postCompanyJobs/$', 'myapp.companyJobView.postCompanyJobs', name='postCompanyJobs'), #Author:Lijin,Purpose:post jobs as company,
    url(r'^APIapplyCompanyJobs/$', FileUploadView.as_view(), name='myapp.FileUploadView.FileUploadView'), #Author:Lijin,Purpose:Add feature for candidates to apply for the jobs,
    url(r'^getRptUserDetails/$', 'myapp.views.getRptUserDetails', name='getRptUserDetails'), #Author:Akshath kumar,description: Retrving of users details for google chart reporting.
    url(r'^ShowMoreCompanies/$', 'myapp.views.showMoreCompaniesView', name='ShowMoreCompanies'),
    url(r'^getCompanyJobs/$', 'myapp.companyJobView.getCompanyJobs', name='getCompanyJobs'), #Author:Jihin
    url(r'^UpdateJobDetails/$', 'myapp.companyJobView.UpdateJobDetailsView', name='UpdateJobDetails'), #Author:Jihin
    url(r'^HideJobDetails/$', 'myapp.companyJobView.HideJobDetailsView', name='HideJobDetails'), #Author:Jihin
    url(r'^EmailAlreadyRegisterdorNot/$', 'myapp.views.EmailAlreadyRegisterdorNot', name='EmailAlreadyRegisterdorNot'),
    url(r'^LinkAccountWithFacebook/$', 'myapp.views.LinkAccountWithFacebook', name='LinkAccountWithFacebook'),
    url(r'^SelectedCompany/$', 'myapp.views.SelectedCompanyView', name='SelectedCompany'),#Arun
    url(r'^SearchCompany/$', 'myapp.views.SearchCompanyView', name='SearchCompany'),#Arun
    url(r'^GetUserPlan/$', 'myapp.views.GetUserPlanView', name='GetUserPlan'),#Arun
    url(r'^GetPlans/$', 'myapp.views.GetPlansView', name='GetPlans'),#Arun
    url(r'^GetFeatures/$', 'myapp.views.GetFeaturesView', name='GetFeatures'),#Arun
    url(r'^ChangeUserPlan/$', 'myapp.views.ChangeUserPlanView', name='ChangeUserPlan'),#Arun
    url(r'^EditPricing/$', 'myapp.views.EditPricingView', name='EditPricing'),#Arun
    url(r'^AddFeature/$', 'myapp.views.AddFeatureView', name='AddFeature'),#Arun
    url(r'^DeleteFeature/$', 'myapp.views.DeleteFeatureView', name='DeleteFeature'),#Arun
    url(r'^EditBilling/$', 'myapp.views.EditBillingView', name='EditBilling'),#Arun
    url(r'^GetFeaturesConfig/$', 'myapp.views.GetFeaturesConfigView', name='GetFeaturesConfig'),#Arun
    url(r'^SaveFeaturesConfig/$', 'myapp.views.SaveFeaturesConfigView', name='SaveFeaturesConfig'),#Arun
    url(r'^GetFeaturesConfigValues/$', 'myapp.views.GetFeaturesConfigValues', name='GetFeaturesConfigValues'),#Arun
    url(r'^InsertBranch/$', 'myapp.branchRelatedView.fnInsertBranches', name='InsertBranch'),#jihin
    url(r'^LoadBranches/$', 'myapp.branchRelatedView.fnLoadBranches', name='LoadBranches'),#jihin
    url(r'^loadInputTypes/$','myapp.feature_config.loadInputTypes', name='loadInputTypes'),#created by midhun
    url(r'^newFeatureCreation/$','myapp.feature_config.newFeatureCreation', name='newFeatureCreation'),#created by midhun
    url(r'^loadFeatures/$','myapp.billing_plans.loadFeatures', name='loadFeatures'),#created by midhun
    url(r'^addNewBillingPlan/$','myapp.billing_plans.addNewBillingPlan', name='addNewBillingPlan'),#created by midhun
    url(r'^retriveCurrentPlans/$','myapp.billing_plans.retriveCurrentPlans', name='retriveCurrentPlans'),#created by midhun
    url(r'^delete_plans/$','myapp.billing_plans.delete_plans', name='delete_plans'),#created by midhun
    url(r'^loadlogUserdata/$', 'myapp.loginLogoutRealted.loadlogUserdata', name='loadlogUserdata'),  #URL for the login,added by midhun
    url(r'^logout/$', 'myapp.loginLogoutRealted.logout', name='logout'),  #URL for the login,added by midhun
    url(r'^InsertDomain/$', 'myapp.domainRelatedViews.InsertDomainView', name='InsertDomain'),  #URL for the insert domain,added by jihin
    url(r'^LoadDomain/$', 'myapp.domainRelatedViews.LoadDomainView', name='LoadDomain'),  #URL for the insert domain,added by jihin
    url(r'^GetExitCriteria/$', 'myapp.views.GetExitCriteriaView', name='GetExitCriteria'), #by Arun
    url(r'^SaveCourseElementForm/$', 'myapp.views.SaveCourseElementFormView', name='SaveCourseElementForm'),  #by Arun
    url(r'^forgotPassword/$', 'myapp.views.forgotPassword', name='forgotPassword'), #URL for the forgot password,added by midhun
    url(r'^LoadGlobalValues/$', 'myapp.commonViews.LoadGlobalValuesView', name='LoadGlobalValues'),#added by jihin for get global values
    url(r'^InsertDomain/$', 'myapp.domainRelatedViews.InsertDomainView', name='InsertDomain'),  #URL for the insert domain,added by jihin
    url(r'^GetExitCriteria/$', 'myapp.views.GetExitCriteriaView', name='GetExitCriteria'), #by Arun
    url(r'^SaveCourseElementForm/$', 'myapp.views.SaveCourseElementFormView', name='SaveCourseElementForm'),  #by Arun
    url(r'^forgotPassword/$', 'myapp.views.forgotPassword', name='forgotPassword'),  #URL for the forgot password,added by midhun
    url(r'^GetCourseElements/$', 'myapp.views.GetCourseElementsView', name='GetCourseElements'),  #by Arun
    url(r'^DeleteCourseElement/$', 'myapp.views.DeleteCourseElementView', name='DeleteCourseElement'),  #by Arun
    url(r'^SaveExitCriteria/$', 'myapp.views.SaveExitCriteriaView', name='SaveExitCriteria'),  #by Arun
    url(r'^RegisterUser/$', 'myapp.views.RegisterUserView', name='RegisterUser'),  #by Arun
    url(r'^FetchUserDetails/$', 'myapp.views.FetchUserDetailsView', name='FetchUserDetails'),  #by Arun
    url(r'^DeleteExitCriteria/$', 'myapp.views.DeleteExitCriteriaView', name='DeleteExitCriteria'), #by Arun
    url(r'^saveCourseObject/$', 'myapp.course.saveCourseObjectView', name='saveCourseObject'), #for save course details, added by jihin
    url(r'^removeCourseElement/$', 'myapp.course.removeCourseElementView', name='removeCourseElement'), #for remove course element, added by jihin
    url(r'^editCourseElement/$', 'myapp.course.editCourseElementView', name='editCourseElement'), #for remove course element, added by jihin
    url(r'^loadDraftedCourses/$', 'myapp.course.loadDraftedCoursesView', name='loadDraftedCourses'), #for load drafted course, added by jihin 
    url(r'^deleteDraftedCourse/$', 'myapp.course.deleteDraftedCourseView', name='deleteDraftedCourse'), #for delete Drafted Course, added by jihin 
    url(r'^loadCourseDetails/$', 'myapp.course.loadCourseDetailsView', name='loadCourseDetails'), #for load course details, added by jihin
    url(r'^saveCourseTimelineEelement/$', 'myapp.course.saveCourseTimelineEelementView', name='saveCourseTimelineEelement'), #for save course details, added by jihin
    url(r'^RegisterReseller/$', 'myapp.resellerRelatedViews.registerResellerView', name='RegisterReseller'), #for save reseller details, added by jihin
    url(r'^CourseFileUpload/$', CourseFileUploadView.as_view(), name='myapp.CourseFileUploadView.CourseFileUploadView'),# added by jihin, for upload course related files
    url(r'^SaveCustomForm/$', 'myapp.customFormRelatedViews.SaveCustomFormView', name='SaveCustomForm'), #by Arun for custom Form
    url(r'^FetchCustomForm/$', 'myapp.customFormRelatedViews.FetchCustomFormView', name='FetchCustomForm'), #by Arun for custom Form
    url(r'^FetchCourseList/$', 'myapp.course.fetchCourseListView', name='FetchCourseList'), #by Arun for custom Form

    
    #url(r'^userRegisterationPayment/$', 'myapp.paymentRelatedViews.userRegisterationPaymentView', name='userRegisterationPayment')
    # registerResellerView
    url(r'^userRegisterationPayment/$', PaymentView.as_view(), name='myapp.paymentRelatedViews.PaymentView'), #Author:Lijin,Purpose:Add feature for candidates to apply for the jobs,
    url(r'^loadPublishedCourses/$', 'myapp.course.loadPublishedCourses', name='loadPublishedCourses'), #for load completed course by Midhun
     url(r'^loadCourseData/$', 'myapp.course.loadCourseData', name='loadCourseData') #for load completed course by Midhun
)+ static('/files/', document_root=settings.FILEUPLOAD_PATH)


