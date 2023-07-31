from .models import Teacher, Question, Result, Student, Answer, Form, Custom_Strategy
from rest_framework import serializers
from django.contrib.auth.models import User
from dj_rest_auth.serializers import LoginSerializer
from django.conf import settings

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    next_question = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializers(serializers.ModelSerializer):
    # use source for related questions
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True,source="this_question")

    class Meta:
        model = Question
        fields = "__all__"


class ResultSerializers(serializers.ModelSerializer):
    answer = serializers.SlugRelatedField(many=True, read_only=True, slug_field="text")
    question = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="text"
    )

    class Meta:
        model = Result
        fields = ["question", "answer"]


class minimalAnswerSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    strength =              serializers.CharField(source='strength.strength',allow_blank=True, allow_null=True)
    locations =             serializers.CharField(source='location.location',allow_blank=True, allow_null=True)       
    setting =               serializers.CharField(source='setting.setting',allow_blank=True, allow_null=True)
    trigger =               serializers.CharField(source='trigger.trigger',allow_blank=True, allow_null=True)
    behavior =              serializers.CharField(source='behavior.behavior',allow_blank=True, allow_null=True)
    consequence =           serializers.CharField(source='consequence.consequence',allow_blank=True, allow_null=True)
    setting_strategy =      serializers.CharField(source='setting_strategy.setting_strategy',allow_blank=True, allow_null=True)
    trigger_strategy =      serializers.CharField(source='trigger_strategy.trigger_strategy',allow_blank=True, allow_null=True)
    behavior_strategy =     serializers.CharField(source='behavior_strategy.behavior_strategy',allow_blank=True, allow_null=True)
    consequence_strategy =  serializers.CharField(source='consequence_strategy.consequence_strategy',allow_blank=True, allow_null=True)

    class Meta:
        model = Answer
        fields = ["id", "question", "text","strength","locations","setting","trigger","behavior","consequence","setting_strategy",
                  "trigger_strategy","behavior_strategy","consequence_strategy"]

class customStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom_Strategy
        fields = ["id","strategy_type","text"]

class FormSerializer(serializers.ModelSerializer):
    answers = minimalAnswerSerializer(many=True, read_only=True)
    other_answer = customStrategySerializer(many=True, read_only=True)
    class Meta:
        model = Form
        fields = ["id", "date", "student", "answers","other_answer"]

class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["id", "date", "student"]

class CreateFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["student"]


class StudentSerializers(serializers.ModelSerializer):
    # result = ResultSerializers(many=True, read_only=True)
    # form = FormSerializer(many=True,read_only=True,source='form_set')

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "student_id",
            "teacher",
            "grade",
            "gender",
            "IEP",
            "date_of_birth",
            # "result",
            # "saved_result",
            # "form"
        ]


class GetStudentsSerializer(serializers.ModelSerializer):
    form_count = serializers.SerializerMethodField()
    class Meta:
        model= Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "student_id",
            "form_count"
        ]
    # function to get form count
    def get_form_count(self, instance):
        form_count = Form.objects.filter(student=instance.pk)
        return len(form_count)

class GetTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields=[
            "first_name",
            "last_name",
            "school",
        ]

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.school = validated_data.get("school", instance.school)
        instance.save()
        return instance


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.grade = validated_data.get("grade", instance.grade)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.IEP = validated_data.get("IEP", instance.IEP)
        instance.save()
        return instance


from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        user = self.get_auth_user(username, email, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)
        
        # teacher = Teacher.objects.get(user=user)
        # if teacher.email_verified == False:
        #     msg = _('Your email is not verified. Please verify')
        #     raise exceptions.ValidationError(msg)
        # print("Try this",self.validate_email_verification_status(user))
        # Did we get back an active user?
        # print(self.validate_auth_user_status(user))
        if self.validate_auth_user_status(user) == False:
            raise exceptions.ValidationError("Your E-mail Is not Verified, Please verify")

        # If required, is the email verified?
        if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
            self.validate_email_verification_status(user)

        attrs['user'] = user
        return attrs

# ## Token adjustment. Don't touch.
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         token['username'] = user.username

#         return token
