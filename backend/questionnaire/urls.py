from django.urls import path
from . import views


# app_name allows for easier calling of url in html
app_name = "questionnaire"
# these are the url patterns for each page of the website
urlpatterns = [
    path("question", views.QuestionSerial.as_view(), name="questionView"),
    path("update_teacher",views.UpdateTeacher.as_view(),name="update_teacherView"),
    path("get_teacher", views.GetTeacher.as_view(), name="get_teacherInfo"),
    path("create_student",views.CreateStudent.as_view(),name="create_studentView"),
    path("update_student/<int:pk>/",views.UpdateStudent.as_view(),name="update_studentView"),
    path("delete_student/<int:pk>/",views.DeleteStudent.as_view(),name="delete_StudentView"),
    path("get_students",views.StudentSerial.as_view(),name="students_listView"),
    path("get_student/<int:pk>/",views.IndividualStudentSerial.as_view(), name="student_view"),
    path("get_student_forms/<int:pk>/",views.FormsSerial.as_view(),name="form_listView"),
    path("get_form/<int:pk>/",views.IndividualFormSerial.as_view(),name="individualform_view"),
    path("answer",views.AnswerSerial.as_view(),name="answersView"),
    path("create_form",views.CreateForm.as_view(),name="create_formView"),
    path("get_form_csv/<int:pk>/",views.FormCSV.as_view(),name="get_form_csvView"),
    path('change-password', views.ChangePasswordView.as_view(), name='change-password'),
    path('resend_verification', views.ResendValidationEmail.as_view(), name="Resend_Verification"),
    path('admin_csv_forms',views.AdminFormCSV.as_view(),name="admin_form_csv"),
    
]
