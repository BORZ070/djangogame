import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tbot.models import TbotUserProfile

#t.me/django_games_test_bot
token = '6783897789:AAF0J26XI-tEseNmlhT0z0_cGYhC1Wxodzc'
webhook = 'https://149c-5-144-123-244.ngrok-free.app/tbot/webhook/'
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
    id = message.chat.id
    first_name = message.chat.first_name
    username = message.chat.username
    #testcode
    user_exists = TbotUserProfile.objects.filter(tuser_id=id).exists()
    print(user_exists)
    # if not user_exists:
    try:
        TbotUserProfile.objects.create(tuser_id=id,
                                       tuser_name=username,
                                       tuser_first_name=first_name,
                                       )
    except Exception as err:
        print(err)

    bot.send_message(message.chat.id, f'Hello, {username}')

def send_tmessage(chat_id, text):
    bot.send_message(chat_id, text, parse_mode='Markdown')







