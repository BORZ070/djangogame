import telebot
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from tbot.models import TbotUserProfile
from tbot.views import tlink_views
from telebot import types

from articles.models import Article
from games.models import Game,Genre
from account.models import Profile

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

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton('articles')
    item_2 = types.KeyboardButton('games')
    item_3 = types.KeyboardButton('library')
    item_4 = types.KeyboardButton('profile')
    item_5 = types.KeyboardButton('genre')
    markup.row(item_1, item_2, item_5)
    markup.row(item_3, item_4)

    bot.send_message(message.chat.id, f'Hello, {username}', reply_markup=markup)
    print(django_user_id)


@bot.message_handler(func=lambda message: message.text == 'articles')
def item_1(message):
    articles = Article.objects.all()
    for article in articles:
        answer = f'{article.title}\nhttp://127.0.0.1:8000/{article.get_absolute_url()}'
        bot.send_message(message.chat.id, answer)



@bot.message_handler(func=lambda message: message.text == 'games')
def item_2(message):
    games = Game.objects.all()
    for game in games:
        answer = f'{game.name}\nhttp://127.0.0.1:8000/{game.get_absolute_url()}'
        bot.send_message(message.chat.id, answer)



@bot.message_handler(func=lambda message: message.text == 'library')
def item_3(message):
    # answer = 'you press button library'
    games = Game.objects.all()
    for game in games:
        answer = f'{game.name}\nhttp://127.0.0.1:8000/{game.get_absolute_url()}'
        bot.send_message(message.chat.id, answer)


@bot.message_handler(func=lambda message: message.text == 'profile')
def item_4(message):
    username = message.chat.username

    chat_id= message.chat.id
    tguser = TbotUserProfile.objects.get(tuser_id=chat_id)
    site_id = tguser.tuser_link_to_user_id
    site_user = User.objects.get(id=site_id)

    site_username = site_user.username
    email = site_user.email

    answer = f'TG_name: "{username}"\nSite_name: "{site_username}"\nEmail: "{email}"'

    bot.send_message(message.chat.id, answer)

@bot.message_handler(func=lambda message: message.text == 'genre')
def item_5(message):
    genres = Genre.objects.all()
    markup = types.InlineKeyboardMarkup()
    for genre in genres:
        button = types.InlineKeyboardButton(genre.genre, callback_data='xxx')
        markup.add(button)
    answer = 'Выберите жанр'
    bot.send_message(message.chat.id, answer, reply_markup=markup)
def send_tmessage(chat_id, text):
    bot.send_message(chat_id, text)







