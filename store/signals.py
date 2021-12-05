from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Box


# TODO: delete the signal.py
@receiver(pre_save, sender=Box)
def student_otp(sender, instance, **kwargs):
    instance.area = 2 * (instance.length + instance.width + instance.height)
    instance.volume = (instance.length * instance.width * instance.height)
