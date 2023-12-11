import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from tbot.models import TbotUserProfile
from tbot.views import tlink_views

#t.me/django_games_test_bot
token = settings.TGTOKEN
webhook = settings.TGWEBHOOK
bot = telebot.TeleBot(token)
def set_webhook(request):
    webhook_url = webhook
    bot.remove_webhook()
    bot.set_webhook(webhook_url)
    return HttpResponse(f'<h1> webhook_set OK on {webhook} </h1>')


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = telebot.types.Update.de_json(request.body.decode('utf-8'))
        bot.process_new_updates([update])
    return HttpResponse('<h1> bot_live </h1>')


@bot.message_handler(commands=['start'])
def start(message):
    text = message.text
    django_user_id = None
    try:
        message_text = text.split()
        django_user_id = message_text[1]
    except Exception as err:
        print(err)
    id = message.chat.id
    first_name = message.chat.first_name
    username = message.chat.username
    #testcode
    user_exists = TbotUserProfile.objects.filter(tuser_id=id).exists()
    print(user_exists)

    if django_user_id:
        if user_exists:
            tg_user = TbotUserProfile.objects.get(tuser_id=id)
            link_to_user_exists = tg_user.tuser_link_to_user
            if link_to_user_exists:
                pass
            else:
                tg_user.tuser_link_to_user_id = django_user_id
                tg_user.save()
        else:
            TbotUserProfile.objects.create(tuser_id=id,
                                           tuser_name=username,
                                           tuser_first_name=first_name,
                                           tuser_link_to_user_id=django_user_id,
                                           )
    else:
        if user_exists:
            pass
        else:
            TbotUserProfile.objects.create(tuser_id=id,
                                           tuser_name=username,
                                           tuser_first_name=first_name,
                                           )
    # if not user_exists:
    # try:
    #     TbotUserProfile.objects.create(tuser_id=id,
    #                                    tuser_name=username,
    #                                    tuser_first_name=first_name,
    #                                    tuser_link_to_user_id=django_user_id,
    #                                    )
    # except Exception as err:
    #     print(err)
    #
    bot.send_message(message.chat.id, f'Hello, {username}')
    print(django_user_id)

def send_tmessage(chat_id, text):
    bot.send_message(chat_id, text)







