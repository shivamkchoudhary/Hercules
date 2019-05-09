from telegram import ChatAction
import html
import urllib.request
import re
import json
from typing import Optional, List
import time
import urllib
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from IHbot import dispatcher
from IHbot.__main__ import STATS, USER_INFO
from IHbot.modules.disable import DisableAbleCommandHandler

def boobs(bot: Bot, update: Update):
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    final = "http://media.oboobs.ru/{}".format(nsfw)
    update.message.reply_photo(final)
		
BOOBS_HANDLER = DisableAbleCommandHandler("boobs", boobs)
dispatcher.add_handler(BOOBS_HANDLER)
