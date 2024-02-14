from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.models import Profile
from account.tasks import uuid_checking_uuid_celery


@receiver(post_save, sender=Profile.uuid)
def uuid_checking_uuid(sender, instance, created, **kwargs):

    uuid_checking_uuid_celery.delay()

