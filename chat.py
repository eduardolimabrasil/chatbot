from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

def start(bot, update):
    me = bot.get_me()
    update.message.reply_text("olá {1}, eu sou {0}".format(me.username, update.message.from_user.name))

def convert_uppercase(bot, update):
    update.message.reply_text("Você disse:"+update.message.text)

def main():
    # Create Updater object and attach dispatcher to it
    updater = Updater(os.environ.get('TOKEN'))
    dispatcher = updater.dispatcher
    print("Bot started")

    # Add command handler to dispatcher
    start_handler = CommandHandler('start',start)
    upper_case = MessageHandler(Filters.text, convert_uppercase)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(upper_case)
    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()