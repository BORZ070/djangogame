from django.dispatch import receiver
from django.db.models.signals import post_save

from tbot.bot import send_tmessage
from tbot.models import SupportQ, TSpam, WebhookLink
from tbot.tasks import send_spam
from tbot.bot import auto_set_webhook


@receiver(post_save, sender=SupportQ)
def send_mails(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        data = instance.data
        question = instance.question
        chat_id = 1834541260
        text = f'**Новое сообщение в службу поддержки**\n{email}\n{question}'
        send_tmessage(chat_id, text)

@receiver(post_save, sender=TSpam)
def tspam(instance, created, **kwargs):
        if True:
            title = instance.title
            text = instance.text
            link_image = instance.image.path
            send_spam.delay(title, text, link_image)


@receiver(post_save, sender=WebhookLink)
def webhook_send(instance, created, **kwargs):
    link = instance.link
    link_full = f'{link.strip}/tbot/webhook/'
    auto_set_webhook(link_full)



