# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, Filters
import logging
import re
import json

from config import get_config

from bot.handlers.category_handlers import category_handlers, subcategory
from keyboard import start_keyboard, instruction_keyboard, menu_keyboard, first_categories_keyboard, \
    second_categories_keyboard
from bot.handlers.subcategory_handlers import subcategory_handlers, target_search

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


config = get_config()


CATEGORY = None
SUBCATEGORY = None
QUERY = None
isRunning = False


def start(update, context):
    """Send message with menu on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    bot = context.bot
    chat_id = update.message.chat.id
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    reply_markup = InlineKeyboardMarkup(start_keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, "Выберите пункт в меню", reply_markup=reply_markup)


def instruction(update, context):
    """Show instruction"""
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id
    instruction = """
        Мы все привыкли пользоваться сайтом rutracker.org и скачивать оттуда много полезного и приятного. \
        К сожалению, в последние годы доступ к нему ограничен. \
        Данный бот предоставляет доступ к загрузкам из архивов 2014 года. \
        В качестве результата своей работы он возвращает пользователю magnet-ссылку, с помощью которой можно так же запустить загрузку нужного файла. \
        О том как это сделать лучше читать в интернете.\n
        Все раздачи в рутрекере делятся по категориям, которые в свою очередь делятся на подкатегории, за редким исключением. \
        Это облегчает поиск, т.к. вычеркивает из поиска те категории, в которых явно не содержится нужная информация. \
        Категорий много, поэтому они разбиты на две группы. 
        Уже после выбора категории результаты поиска заметно улучшатся. Но чтобы выдача идеально подходила вашим запросам \
        так же рекомендуется выбрать подкатегорию. Сделать это так же можно из меню. Главное, чтобы \
        перед выбором подкатегории была выбрана категория. Иначе не для чего будет выводить подкатегорию.\n
        После выбора категории и подкатегории можно осуществлять поиск по ним. \
        Как и на сайте rutracker.org поиск можно осуществлять адресный или глобальный поиск. Для последнего предусмотрен раздел в меню.\n
        Желаем найти все!
        """

    reply_markup = InlineKeyboardMarkup(instruction_keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, instruction, reply_markup=reply_markup)


def menu(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id
    reply_markup = InlineKeyboardMarkup(menu_keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, 'Выберите пункт в меню', reply_markup=reply_markup)


def first_categories(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id
    reply_markup = InlineKeyboardMarkup(first_categories_keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, 'Выберите категорию', reply_markup=reply_markup)


def second_categories(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id
    reply_markup = InlineKeyboardMarkup(second_categories_keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, 'Выберите категорию', reply_markup=reply_markup)


def subcategory_handler(update, context):
    logger.info('subcategory handler works')
    global SUBCATEGORY
    bot = context.bot
    logger.info("bot: ",bot)
    chat_id = update.callback_query.message.chat.id
    logger.info("chat_id: ", chat_id)
    data = update.callback_query.data
    logger.info("data: ", data)

    with open(config.categories_dict, 'r', encoding='utf-8') as dictionary:
        d = json.load(dictionary)
        ctgs = [x for i, x in enumerate(d)]
        subcategories = d[CATEGORY]

    sbct_clbk = {}

    for sbct in subcategories:
        clean_sbct = sbct.replace("'", "\'")
        clbk = '{}-{}'.format(ctgs.index(CATEGORY), subcategories.index(sbct))
        sbct_clbk[clbk] = clean_sbct

    logger.info("Subcategory callback data: ", sbct_clbk)

    if data in sbct_clbk:
        SUBCATEGORY = sbct_clbk[data]
        logger.info("SUBCATEGORY: ", SUBCATEGORY)
        bot.sendMessage(chat_id, 'Выбрана подкатегория: {}'.format(SUBCATEGORY))
    target_search(update, context)

def global_search(update, context):
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    bot.sendMessage(chat_id, 'Здесь будет реализован глобальный поиск')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # Add conversationhandler to dispatcher it will be used for handling
    # updates
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(instruction, pattern='Инструкция'))
    dp.add_handler(CallbackQueryHandler(first_categories, pattern='Выбор категории 1-58'))
    dp.add_handler(CallbackQueryHandler(second_categories, pattern='Выбор категории 59-117'))
    dp.add_handler(CallbackQueryHandler(menu, pattern='m'))

    for handler in category_handlers:
        dp.add_handler(handler)

    for handler in subcategory_handlers:
        dp.add_handler(handler)

    dp.add_handler(CallbackQueryHandler(subcategory, pattern='Выбор подкатегории'))
    dp.add_handler(CallbackQueryHandler(subcategory_handler, pattern=re.compile('.*')))

    dp.add_handler(CallbackQueryHandler(global_search, pattern='Глобальный поиск'))
    dp.add_handler(CallbackQueryHandler(target_search, pattern='Поиск по категориям'))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()