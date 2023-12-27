from celery import shared_task
from tbot.models import TbotUserProfile
from tbot.bot import bot

def send_spam():
    all_tgusers = TbotUserProfile.objects.all()
    list_chat_id = []
    for tguser in all_tgusers:
        chat_id = tguser.tuser_id
        list_chat_id.append(chat_id)
    print(list_chat_id)
    for chat_id in list_chat_id:
        # bot.send_photo(chat_id=chat_id, caption=)
        