from urllib import request
from .serializers import (
    QuestionSerializers,
    AnswerSerializer,
    StudentCreateSerializer,
    StudentSerializers,
    TeacherCreateSerializer,
    CreateFormSerializer,
    FormSerializer,
    FormsSerializer,
    GetStudentsSerializer,
    GetTeacherSerializer,
    ChangePasswordSerializer,
)
from .models import Question, Student, Teacher, Form, Answer, Custom_Strategy
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseBadRequest
import csv


User = get_user_model()
def is_user_email_verified(user, email):
    """
    returns True if EmailAddress exists and is already verified, otherwise returns False
    """
    result = False
    try:
        emailaddress = EmailAddress.objects.get_for_user(user, email)
        result = emailaddress.verified
    except EmailAddress.DoesNotExist:
        pass
    return result

# Reference: https://github.com/pennersr/django-allauth/issues/2980#issuecomment-972883246
class ResendValidationEmail(APIView):
    """
    Implement requests to manually send confirmation email in case it hasn't been received
    """

    def post(self, request, *args, **kwargs):
        """
        request for validation email sending
        """
        payload = json.loads(request.body)
        email = payload.get('email')
        if email is None:
            return HttpResponseBadRequest("No email provided")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # avoid leaking information about user existence
            return HttpResponse(status=200)

        if not is_user_email_verified(user, email):
            send_email_confirmation(request, user, email)
            return HttpResponse(status=200)
        elif is_user_email_verified(user, email):
            return HttpResponse("Email has been verified",status=403)


    
# Create your views here.
class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"Old Password is wrong"}, status=status.HTTP_400_BAD_REQUEST
                )
            # Check if old password match new password
            elif serializer.data.get("old_password") == serializer.data.get(
                "new_password"
            ):
                return Response(
                    {"New Password Cannot Match Old Password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionSerial(generics.ListAPIView):
    queryset = Question.objects.order_by("question_number").all()
    serializer_class = QuestionSerializers


class AnswerSerial(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class StudentSerial(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        return Student.objects.filter(teacher=user)
        # return Student.objects.all()

    # serializer_class = StudentSerializers
    serializer_class = GetStudentsSerializer


class IndividualStudentSerial(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        input = self.kwargs["pk"]
        return Student.objects.filter(id=input)

    serializer_class = StudentSerializers


class FormsSerial(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # check if the student is related to this teacher
        input = self.kwargs["pk"]
        return Form.objects.filter(student=input)

    serializer_class = FormsSerializer


class IndividualFormSerial(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # check if the student is related to this teacher
        input = self.kwargs["pk"]
        curr_form = Form.objects.filter(id=input)
        if curr_form[0].student.teacher != self.request.user:
            return Form.objects.filter(id=-1) # return empty queryset if teacher isn't user
        
        
        return curr_form

    serializer_class = FormSerializer


class UpdateTeacher(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user.id
        request_data = request.data.copy()
        request_data["user"] = user
        if Teacher.objects.filter(user=user).exists():
            existing_teacher = Teacher.objects.get(user=user)
            serializer = TeacherCreateSerializer(existing_teacher, data=request_data)
            serializer.is_valid()
            if serializer.is_valid():
                new_teacher = serializer.save()
                new_teacher.save()
                return Response("Teacher's information is updated", status.HTTP_200_OK)
            else:
                return Response(str(serializer.errors), status.HTTP_400_BAD_REQUEST)
        else:
            # assume teacher has not been created yet for this user
            serializer = TeacherCreateSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    "Teacher's information is created", status.HTTP_201_CREATED
                )
            else:
                return Response(str(serializer.errors), status.HTTP_400_BAD_REQUEST)


class GetTeacher(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user.id
        if Teacher.objects.filter(user=user).exists():
            final_teacher_object = GetTeacherSerializer(
                Teacher.objects.filter(user=user).get()
            )
            return Response(final_teacher_object.data, status=status.HTTP_200_OK)
        else:
            return Response(
                "Please create teacher info", status=status.HTTP_404_NOT_FOUND
            )

    # serializer_class = GetTeacherSerializer


class UpdateStudent(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user.id
        request_data = request.data.copy()
        pk = self.kwargs["pk"]
        if Student.objects.filter(teacher=user).exists():
            existing_student = Student.objects.get(pk=pk)
            serializer = StudentCreateSerializer(existing_student, data=request_data)
            serializer.is_valid()
            if serializer.is_valid():
                serializer.save()
                return Response("Student's information is updated", status.HTTP_200_OK)
            else:
                return Response(str(serializer.errors), status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Bad request", status.HTTP_400_BAD_REQUEST)

    serializer_class = StudentSerializers


class CreateStudent(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user.id
        request_data = request.data.copy()
        request_data["teacher"] = user
        create_new_student = request_data.get("create_new_student", True)
        if not create_new_student:
            pass
            # Not yet implemented
            # existing_teacher = Teacher.objects.get(user=user)
            # serializer = TeacherCreateSerializer(existing_teacher, data=request_data)
            # serializer.is_valid()
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response("Teacher's information is updated", status.HTTP_200_OK)
            # else:
            #     return Response(str(serializer.errors), status.HTTP_400_BAD_REQUEST)
        else:
            # assume teacher has not been created yet for this user
            # first_name = request_data.get("first_name")
            # last_name = request_data.get("last_name")
            # date_of_birth = request_data.get("date_of_birth")
            # student_id = request_data.get("student_id")
            # grade = request_data.get("grade")
            # gender = request_data.get("gender")
            # print(first_name,last_name,date_of_birth, student_id, grade, gender)
            # student_exist = (Student.objects.filter(first_name = first_name, last_name = last_name, date_of_birth=date_of_birth,
            #                        student_id=student_id, grade=grade, gender=gender))
            # print(student_exist, 0)
            serializer = StudentCreateSerializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    "Student's information is created", status.HTTP_201_CREATED
                )
            else:
                return Response(str(serializer.errors), status.HTTP_400_BAD_REQUEST)


class DeleteStudent(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        user = request.user.id
        pk = self.kwargs["pk"]
        if Student.objects.filter(teacher=user, pk=pk).exists():
            forms = Form.objects.filter(pk=pk)
            if len(forms) > 0:
                form_objects = Form.objects.get(pk=pk)
                form_objects.delete()
            student_object = Student.objects.get(pk=pk)
            student_object.delete()
            return Response("Ok", status=status.HTTP_200_OK)


class DeleteForm(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, pk):
        pk = self.kwargs["pk"]
        form_objects = Form.objects.get(pk=pk)
        form_objects.delete()
        return Response("Ok", status=status.HTTP_200_OK)


class CreateForm(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # input should be
    # {
    # student: 1(studentid)

    # answer: [1,2,4,51,23,2,...]
    # other_answer_type = {1:"custom answer for answer #1",}
    # }
    def post(self, request):
        user = request.user.id
        new_data = {}
        new_data["student"] = int(request.data["student"])
        serializer = CreateFormSerializer(data=new_data)
        if (
            serializer.is_valid()
            and Student.objects.get(pk=new_data["student"]).teacher.pk == user
        ):
            new_form = Form.objects.create(**serializer.validated_data)
            # answer should be [1,2,4,...] in id
            new_form.answers.set(request.data["answers"])
            # custom_answers = {1:"sdfsdf"}
            list_of_custom_strats = []
            # custom_answer_dictionary = json.loads(request.data['custom_answers'])
            for keys,value in request.data['custom_answers'].items():
                if value == []:
                    continue
                curr_strategy_type = Answer.objects.get(pk=keys).other_type
                new_custom_strat = Custom_Strategy.objects.create(strategy_type=curr_strategy_type,text=value)
                list_of_custom_strats.append(new_custom_strat.pk)
            new_form.other_answer.set(list_of_custom_strats)


            return Response("Form has been created", status.HTTP_201_CREATED)
        else:
            return Response(str(serializer.errors), status.HTTP_400_BAD_REQUEST)


class FormCSV(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = request.user.id
        pk = self.kwargs["pk"]

        if not Form.objects.filter(pk=pk).exists():
            return Response("Form does not exist", status=status.HTTP_404_NOT_FOUND)
        current_form = Form.objects.filter(pk=pk).get()

        # check who form belongs to
        current_student = current_form.student

        if not current_student.teacher.pk == user:
            return Response(
                "This form's student does not belong to you",
                status=status.HTTP_401_UNAUTHORIZED,
            )

        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="export_{current_student.first_name}_{current_student.last_name}_{pk}.csv"'
        writer = csv.DictWriter(
            response,
            fieldnames=[
                "question",
                "answer",
                "strength",
                "locations",
                "setting",
                "trigger",
                "behavior",
                "consequence",
                "setting_strategy",
                "trigger_strategy",
                "behavior_strategy",
                "consequence_strategy",
            ],
        )
        writer.writeheader()
        answers = current_form.answers.all()

        for ans in answers:
            writer.writerow(
                {
                    "question": ans.question if ans.question else "",
                    "answer": ans.text if ans.text else "",
                    "strength": ans.strength.strength if ans.strength else "",
                    "locations": ans.locations.location if ans.locations else "",
                    "setting": ans.setting.setting if ans.setting else "",
                    "trigger": ans.trigger.trigger if ans.trigger else "",
                    "behavior": ans.behavior.behavior if ans.behavior else "",
                    "consequence": ans.consequence.consequence
                    if ans.consequence
                    else "",
                    "setting_strategy": ans.setting_strategy.setting_strategy
                    if ans.setting_strategy
                    else "",
                    "trigger_strategy": ans.trigger_strategy.trigger_strategy
                    if ans.trigger_strategy
                    else "",
                    "behavior_strategy": ans.behavior_strategy.behavior_strategy
                    if ans.behavior_strategy
                    else "",
                    "consequence_strategy": ans.consequence_strategy.consequence_strategy
                    if ans.consequence_strategy
                    else "",

                }
            )
        custom_answers = current_form.other_answer.all()
        for ans in custom_answers:
            writer.writerow(
                {
                    str(ans.strategy_type) : str(ans.text)
                    

                }
            )

        return response


class AdminFormCSV(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk):
        forms = Form.objects.all()
        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="export_file.csv"'
        writer = csv.DictWriter(
            response,
            fieldnames=[
                "student_name",
                "teacher_name",
                "school",
                "date",
                "strength",
                "locations",
                "setting",
                "trigger",
                "behavior",
                "consequence",
                "setting_strategy",
                "trigger_strategy",
                "behavior_strategy",
                "consequence_strategy",
            ],
        )
        writer.writeheader()
        for form in forms:
            
            student_name = f"{form.student.first_name} {form.student.last_name}"
            teacher = Teacher.objects.get(user=form.student.teacher)
            teacher_name = f"{teacher.first_name} {teacher.last_name}"
            school = f"{teacher.school}"
            date = f"{str(form.date)}"
            answers = form.answers.all()
            strength = []
            locations = []
            settings = []
            trigger = []
            behavior = []
            consequence = []
            setting_strategy = []
            trigger_strategy = []
            behavior_strategy = []
            consequence_strategy = []
            answers_text = []

            for ans in answers:
                strength.append(ans.strength.strength if ans.strength else "")
                locations.append(ans.locations.location if ans.locations else "")
                settings.append(ans.setting.setting if ans.setting else "")
                trigger.append(ans.trigger.trigger if ans.trigger else "")
                behavior.append(ans.behavior.behavior if ans.behavior else "")
                consequence.append(ans.consequence.consequence
                        if ans.consequence
                        else "")
                setting_strategy.append(ans.setting_strategy.setting_strategy
                        if ans.setting_strategy
                        else "")
                trigger_strategy.append(ans.trigger_strategy.trigger_strategy
                        if ans.trigger_strategy
                        else "")
                behavior_strategy.append(ans.behavior_strategy.behavior_strategy
                        if ans.behavior_strategy
                        else "")
                consequence_strategy.append(ans.consequence_strategy.consequence_strategy
                        if ans.consequence_strategy
                        else "")
                answers_text.append(f"{ans.text}")
                
            def delete_empty(text):
                if text == "":
                    return False
                return True
            writer.writerow(
                {
                    "student_name": student_name,
                    "teacher_name": teacher_name,
                    "school": school,
                    "date": date,
                    "strength": ''.join(filter(delete_empty,strength)),
                    "locations": ''.join(filter(delete_empty,locations)),
                    "setting": ''.join(filter(delete_empty,settings)),
                    "trigger": ''.join(filter(delete_empty,trigger)),
                    "behavior": ''.join(filter(delete_empty,behavior)),
                    "consequence": ''.join(filter(delete_empty,consequence)),
                    "setting_strategy": ''.join(filter(delete_empty,setting_strategy)),
                    "trigger_strategy": ''.join(filter(delete_empty,trigger_strategy)),
                    "behavior_strategy": ''.join(filter(delete_empty,behavior_strategy)),
                    "consequence_strategy": ''.join(filter(delete_empty,consequence)),
                    "answers": ''.join(filter(delete_empty,answers_text))
                }
            )

        return response
