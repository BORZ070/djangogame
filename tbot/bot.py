import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#t.me/django_games_test_bot
token = '6783897789:AAF0J26XI-tEseNmlhT0z0_cGYhC1Wxodzc'
webhook = 'https://5890-5-144-117-45.ngrok-free.app/tbot/webhook/'
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
    bot.send_message(message.chat.id, 'Hello')
    id = message.chat.id
    first_name = message.chat.first_name
    username = message.chat.username
    


