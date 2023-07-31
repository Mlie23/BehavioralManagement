from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from .models import Teacher

from .serializers import TeacherCreateSerializer

@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = email_address.user
    if not Teacher.objects.filter(user=user.id).exists():
        Teacher.objects.create(user=user)
    user_teacher = Teacher.objects.get(user=user.id)
    user_teacher.email_verified = True
    user_teacher.save()