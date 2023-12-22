from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mails_all_user_celery(instance):

    for _ in range(10001):
        if True:
            email_subject = instance.title
            message = instance.text
            from_email = 'xbox070@yandex.ru'
            email_manager = ['shdgit07@gmail.com']
            send_mail(email_subject, message, from_email, recipient_list=email_manager)

