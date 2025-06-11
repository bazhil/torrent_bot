import json
import re
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging


from config import get_config


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


config = get_config()


def target_search(update, context):
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    bot.sendMessage(chat_id, 'Здесь будет реализован адресный поиск')


def subcategory(update, context):
    global SUBCATEGORY
    bot = context.bot
    chat_id = update.callback_query.message.chat.id

    no_subcategory_text = """Сперва необходимо выбрать категорию. Сделать это можно в меню"""

    if CATEGORY == None:
        bot.sendMessage(chat_id, no_subcategory_text)

    with open(config.categories_dict, 'r', encoding='utf-8') as dictionary:
        d = json.load(dictionary)
        ctgs = [x for i, x in enumerate(d)]
        subcategories = d[CATEGORY]
        if len(subcategories) == 0:
            SUBCATEGORY = None
            text = """У категории ({}) нет подкатегорий. Перенаправляю вас на адресный поиск."""
            bot.sendMessage(chat_id, text)
            target_search(update, context)
            return

    keyboard = []

    for sbct in subcategories:
        clean_sbct = sbct.replace("'", "\'")
        clbk = '.{}-{}'.format(ctgs.index(CATEGORY), subcategories.index(sbct))
        keyboard.append([InlineKeyboardButton(clean_sbct, callback_data=clbk)])
    keyboard.append([InlineKeyboardButton('Назад', callback_data='back')])

    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.sendMessage(chat_id, 'Выберите подкатегорию: ', reply_markup=reply_markup)


def category_handler(update, context):
    global CATEGORY

    with open(config.categories_dict, 'r', encoding='utf-8') as dict:
        d = json.load(dict)
        ctgs = [x for i, x in enumerate(d)]

    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    data = update.callback_query.data

    if int(data) in list(range(117)):
        CATEGORY = ctgs[int(data)]
        bot.sendMessage(chat_id, 'Выбрана категория: {}'.format(CATEGORY))
    subcategory(update, context)


category_handlers = [
    CallbackQueryHandler(category_handler, pattern=re.compile('0')),
    CallbackQueryHandler(category_handler, pattern=re.compile('1')),
    CallbackQueryHandler(category_handler, pattern=re.compile('2')),
    CallbackQueryHandler(category_handler, pattern=re.compile('3')),
    CallbackQueryHandler(category_handler, pattern=re.compile('4')),
    CallbackQueryHandler(category_handler, pattern=re.compile('5')),
    CallbackQueryHandler(category_handler, pattern=re.compile('6')),
    CallbackQueryHandler(category_handler, pattern=re.compile('7')),
    CallbackQueryHandler(category_handler, pattern=re.compile('8')),
    CallbackQueryHandler(category_handler, pattern=re.compile('9')),
    CallbackQueryHandler(category_handler, pattern=re.compile('10')),
    CallbackQueryHandler(category_handler, pattern=re.compile('11')),
    CallbackQueryHandler(category_handler, pattern=re.compile('12')),
    CallbackQueryHandler(category_handler, pattern=re.compile('13')),
    CallbackQueryHandler(category_handler, pattern=re.compile('14')),
    CallbackQueryHandler(category_handler, pattern=re.compile('15')),
    CallbackQueryHandler(category_handler, pattern=re.compile('16')),
    CallbackQueryHandler(category_handler, pattern=re.compile('17')),
    CallbackQueryHandler(category_handler, pattern=re.compile('18')),
    CallbackQueryHandler(category_handler, pattern=re.compile('19')),
    CallbackQueryHandler(category_handler, pattern=re.compile('20')),
    CallbackQueryHandler(category_handler, pattern=re.compile('21')),
    CallbackQueryHandler(category_handler, pattern=re.compile('22')),
    CallbackQueryHandler(category_handler, pattern=re.compile('23')),
    CallbackQueryHandler(category_handler, pattern=re.compile('24')),
    CallbackQueryHandler(category_handler, pattern=re.compile('25')),
    CallbackQueryHandler(category_handler, pattern=re.compile('26')),
    CallbackQueryHandler(category_handler, pattern=re.compile('27')),
    CallbackQueryHandler(category_handler, pattern=re.compile('28')),
    CallbackQueryHandler(category_handler, pattern=re.compile('29')),
    CallbackQueryHandler(category_handler, pattern=re.compile('30')),
    CallbackQueryHandler(category_handler, pattern=re.compile('31')),
    CallbackQueryHandler(category_handler, pattern=re.compile('32')),
    CallbackQueryHandler(category_handler, pattern=re.compile('33')),
    CallbackQueryHandler(category_handler, pattern=re.compile('34')),
    CallbackQueryHandler(category_handler, pattern=re.compile('35')),
    CallbackQueryHandler(category_handler, pattern=re.compile('36')),
    CallbackQueryHandler(category_handler, pattern=re.compile('37')),
    CallbackQueryHandler(category_handler, pattern=re.compile('38')),
    CallbackQueryHandler(category_handler, pattern=re.compile('39')),
    CallbackQueryHandler(category_handler, pattern=re.compile('40')),
    CallbackQueryHandler(category_handler, pattern=re.compile('41')),
    CallbackQueryHandler(category_handler, pattern=re.compile('42')),
    CallbackQueryHandler(category_handler, pattern=re.compile('43')),
    CallbackQueryHandler(category_handler, pattern=re.compile('44')),
    CallbackQueryHandler(category_handler, pattern=re.compile('45')),
    CallbackQueryHandler(category_handler, pattern=re.compile('46')),
    CallbackQueryHandler(category_handler, pattern=re.compile('47')),
    CallbackQueryHandler(category_handler, pattern=re.compile('48')),
    CallbackQueryHandler(category_handler, pattern=re.compile('49')),
    CallbackQueryHandler(category_handler, pattern=re.compile('50')),
    CallbackQueryHandler(category_handler, pattern=re.compile('51')),
    CallbackQueryHandler(category_handler, pattern=re.compile('52')),
    CallbackQueryHandler(category_handler, pattern=re.compile('53')),
    CallbackQueryHandler(category_handler, pattern=re.compile('54')),
    CallbackQueryHandler(category_handler, pattern=re.compile('55')),
    CallbackQueryHandler(category_handler, pattern=re.compile('56')),
    CallbackQueryHandler(category_handler, pattern=re.compile('57')),
    CallbackQueryHandler(category_handler, pattern=re.compile('58')),
    CallbackQueryHandler(category_handler, pattern=re.compile('59')),
    CallbackQueryHandler(category_handler, pattern=re.compile('60')),
    CallbackQueryHandler(category_handler, pattern=re.compile('61')),
    CallbackQueryHandler(category_handler, pattern=re.compile('62')),
    CallbackQueryHandler(category_handler, pattern=re.compile('63')),
    CallbackQueryHandler(category_handler, pattern=re.compile('64')),
    CallbackQueryHandler(category_handler, pattern=re.compile('65')),
    CallbackQueryHandler(category_handler, pattern=re.compile('66')),
    CallbackQueryHandler(category_handler, pattern=re.compile('67')),
    CallbackQueryHandler(category_handler, pattern=re.compile('68')),
    CallbackQueryHandler(category_handler, pattern=re.compile('69')),
    CallbackQueryHandler(category_handler, pattern=re.compile('70')),
    CallbackQueryHandler(category_handler, pattern=re.compile('71')),
    CallbackQueryHandler(category_handler, pattern=re.compile('72')),
    CallbackQueryHandler(category_handler, pattern=re.compile('73')),
    CallbackQueryHandler(category_handler, pattern=re.compile('74')),
    CallbackQueryHandler(category_handler, pattern=re.compile('75')),
    CallbackQueryHandler(category_handler, pattern=re.compile('76')),
    CallbackQueryHandler(category_handler, pattern=re.compile('77')),
    CallbackQueryHandler(category_handler, pattern=re.compile('78')),
    CallbackQueryHandler(category_handler, pattern=re.compile('79')),
    CallbackQueryHandler(category_handler, pattern=re.compile('80')),
    CallbackQueryHandler(category_handler, pattern=re.compile('81')),
    CallbackQueryHandler(category_handler, pattern=re.compile('82')),
    CallbackQueryHandler(category_handler, pattern=re.compile('83')),
    CallbackQueryHandler(category_handler, pattern=re.compile('84')),
    CallbackQueryHandler(category_handler, pattern=re.compile('85')),
    CallbackQueryHandler(category_handler, pattern=re.compile('86')),
    CallbackQueryHandler(category_handler, pattern=re.compile('87')),
    CallbackQueryHandler(category_handler, pattern=re.compile('88')),
    CallbackQueryHandler(category_handler, pattern=re.compile('89')),
    CallbackQueryHandler(category_handler, pattern=re.compile('90')),
    CallbackQueryHandler(category_handler, pattern=re.compile('91')),
    CallbackQueryHandler(category_handler, pattern=re.compile('92')),
    CallbackQueryHandler(category_handler, pattern=re.compile('93')),
    CallbackQueryHandler(category_handler, pattern=re.compile('94')),
    CallbackQueryHandler(category_handler, pattern=re.compile('95')),
    CallbackQueryHandler(category_handler, pattern=re.compile('96')),
    CallbackQueryHandler(category_handler, pattern=re.compile('97')),
    CallbackQueryHandler(category_handler, pattern=re.compile('98')),
    CallbackQueryHandler(category_handler, pattern=re.compile('99')),
    CallbackQueryHandler(category_handler, pattern=re.compile('100')),
    CallbackQueryHandler(category_handler, pattern=re.compile('101')),
    CallbackQueryHandler(category_handler, pattern=re.compile('102')),
    CallbackQueryHandler(category_handler, pattern=re.compile('103')),
    CallbackQueryHandler(category_handler, pattern=re.compile('104')),
    CallbackQueryHandler(category_handler, pattern=re.compile('105')),
    CallbackQueryHandler(category_handler, pattern=re.compile('106')),
    CallbackQueryHandler(category_handler, pattern=re.compile('107')),
    CallbackQueryHandler(category_handler, pattern=re.compile('108')),
    CallbackQueryHandler(category_handler, pattern=re.compile('109')),
    CallbackQueryHandler(category_handler, pattern=re.compile('110')),
    CallbackQueryHandler(category_handler, pattern=re.compile('111')),
    CallbackQueryHandler(category_handler, pattern=re.compile('112')),
    CallbackQueryHandler(category_handler, pattern=re.compile('113')),
    CallbackQueryHandler(category_handler, pattern=re.compile('114')),
]