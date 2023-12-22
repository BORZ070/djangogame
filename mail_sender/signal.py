from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from mail_sender.models import MailForAllUser
from mail_sender.tasks import send_mails_all_user_celery


@receiver(post_save, sender=MailForAllUser)
def send_mails_all_user(sender, instance, created, **kwargs):

    # for _ in range(10001):
    #     if True:
    #         email_subject = instance.title
    #         message = instance.text
    #         from_email = 'xbox070@yandex.ru'
    #         email_manager = ['shdgit07@gmail.com']
    #         send_mail(email_subject, message, from_email, recipient_list=email_manager)
    instance = MailForAllUser.objects.get(id=instance.id)
    send_mails_all_user_celery.delay(instance)