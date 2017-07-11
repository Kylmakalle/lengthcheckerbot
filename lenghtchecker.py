import telebot
import os

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Отправь или перешли мне заявку, которую нужно проверить.')


@bot.message_handler(content_types=['text'])
def check_message(message):
    if len(message.text) > 26:
        bot.reply_to(message,
                     '❌ Длина заявки превышает 26 символов ❌\n\nТребуется сократить заявку на `{}` симв.'.format(
                         len(message.text) - 26), parse_mode='Markdown')
    else:
        bot.reply_to(message, '✅ Длина заявки не превышает 26 символов ✅')


bot.polling(none_stop=True)
