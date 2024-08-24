import telebot
import webbrowser

bot = telebot.TeleBot("7412430099:AAGuQWI6dnWEufE0hZCBtP4I3yUNptdBe9Y")

first_but=telebot.types.InlineKeyboardButton("جەنالی خوم🙂💯",url="https://t.me/f_0_x404")
se_but=telebot.types.InlineKeyboardButton("ئەکاونتی خوم🎭🛡️",url="https://t.me/f_o_x404")
s_but=telebot.types.InlineKeyboardButton("ئەکاونتی خوم🎭🛡️",url="https://t.me/f_o_x404")
e_but=telebot.types.InlineKeyboardButton("ئەکاونتی خوم🎭🛡️",url="https://t.me/f_o_x404")
markup=telebot.types.InlineKeyboardMarkup(row_width=2)
markup=telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(first_but,se_but,s_but,e_but)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"بەخێر بێی بو باشترین بوتی تلیگرام 🛡️❤️",reply_markup=markup)
@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id,"chune ch keshat haya",)


@bot.message_handler(func=lambda message:True)
def echo_all(message):
    bot.reply_to(message,message.text)
bot.polling()