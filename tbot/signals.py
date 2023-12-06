from django.dispatch import receiver
from django.db.models.signals import post_save

from tbot.bot import send_tmessage
from tbot.models import SupportQ


@receiver(post_save, sender=SupportQ)
def send_mails(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        data = instance.data
        question = instance.question
        chat_id = 1834541260
        text = f'**Новое сообщение в службу поддержки**\n{email}\n{question}'
        send_tmessage(chat_id, text)


        # email_subject = 'заявка'
        # message = f'новая заявка от {email}, {data}, {question}'
        # from_email = 'xbox070@yandex.ru'
        # email_manager = ['shdgit07@gmail.com']
        # send_mail(email_subject, message, from_email)



