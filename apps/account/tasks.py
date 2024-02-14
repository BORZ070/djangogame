from celery import shared_task
from django.core.mail import send_mail


@shared_task
def uuid_checking_uuid_celery(instance):

    if True:
        email_subject = instance.user
        message = f'http://127.0.0.1:8000/account/uuid/{instance.uuid}/'
        from_email = 'xbox070@yandex.ru'
        email_manager = ['shdgit07@gmail.com']
        send_mail(email_subject, message, from_email, recipient_list=email_manager)