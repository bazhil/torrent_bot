# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
import logging

import config


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

cat_dict = 'categories_dict.json'

CATEGORY = None
SUBCATEGORY = None
QUERY = None
isRunning = False

# Stages
FIRST, SECOND, THIRD, FOURTH = range(4)

def start(update, context):
    """Send message with menu on `/start`."""
    # Get user that sent /start and log his name
    print(update)
    print(context)
    user = update.message.from_user
    bot = context.bot
    chat_id = update.message.chat.id
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (henc `[[...]]`).
    keyboard = [[InlineKeyboardButton('Инструкция', callback_data='Инструкция')],
                 [InlineKeyboardButton('Выбор категории 1-58', callback_data='Выбор категории 1-58')],
                 [InlineKeyboardButton('Выбор категории 59-117', callback_data='Выбор категории 59-117')],
                 [InlineKeyboardButton('Поиск по категориям', callback_data='Поиск по категориям')],
                 [InlineKeyboardButton('Глобальный поиск', callback_data='Глобальный поиск')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    # update.message.reply_text("Выберите пункт в меню", reply_markup=reply_markup)
    bot.sendMessage(chat_id, "Выберите пункт в меню", reply_markup=reply_markup)



def instruction(update, context):
    """Show instruction"""
    query = update.callback_query
    bot = context.bot
    chat_id = update.message.chat.id
    instruction = """
        Мы все привыкли пользоваться сайтом rutracker.org и скачивать оттуда много полезного и приятного. \
        К сожалению, в последние годы доступ к нему ограничен. \
        Данный бот предоставляет доступ к загрузкам из архивов 2014 года. \
        В качестве результата своей работы он возвращает пользователю magnet-ссылку, с помощью которой можно так же запустить загрузку нужного файла. \
        О том как это сделать лучше читать в интернете.\n
        Все раздачи в рутрекере делятся по категориям, которые в свою очередь делятся на подкатегории, за редким исключением. \
        Это облегчает поиск, т.к. вычеркивает из поиска те категории, в которых явно не содержится нужная информация. \
        Категорий много, поэтому они разбиты на две группы. Ознакомиться с ними можно из меню, или с помощью команд /categories58 \
        и /categories117.\n
        Уже после выбора категории результаты поиска заметно улучшатся. Но чтобы выдача идеально подходила вашим запросам \
        так же рекомендуется выбрать подкатегорию. Сделать это так же можно из меню или по команде /subcategories. Главное, чтобы \
        перед выбором подкатегории была выбрана категория. Иначе не для чего будет выводить подкатегорию.\n
        После выбора категории и подкатегории можно осуществлять поиск по ним. Из меню или по команде /targetsearch. \
        Как и на сайте rutracker.org поиск можно осуществлять адресный или глобальный поиск. Для этого есть раздел в меню и команда /globalsearch.\n
        Желаем найти все!
        """
    keyboard = [[InlineKeyboardButton('Выбор категории 1-58', callback_data='Выбор категории 1-58')],
                [InlineKeyboardButton('Выбор категории 59-117', callback_data='Выбор категории 59-117')],
                [InlineKeyboardButton('Поиск по категориям', callback_data='Поиск по категориям')],
                [InlineKeyboardButton('Глобальный поиск', callback_data='Глобальный поиск')],
                [InlineKeyboardButton('Меню', callback_data='Меню')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, instruction, reply_markup=reply_markup)
    return FIRST


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueryies with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={

        },
        fallbacks=[CommandHandler('start', start)]
    )

    cmd_handler = CommandHandler('instruction', instruction)

    # Add conversationhandler to dispatcher it will be used for handling
    # updates
    dp.add_handler(conv_handler)
    dp.add_handler(cmd_handler)

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