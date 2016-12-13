#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import netifaces
import subprocess
from unidecode import unidecode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
path = "/home/pi/madmug/"

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('/start')
    update.message.reply_text('/ip')
    update.message.reply_text('/msg_once')
    update.message.reply_text('/msg_print')
    update.message.reply_text('/msg_ip')
    update.message.reply_text('/msg')
    update.message.reply_text('/time')
    update.message.reply_text('/stop_all')

def msg_print(bot, update, args):
    update.message.reply_text("Message will be print [" + " ".join(args) + "]")
    cmd = path + "print_message.sh"
    args.insert(0, unidecode(update.message.from_user.first_name))
    args.insert(0, cmd)
    subprocess.Popen(args)
    update.message.reply_text("Done!")


def ip(bot, update):
    update.message.reply_text('IP:' + netifaces.ifaddresses("wlan0")[netifaces.AF_INET][0]["addr"])

def msg_once(bot, update, args):
    update.message.reply_text("Message will be shown [" + " ".join(args) + "]")
    #cmd = "/home/pi/Pimoroni/scrollphat/write_message.sh"
    cmd = path + "write_message.sh"
    args.insert(0, cmd)
    #subprocess.Popen(unidecode(u" ".join(args)))
    subprocess.Popen(args)
    update.message.reply_text("Done!")

def msg_ip(bot, update):
    #cmd = "/home/pi/Pimoroni/scrollphat/write_message.sh"
    cmd = path + "write_message.sh"
    ip = netifaces.ifaddresses("wlan0")[netifaces.AF_INET][0]["addr"]
    cmd_list = []
    cmd_list.append(cmd)
    cmd_list.append(ip)
    subprocess.Popen(cmd_list)
    update.message.reply_text('IP: [' + ip +'] is shown.')

def msg(bot, update, args):
    update.message.reply_text("Message [" + " ".join(args) + "] will always be shown")
    #cmd = "/home/pi/Pimoroni/scrollphat/write_message_always.sh"
    cmd = path + "write_message_always.sh"
    args.insert(0, cmd)
    subprocess.Popen(args)
    update.message.reply_text("Done!")

def time(bot, update):
    update.message.reply_text("Screen will show time")
    #cmd = "/home/pi/Pimoroni/scrollphat/time.sh"
    cmd = path + "time.sh"
    subprocess.Popen([cmd])
    update.message.reply_text("Done!")

def stop_all(bot, update):
    update.message.reply_text("Every scrollphat process will stop")
    #cmd = "/home/pi/Pimoroni/scrollphat/stop_all.sh"
    cmd = path + "stop_all.sh"
    subprocess.Popen([cmd])
    update.message.reply_text("Stoped!")
    #cmd = "/home/pi/Pimoroni/scrollphat/clear_screen.sh"
    cmd = path + "clear_screen.sh"
    subprocess.Popen([cmd])
    update.message.reply_text("Cleared!")

def echo(bot, update):
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ip", ip))
    dp.add_handler(CommandHandler("msg_ip", msg_ip))
    dp.add_handler(CommandHandler("msg_once", msg_once, pass_args=True))
    dp.add_handler(CommandHandler("msg_print", msg_print, pass_args=True))
    dp.add_handler(CommandHandler("msg", msg, pass_args=True))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("stop_all", stop_all))
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    # log all errors
    dp.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
