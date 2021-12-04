from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Box

#TODO: delete the signal.py
# @receiver(pre_save, sender=Box)
# def student_otp(sender, instance, **kwargs):
#     # instance.otp = random.randrange(10101, 909090)
#     instance.area=2*(instance.lenght+instance.width+instance.height)
#     # create_or_update_user(instance)
#     # broadcast_sms(instance.phone_number, content)
