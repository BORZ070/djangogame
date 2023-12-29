from celery import shared_task
from tbot.models import TbotUserProfile
from tbot.bot import bot

@shared_task()
def send_spam(title, text, link_image):
    all_tgusers = TbotUserProfile.objects.all()
    message = f'{title}\n{text}'
    with open(link_image, 'rb') as file:
        photo = file.read()
    for tguser in all_tgusers:
        chat_id = tguser.tuser_id
        bot.send_photo(chat_id=chat_id, caption=message, photo=photo, parse_mode='Markdown')




