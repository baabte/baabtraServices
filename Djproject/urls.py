from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import View, TemplateView
from rest_framework.views import APIView
from myapp.jobRelatedView import FileUploadView
from myapp.fileUploadView import CourseFileUploadView 
from myapp.paymentRelatedViews import PaymentView
from myapp.companyRegisterRelatedView import companyRegisterView
from myapp.fileRemoveView import FileRemove
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
    url(r'^fileRemove/$',FileRemove.as_view(), name='fileRemove'),
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
    url(r'^LoadUsersUnderRole/$', 'myapp.commonViews.LoadUsersUnderRoleView', name='LoadUsersUnderRole'),#added by jihin for Load Users Under a Role
    url(r'^LoadUserCardDetails/$', 'myapp.commonViews.LoadUserCardDetailsView', name='LoadUserCardDetails'),#added by jihin for Load User Card Details
    url(r'^loadMentees/$', 'myapp.commonViews.loadMenteesView', name='loadMentees'),#added by jihin for load Mentees
    url(r'^LoadRoleUnderCompany/$', 'myapp.commonViews.LoadRoleUnderCompanyView', name='LoadRoleUnderCompany'),#added by jihin for load Mentees
    url(r'^RemoveFileFromServer/$', 'myapp.commonViews.RemoveFileFromServerView', name='RemoveFileFromServer'),#added by jihin for Load Role Under Company
    url(r'^SaveAppSettings/$', 'myapp.commonViews.SaveAppSettingsView', name='SaveAppSettings'),#added by jihin for Save App Settings
    url(r'^UploadProfilePic/$', 'myapp.commonViews.UploadProfilePicView', name='UploadProfilePic'),#added by jihin for upload profile picture
    url(r'^InsertDomain/$', 'myapp.domainRelatedViews.InsertDomainView', name='InsertDomain'),  #URL for the insert domain,added by jihin
    url(r'^GetExitCriteria/$', 'myapp.views.GetExitCriteriaView', name='GetExitCriteria'), #by Arun
    url(r'^SaveCourseElementForm/$', 'myapp.views.SaveCourseElementFormView', name='SaveCourseElementForm'),  #by Arun
    url(r'^forgotPassword/$', 'myapp.views.forgotPassword', name='forgotPassword'),  #URL for the forgot password,added by midhun
    url(r'^GetCourseElements/$', 'myapp.views.GetCourseElementsView', name='GetCourseElements'),  #by Arun
    url(r'^DeleteCourseElement/$', 'myapp.views.DeleteCourseElementView', name='DeleteCourseElement'),  #by Arun
    url(r'^SaveExitCriteria/$', 'myapp.views.SaveExitCriteriaView', name='SaveExitCriteria'),  #by Arun
    url(r'^RegisterUser/$', 'myapp.views.RegisterUserView', name='RegisterUser'),  #by Arun
    url(r'^RegisterMultipleUsers/$', 'myapp.views.RegisterMultipleUsersView', name='RegisterMultipleUsers'),  #by Register Multiple Users
    url(r'^FetchUserDetails/$', 'myapp.views.FetchUserDetailsView', name='FetchUserDetails'),  #by Arun
    url(r'^DeleteExitCriteria/$', 'myapp.views.DeleteExitCriteriaView', name='DeleteExitCriteria'), #by Arun
    url(r'^saveCourseObject/$', 'myapp.course.saveCourseObjectView', name='saveCourseObject'), #for save course details, added by jihin
    url(r'^getCourseSyllabus/$', 'myapp.course.getCourseSyllabus', name='getCourseSyllabus'), #by lijin for fetching syllabus
    url(r'^saveMarksheetElements/$', 'myapp.course.saveMarksheetElements', name='saveMarksheetElements'), #by lijin for saving marksheetConfig
    url(r'^removeCourseElement/$', 'myapp.course.removeCourseElementView', name='removeCourseElement'), #for remove course element, added by jihin
    url(r'^editCourseElement/$', 'myapp.course.editCourseElementView', name='editCourseElement'), #for remove course element, added by jihin
    url(r'^loadDraftedCourses/$', 'myapp.course.loadDraftedCoursesView', name='loadDraftedCourses'), #for load drafted course, added by jihin 
    url(r'^deleteDraftedCourse/$', 'myapp.course.deleteDraftedCourseView', name='deleteDraftedCourse'), #for delete Drafted Course, added by jihin 
    url(r'^loadCourseDetails/$', 'myapp.course.loadCourseDetailsView', name='loadCourseDetails'), #for load course details, added by jihin
    url(r'^saveCourseTimelineEelement/$', 'myapp.course.saveCourseTimelineEelementView', name='saveCourseTimelineEelement'), #for save course details, added by jihin
    url(r'^SaveCourseElementFields/$', 'myapp.course.SaveCourseElementFieldsView', name='SaveCourseElementFields'), #for save Coure Element Fields, added by jihin
    url(r'^GetCourseElementFields/$', 'myapp.course.GetCourseElementFieldsView', name='GetCourseElementFields'), #for get Coure Element Fields, added by jihin
    url(r'^DeleteCourseElementFields/$', 'myapp.course.DeleteCourseElementFieldsView', name='DeleteCourseElementFields'), #for get Coure Element Fields, added by jihin
    url(r'^RegisterReseller/$', 'myapp.resellerRelatedViews.registerResellerView', name='RegisterReseller'), #for save reseller details, added by jihin
    url(r'^CourseFileUpload/$', CourseFileUploadView.as_view(), name='myapp.CourseFileUploadView.CourseFileUploadView'),# added by jihin, for upload course related files
    url(r'^SaveCustomForm/$', 'myapp.customFormRelatedViews.SaveCustomFormView', name='SaveCustomForm'), #by Arun for custom Form
    url(r'^FetchCustomForm/$', 'myapp.customFormRelatedViews.FetchCustomFormView', name='FetchCustomForm'), #by Arun for custom Form
    url(r'^saveAnswer/$', 'myapp.course.saveAnswer', name='saveAnswer'), #for remove course element, added by jihin
    url(r'^FetchCourseList/$', 'myapp.course.FetchCourseListView', name='FetchCourseList'), #by Arun for custom Form
    url(r'^FetchRolesList/$', 'myapp.customFormRelatedViews.FetchRolesListView', name='FetchRolesList'), #by Arun for custom Form
    url(r'^FetchSpecificCustomForm/$', 'myapp.customFormRelatedViews.FetchSpecificCustomFormView', name='FetchSpecificCustomForm'), #by Arun for custom Form
    url(r'^getCurrentElement/$', 'myapp.candidateCourseRelated.getCurrentElement', name='getCurrentElement'), #by Lijin for managing candidate course full view
    url(r'^getCandidateDetailsForCertificate/$', 'myapp.candidateCourseRelated.getCandidateDetailsForCertificate', name='getCandidateDetailsForCertificate'), #by Lijin for managing candidate certificate
    url(r'^SaveTestStartTime/$', 'myapp.testRelatedViews.SaveTestStartTimeView', name='SaveTestStartTime'), #by Arun
    url(r'^SaveTestStartTimeRandomExam/$', 'myapp.testRelatedViews.SaveTestStartTimeRandomExamView', name='SaveTestStartTimeRandomExam'), #by Arun
    url(r'^TestTimeReCheck/$', 'myapp.testRelatedViews.TestTimeReCheckView', name='TestTimeReCheck'), #by Arun
    url(r'^SubmitTest/$', 'myapp.testRelatedViews.SubmitTestView', name='SubmitTest'), #by Arun
    url(r'^courseElementsByAttendence/$', 'myapp.attendenceRelatedViews.courseElementsByAttendenceView', name='courseElementsByAttendence'), #by Arun
    url(r'^MarkAttendence/$', 'myapp.attendenceRelatedViews.MarkAttendenceView', name='MarkAttendence'), #by Arun
    url(r'^EvaluationFetch/$', 'myapp.evaluationRelatedViews.EvaluationFetchView', name='EvaluationFetch'), #by Arun
    url(r'^EvaluateAnswer/$', 'myapp.evaluationRelatedViews.EvaluateAnswerView', name='EvaluateAnswer'), #by Arun
    url(r'^ExistingMaterials/$', 'myapp.course.ExistingMaterialsView', name='ExistingMaterials'), #by Arun
    url(r'^GetCourses/$', 'myapp.course.GetCoursesView', name='GetCourses'), #by Arun
    url(r'^SaveExistingElement/$', 'myapp.course.SaveExistingElementView', name='SaveExistingElement'), #by Arun
    url(r'^moveCourseElement/$', 'myapp.course.moveCourseElementView', name='moveCourseElement'), #by Jihin
    url(r'^getPaymentReport/$', 'myapp.paymentReport.getPaymentReport', name='getPaymentReport'), #by Arun
    url(r'^fnLoadMenteesBlindFromBatch/$', 'myapp.attendenceRelatedViews.fnLoadMenteesBlindFromBatch', name='fnLoadMenteesBlindFromBatch'), #by lijin
    url(r'^saveCandidatesAttendance/$', 'myapp.attendenceRelatedViews.saveCandidatesAttendance', name='saveCandidatesAttendance'), #by lijin
    url(r'^updateCandidatesAttendance/$', 'myapp.attendenceRelatedViews.updateCandidatesAttendance', name='updateCandidatesAttendance'), #by lijin
    url(r'^fnLoadMenteesMarkedAttendanceFromBatch/$', 'myapp.attendenceRelatedViews.fnLoadMenteesMarkedAttendanceFromBatch', name='fnLoadMenteesMarkedAttendanceFromBatch'), #by lijin
    url(r'^userCourseDetailsOF/$', 'myapp.payment.userCourseDetailsOFView', name='userCourseDetailsOF'), #by lijin
    url(r'^RegisterCollege/$', 'myapp.college.RegisterCollegeView', name='RegisterCollege'), #by lijin
    url(r'^getCourseSyllabus4CandidateView/$', 'myapp.candidateCourseRelated.getCourseSyllabus4CandidateView', name='getCourseSyllabus4CandidateView'), #by Arun for managing candidate course full view
    url(r'^getElement4CandidateView/$', 'myapp.candidateCourseRelated.getElement4CandidateView', name='getElement4CandidateView'), #by Arun for managing candidate course full view

    
    # userCourseDetailsOFView
    #url(r'^userRegisterationPayment/$', 'myapp.paymentRelatedViews.userRegisterationPaymentView', name='userRegisterationPayment')
    # registerResellerView
    url(r'^userRegisterationPayment/$', PaymentView.as_view(), name='myapp.paymentRelatedViews.PaymentView'), #Author:Lijin,Purpose:Add feature for candidates to apply for the jobs,
    url(r'^loadPublishedCourses/$', 'myapp.course.loadPublishedCourses', name='loadPublishedCourses'), #for load completed course by Midhun
    url(r'^duplicateCourse/$', 'myapp.course.duplicateCourseView', name='duplicateCourse'), #for load completed course by Midhun
    url(r'^courseByKeywords/$', 'myapp.course.courseByKeywordsView', name='courseByKeywords'), #for load course suggestions by Jihin
    url(r'^loadCourseData/$', 'myapp.course.loadCourseData', name='loadCourseData'), #for load completed course by Midhun
    url(r'^loadCoursesForCandidates/$', 'myapp.course.loadCoursesForCandidates', name='loadCoursesForCandidates'), #for load completed course by Midhun
    url(r'^FetchCourseData/$', 'myapp.course.FetchCourseData', name='FetchCourseData'), #for load completed course by Midhun
    url(r'^loadProfileData/$', 'myapp.profile.loadProfileData', name='loadProfileData'), #for load completed course by Midhun
    url(r'^updateUserProfileData/$', 'myapp.profile.updateUserProfileData', name='updateUserProfileData'), #for update user profile data
    url(r'^changeUserPassword/$', 'myapp.profile.changeUserPassword', name='changeUserPassword'), #for update user password data
    url(r'^saveNewBatches/$', 'myapp.Batches.saveNewBatches', name='saveNewBatches'), #for update user profile data
    url(r'^fnLoadBatchesByCourse/$', 'myapp.Batches.fnLoadBatchesByCourse', name='fnLoadBatchesByCourse'), # for getting batch list by courseId
    url(r'^fnLoadMenteesByBatch/$', 'myapp.Batches.fnLoadMenteesByBatch', name='fnLoadMenteesByBatch'), # for getting mentee list by batchMAppingId : Lijin on 29-5-2015
    url(r'^fnMoveMenteeToAnotherBatch/$', 'myapp.Batches.fnMoveMenteeToAnotherBatch', name='fnMoveMenteeToAnotherBatch'), # for moving candidates to another batch : Lijin on 29-5-2015
    url(r'^fnGetUnallocatedCandidatesByCourse/$', 'myapp.Batches.fnGetUnallocatedCandidatesByCourse', name='fnGetUnallocatedCandidatesByCourse'), # for getting list of unallocated candidates by courseId : Lijin on 29-5-2015
    url(r'^fnBulkEnroll/$', 'myapp.enrollment.fnBulkEnroll', name='fnBulkEnroll'), #for bulk enrollment
    url(r'^fnLoadUserReport/$', 'myapp.enrollment.fnLoadUserReport', name='fnLoadUserReport'), #for bulk enrollment
    url(r'^fnLoadCompnayUsers/$', 'myapp.user.fnLoadCompnayUsers', name='fnLoadCompnayUsers'), #for bulk enrollment
    url(r'^fnLoadMenteesForPayment/$', 'myapp.user.fnLoadMenteesForPayment', name='fnLoadMenteesForPayment'), #for paymnet option after enrolling : Lijin - on 27-5-2015
    url(r'^fetchUsersByDynamicSearch/$', 'myapp.user.fetchUsersByDynamicSearchView', name='fetchUsersByDynamicSearch'), #for fetch Users By Dynamic Search
    url(r'^fnFetchFormFeildsForSearch/$', 'myapp.user.fnFetchFormFeildsForSearchView', name='fnFetchFormFeildsForSearch'), #for Fetch Form Feilds For Search
    url(r'^FetchUsersToCourseAllocate/$', 'myapp.user.FetchUsersToCourseAllocateView', name='FetchUsersToCourseAllocate'), #for bulk enrollment
    url(r'^AllocateUsersToCourse/$', 'myapp.user.AllocateUsersToCourseView', name='AllocateUsersToCourse'), #for bulk enrollment
    url(r'^addUserNomination/$', 'myapp.user.addUserNominationView', name='addUserNomination'), #for add User Nomination
    url(r'^fnLoadMenteesForApprove/$', 'myapp.user.fnLoadMenteesForApproveView', name='fnLoadMenteesForApprove'), #for Load Mentees For Approve
    url(r'^ApproveUserRequest/$', 'myapp.user.ApproveUserRequestView', name='ApproveUserRequest'), #for Approve User Request 
    url(r'^loadOrderFormById/$', 'myapp.user.loadOrderFormByIdView', name='loadOrderFormById'), #for load Order Form By Id 
    url(r'^FetchOrderForms/$', 'myapp.orderForm.FetchOrderFormsView', name='FetchOrderForms'), #for orderform 
    url(r'^OFDetails/$', 'myapp.orderForm.OFDetailsView', name='OFDetails'), #for orderform 
    url(r'^requestRefund/$', 'myapp.payment.requestRefundView', name='requestRefund'), #for load Order Form By Id 
    url(r'^fetchRefundRequest/$', 'myapp.payment.fetchRefundRequestView', name='fetchRefundRequest'), #for load Order Form By Id 
    url(r'^updateRefundRequest/$', 'myapp.payment.updateRefundRequestView', name='updateRefundRequest'), #for load Order Form By Id 
    url(r'^processRefund/$', 'myapp.payment.processRefundView', name='processRefund'), #for load Order Form By Id 
    url(r'^fetchUserResults/$', 'myapp.reports.fetchUserResultsView', name='fetchUserResults'), #for load Order Form By Id 
    url(r'^fetchUserResultReport/$', 'myapp.reports.fetchUserResultReportView', name='fetchUserResultReport'), #for load Order Form By Id 
    url(r'^fetchUsersReportBasedOnDynamicSearch/$', 'myapp.reports.fetchUsersReportBasedOnDynamicSearchView', name='fetchUsersReportBasedOnDynamicSearch'), #for fetch Users Report Based On Dynamic Search

    url(r'^verifyCandidateByCourse/$', 'myapp.user.verifyCandidateByCourse', name='verifyCandidateByCourse'), #for verifying order form by course Created by Lijin
    url(r'^fnSaveCandidateMapping/$', 'myapp.user.fnSaveCandidateMapping', name='fnSaveCandidateMapping'), #for saving parent-candidate mapping into parent's user details, Created by Lijin
    url(r'^fnLoadParents/$', 'myapp.user.fnLoadParents', name='fnLoadParents'), #for loading parents, Created by Lijin
    url(r'^fnLoadMappedCandidatesForParent/$', 'myapp.user.fnLoadMappedCandidatesForParent', name='fnLoadMappedCandidatesForParent'), #for loading candidates that are mapped to a parent, Created by Lijin
    
    url(r'^loadBatches/$', 'myapp.Batches.loadBatches', name='loadBatches'), #for loading batches
    url(r'^loadExistingCoursesUnderBatch/$', 'myapp.Batches.loadExistingCoursesUnderBatch', name='loadExistingCoursesUnderBatch'), #for loading batches
    url(r'^addCoursesToBatch/$', 'myapp.Batches.addCoursesToBatch', name='addCoursesToBatch'), #for adding courses to batch
    url(r'^loadCourseRelatedBatches/$', 'myapp.Batches.loadCourseRelatedBatches', name='loadCourseRelatedBatches'), #for loading existing batches related to courses
    url(r'^loadBatches/$', 'myapp.Batches.loadBatches', name='loadBatches'), #for bulk enrollment
    url(r'^saveFeedbackForm/$', 'myapp.feedback.saveFeedbackFormView', name='saveFeedbackForm'), #for save Feedback Form
    url(r'^viewFeedbackRequests/$', 'myapp.feedback.viewFeedbackRequestsView', name='viewFeedbackRequests'), #for view Feedback Requests
    url(r'^LoadFeedbackRequestDetails/$', 'myapp.feedback.LoadFeedbackRequestDetailsView', name='LoadFeedbackRequestDetails'), #for view Feedback Requests
    url(r'^SaveUserFeedback/$', 'myapp.feedback.SaveUserFeedbackView', name='SaveUserFeedback'), #for Save User Feedback
    url(r'^fnLoadFeedbackList/$', 'myapp.user.fnLoadFeedbackList', name='fnLoadFeedbackList'), #for loading feedback list
    url(r'^fnLoadFeedbackReport/$', 'myapp.user.fnLoadFeedbackReport', name='fnLoadFeedbackReport'),
    url(r'^addEvaluator/$', 'myapp.globalSettings.addEvaluator', name='addEvaluator'),
    url(r'^fnUpdateNotificationConfig/$', 'myapp.globalSettings.fnUpdateNotificationConfig', name='fnUpdateNotificationConfig'),#by:lijin , for updating notification configuration
    url(r'^fnGetNotificationConfig/$', 'myapp.globalSettings.fnGetNotificationConfig', name='fnGetNotificationConfig'),#by:lijin , for getting notification configuration
    url(r'^GenerateCode/$', 'myapp.globalSettings.GenerateCode', name='GenerateCode'),
    url(r'^retrieveExistingConf/$', 'myapp.globalSettings.retrieveExistingConf', name='retrieveExistingConf'),
    url(r'^removeExistingEvaluator/$', 'myapp.globalSettings.removeExistingEvaluator', name='removeExistingEvaluator'),
    url(r'^updateExistingPrefix/$', 'myapp.globalSettings.updateExistingPrefix', name='updateExistingPrefix'),
    url(r'^fnUpdateCandidateAgeLimit/$', 'myapp.globalSettings.fnUpdateCandidateAgeLimit', name='fnUpdateCandidateAgeLimit'),#created by lijin
    url(r'^loadUserNotification/$', 'myapp.notification.loadUserNotificationView', name='loadUserNotification'),
    url(r'^AddDepartment/$', 'myapp.departmentView.AddDepartmentView', name='AddDepartment'),#for Add Department
    url(r'^LoadDepartment/$', 'myapp.departmentView.LoadDepartmentView', name='LoadDepartment'),#for load Department
    url(r'^fnLoadBatchesForView/$', 'myapp.Batches.fnLoadBatchesForView', name='fnLoadBatchesForView'),
    url(r'^fnLoadMenteesForView/$', 'myapp.Batches.fnLoadMenteesForView', name='fnLoadMenteesForView'),
    url(r'^fnloadCourses4AssigningCourseMaterial/$', 'myapp.Batches.fnloadCourses4AssigningCourseMaterial', name='fnloadCourses4AssigningCourseMaterial'),
    url(r'^loadCourses4AssigningCourseMaterialStudent/$', 'myapp.Batches.loadCourses4AssigningCourseMaterialStudentView', name='loadCourses4AssigningCourseMaterialStudent'),
    url(r'^loadUserNotification/$', 'myapp.notification.loadUserNotificationView', name='loadUserNotification'),
    url(r'^fnBulkEnrollavailable/$', 'myapp.enrollment.fnBulkEnrollavailable', name='fnBulkEnrollavailable'), #for bulk enrollment up to the selected users from the list
    url(r'^sendEmailSmsNotification/$', 'myapp.emailSms.sendEmailSmsNotification', name='sendEmailSmsNotification'), #for sending email and sms notification
    url(r'^fnloadCourseMaterial4multiSelect/$', 'myapp.Batches.fnloadCourseMaterial4multiSelect', name='fnloadCourseMaterial4multiSelect'),
    url(r'^fnAssignCourseMaterial2timeline/$', 'myapp.Batches.fnAssignCourseMaterial2timeline', name='fnAssignCourseMaterial2timeline'),
    url(r'^fnloadBatchDetails4assignment/$', 'myapp.Batches.fnloadBatchDetails4assignment', name='fnloadBatchDetails4assignment'),
    url(r'^loadMenuStates/$', 'myapp.emailSms.loadMenuStates', name='loadMenuStates'), #for sending email and sms notification
    url(r'^loadMenuNames/$', 'myapp.emailSms.loadMenuNames', name='loadMenuNames'), #for sending email and sms notification  
    url(r'^saveTemplates/$', 'myapp.emailSms.saveTemplates', name='saveTemplates'), #for sending email and sms notification      
    url(r'^loadTemplate/$', 'myapp.emailSms.loadTemplate', name='loadTemplate'), #for sending email and sms notification      
    url(r'^fnloadCourseMaterial4Batch/$', 'myapp.Batches.fnloadCourseMaterial4Batch', name='fnloadCourseMaterial4Batch'),
    url(r'^fnAssignCourseMaterials4Batch/$', 'myapp.Batches.fnAssignCourseMaterials4Batch', name='fnAssignCourseMaterials4Batch'),
    url(r'^fnloadBatchDetails4assignment/$', 'myapp.Batches.fnloadBatchDetails4assignment', name='fnloadBatchDetails4assignment'),
    url(r'^fnloadCoursesMaterials4menteeAtt/$', 'myapp.Batches.fnloadCoursesMaterials4menteeAtt', name='fnloadCoursesMaterials4menteeAtt'),
    url(r'^fnloadCourseMaterials4batchAtt/$', 'myapp.Batches.fnloadCourseMaterials4batchAtt', name='fnloadCourseMaterials4batchAtt'),
    url(r'^fnloadMentees4batchAtt/$', 'myapp.Batches.fnloadMentees4batchAtt', name='fnloadMentees4batchAtt'),
    url(r'^fnloadCoursesMaterials4menteeAtt/$', 'myapp.Batches.fnloadCoursesMaterials4menteeAtt', name='fnloadCoursesMaterials4menteeAtt'),
    url(r'^removeItemFromAgroup/$', 'myapp.globalSettings.removeItemFromAgroup', name='removeItemFromAgroup'),
    url(r'^setSupervisors/$', 'myapp.globalSettings.setSupervisors', name='setSupervisors'),
    url(r'^removeExistingSupervisors/$', 'myapp.globalSettings.removeExistingSupervisors', name='removeExistingSupervisors'),
    url(r'^fnLoadMenteesAttReport/$', 'myapp.reports.fnLoadMenteesAttReport', name='fnLoadMenteesAttReport'),
    url(r'^fnLoadCustomFormTemplates/$', 'myapp.custom-form.fnLoadCustomFormTemplates', name='fnLoadCustomFormTemplates'),
    url(r'^saveCustomFormMain/$', 'myapp.custom-form.fnSaveCustomFormMain', name='saveCustomFormMain'),
    url(r'^loadCustomFormsMain/$', 'myapp.custom-form.fnLoadCustomFormsMain', name='loadCustomFormsMain'),
    url(r'^SaveCompanyCustomForm/$', 'myapp.custom-form.fnSaveCompanyCustomForm', name='SaveCompanyCustomForm'),
    url(r'^LoadCompanyCustomForm/$', 'myapp.custom-form.fnLoadCompanyCustomForm', name='LoadCompanyCustomForm'),
    url(r'^LoadCustomFormforRegistration/$', 'myapp.custom-form.fnLoadCustomFormforRegistration', name='LoadCustomFormforRegistration'),
    url(r'^CustomFormUserRegistration/$', 'myapp.custom-form.fnCustomFormUserRegistration', name='CustomFormUserRegistration'),
    url(r'^deleteBatch/$', 'myapp.Batches.deleteBatch', name='deleteBatch'), #for deleting batches
    url(r'^editBatch/$', 'myapp.Batches.editBatch', name='editBatch'), #for editing batches
    url(r'^updateBatch/$', 'myapp.Batches.updateBatch', name='updateBatch'), #for editing batches
    url(r'^ChangeBatchStatus/$', 'myapp.Batches.ChangeBatchStatus', name='ChangeBatchStatus'), #for editing batches
    url(r'^LoadCoureBatchByBatchId/$', 'myapp.Batches.LoadCoureBatchByBatchIdView', name='LoadCoureBatchByBatchId'), #for Load Coure Batch By Batch Id
    url(r'^saveBatchTimelineChanges/$', 'myapp.Batches.saveBatchTimelineChangesView', name='saveBatchTimelineChanges'), #for save Batch Timeline Changes
    url(r'^LoadUserCourseDetails/$', 'myapp.Batches.LoadUserCourseDetailsView', name='LoadUserCourseDetails'), #for Load User Course Details
    # url(r'^userbaabtraComProfileData/$', 'myapp.baabtraComProfile.userbaabtraComProfileData', name='userbaabtraComProfileData'),
    #url(r'^baabtraComProfileData/$', 'myapp.baabtraComProfile.baabtraComProfileData', name='baabtraComProfileData'),
    url(r'^loadUserProfileDetails/$', 'myapp.baabtraComProfile.loadUserProfileDetailsView', name='loadUserProfileDetails'),
    url(r'^changelanguage/$', 'myapp.profile.changelanguage', name='changelanguage'),
    url(r'^GetCode/$', 'myapp.commonCalls.GetCode', name='GetCode'),
    url(r'^getStatus/$', 'myapp.commonCalls.getStatus', name='getStatus'), #by lijin for online check
    url(r'^setMenuType/$', 'myapp.globalSettings.setMenuType', name='setMenuType'),
    url(r'^fnLoadMenteesAttReport/$', 'myapp.reports.fnLoadMenteesAttReport', name='fnLoadMenteesAttReport'),
    url(r'^saveMenuColor/$', 'myapp.globalSettings.saveMenuColor', name='saveMenuColor'),
    url(r'^saveSubMenuAndBackgrounds/$', 'myapp.globalSettings.saveSubMenuAndBackgrounds', name='saveSubMenuAndBackgrounds'),
    url(r'^updateOrderFormStatus/$', 'myapp.user.updateOrderFormStatusView', name='updateOrderFormStatus'),
    url(r'^loadCourseToWebSite/$', 'myapp.publicAPIs.loadCourseToWebSiteView', name='loadCourseToWebSite'),
    url(r'^LoadCompanyCustomerDetails/$', 'myapp.commonViews.LoadCompanyCustomerDetailsView', name='LoadCompanyCustomerDetails'),#added by jihin for get global values
    url(r'^LoadInterviewQuestionBank/$', 'myapp.commonViews.LoadInterviewQuestionBankView', name='LoadInterviewQuestionBank'),#added by jihin for get global values
    url(r'^checkDomainExits/$', 'myapp.commonViews.checkDomainExitsView', name='checkDomainExits'),#added by jihin for check Domain Exits
    url(r'^FnLoadVerifiedCandidates/$', 'myapp.user.FnLoadVerifiedCandidates', name='FnLoadVerifiedCandidates'),
    url(r'^fnenrollSingleUser/$', 'myapp.user.fnenrollSingleUser', name='fnenrollSingleUser'),
    url(r'^fnenrollBulkUsers/$', 'myapp.user.fnenrollBulkUsers', name='fnenrollBulkUsers'),
    url(r'^saveAttendanceAlertSettings/$', 'myapp.globalSettings.saveAttendanceAlertSettings', name='saveAttendanceAlertSettings'),
    url(r'^updateOrderFormStatus/$', 'myapp.user.updateOrderFormStatusView', name='updateOrderFormStatus'),
    url(r'^setOrderFormConfOrNot/$', 'myapp.globalSettings.setOrderFormConfOrNot', name='setOrderFormConfOrNot'),
    url(r'^FetchCandidateReport/$', 'myapp.reports.FetchCandidateReport', name='FetchCandidateReport'),
    url(r'^fnLoadAllBatches4Report/$', 'myapp.reports.fnLoadAllBatches4Report', name='fnLoadAllBatches4Report'),
    url(r'^fnLoadBatchAttReport/$', 'myapp.reports.fnLoadBatchAttReport', name='fnLoadBatchAttReport'),
    url(r'^FetchCandidateRegisteredReport/$', 'myapp.reports.FetchCandidateRegisteredReport', name='FetchCandidateRegisteredReport'),
    url(r'^FetchAllQuestionBundles/$', 'myapp.questionBankReletedViews.FetchAllQuestionBundlesView', name='FetchAllQuestionBundles'),
    url(r'^ModifyQuestionBundles/$', 'myapp.questionBankReletedViews.ModifyQuestionBundlesView', name='ModifyQuestionBundles'),
    url(r'^FetchQuestionBankList/$', 'myapp.questionBankReletedViews.FetchQuestionBankListView', name='FetchQuestionBankList'),

    url(r'^fnSubmitAssignment/$', 'myapp.assignmentFunctions.fnSubmitAssignment', name='fnSubmitAssignment'),
    url(r'^fnAddToQuestionBank/$', 'myapp.interviewFunctions.fnAddToQuestionBank', name='fnAddToQuestionBank'),
    url(r'^fnDeleteFromQuestionBank/$', 'myapp.interviewFunctions.fnDeleteFromQuestionBank', name='fnDeleteFromQuestionBank'),

    url(r'^sendNewUserRegistrationMail/$', 'myapp.emailSms.sendNewUserRegistrationMail', name='sendNewUserRegistrationMail'), #by Lijin on 9-6-2015 for sending email notification on user reg.
    url(r'^sendBatchStatusUpdateMail/$', 'myapp.emailSms.sendBatchStatusUpdateMail', name='sendBatchStatusUpdateMail'), #by Lijin on 9-6-2015 for sending email notification on batch status update.
    url(r'^getUserCourseDetails4Sync/$', 'myapp.user.getUserCourseDetails4SyncView', name='getUserCourseDetails4Sync') #for bulk enrollment
)+ static('/files/', document_root=settings.FILEUPLOAD_PATH)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'Djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^GetUserPlan/$', 'myapp.views.GetUserPlanView', name='GetUserPlan'),#Arun
    url(r'^GetPlans/$', 'myapp.views.GetPlansView', name='GetPlans'),#Arun
    url(r'^GetFeatures/$', 'myapp.views.GetFeaturesView', name='GetFeatures'),#Arun
    url(r'^ChangeUserPlan/$', 'myapp.views.ChangeUserPlanView', name='ChangeUserPlan'),#Arun
    url(r'^EditPricing/$', 'myapp.views.EditPricingView', name='EditPricing'),#Arun
    url(r'^AddFeature/$', 'myapp.views.AddFeatureView', name='AddFeature'),#Arun
    url(r'^DeleteFeature/$', 'myapp.views.DeleteFeatureView', name='DeleteFeature'),#Arun
    url(r'^EditBilling/$', 'myapp.views.EditBillingView', name='EditBilling'),#Arun
    url(r'^FetchCurrentStatus/$', 'myapp.statusRelated.FetchCurrentStatusView', name='FetchCurrentStatus'),#Arun
    url(r'^SetStatus/$', 'myapp.statusRelated.SetStatusView', name='SetStatus'),#Arun
    url(r'^MultiRegister/$', 'myapp.RegisterRelated.MultiRegisterView', name='MultiRegister'),#Arun
    

    url(r'^loadHomeScreenMenu/$', 'myapp.homescreen.loadHomeScreenMenu', name='loadHomeScreenMenu'),#Lijin
    url(r'^saveHomeScreenMenu/$', 'myapp.homescreen.saveHomeScreenMenu', name='saveHomeScreenMenu'),#Lijin
    url(r'^loadUserNotifications/$', 'myapp.notification.loadUserNotifications', name='loadUserNotifications'),#Lijin 
    url(r'^markNotificationAsRead/$', 'myapp.notification.markNotificationAsRead', name='markNotificationAsRead'),#Lijin 
    url(r'^newNotification/$', 'myapp.notification.newNotification', name='newNotification'),#Lijin 

    url(r'^sendMessage/$', 'myapp.communications.sendMessage', name='sendMessage'),#Lijin
    url(r'^loadInbox/$', 'myapp.communications.loadInbox', name='loadInbox'),#Lijin
    url(r'^loadAllBranchesUnderCompany/$', 'myapp.branchRelatedView.loadAllBranchesUnderCompanyView', name='loadAllBranchesUnderCompany'),#Jihin 
    url(r'^loadMenteesBatchDetails/$', 'myapp.attendenceRelatedViews.loadMenteesBatchDetailsView', name='loadMenteesBatchDetails'),#Jihin
    url(r'^loadMenteeMarkedAttendanceFromBatch/$', 'myapp.attendenceRelatedViews.loadMenteeMarkedAttendanceFromBatchView', name='loadMenteeMarkedAttendanceFromBatch'),#Jihin  
    url(r'^loadInbox/$', 'myapp.communications.loadInbox', name='loadInbox'),#Lijin 
    url(r'^getUserName/$', 'myapp.communications.getUserName', name='getUserName'),#Lijin 
    url(r'^loadSingleMessage/$', 'myapp.communications.loadSingleMessage', name='loadSingleMessage'),#Lijin 
    url(r'^fnLoadParent/$', 'myapp.communications.fnLoadParent', name='fnLoadParent'),#Lijin 
    url(r'^loadAllBranchesUnderCompany/$', 'myapp.branchRelatedView.loadAllBranchesUnderCompanyView', name='loadAllBranchesUnderCompany')#Jihin 
)


