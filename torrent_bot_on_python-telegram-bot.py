# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
import logging
import re
import json

import config

from pprint import pprint

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
    keyboard = [[InlineKeyboardButton('Выбор категории 1-58', callback_data='Выбор категории 1-58')],
                [InlineKeyboardButton('Выбор категории 59-117', callback_data='Выбор категории 59-117')],
                [InlineKeyboardButton('Поиск по категориям', callback_data='Поиск по категориям')],
                [InlineKeyboardButton('Глобальный поиск', callback_data='Глобальный поиск')],
                [InlineKeyboardButton('Меню', callback_data='m')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, instruction, reply_markup=reply_markup)


def menu(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id
    keyboard = [[InlineKeyboardButton('Инструкция', callback_data='Инструкция')],
                [InlineKeyboardButton('Выбор категории 1-58', callback_data='Выбор категории 1-58')],
                [InlineKeyboardButton('Выбор категории 59-117', callback_data='Выбор категории 59-117')],
                [InlineKeyboardButton('Поиск по категориям', callback_data='Поиск по категориям')],
                [InlineKeyboardButton('Глобальный поиск', callback_data='Глобальный поиск')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, 'Выберите пункт в меню', reply_markup=reply_markup)



def first_categories(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id

    keyboard = [[InlineKeyboardButton('Rutracker Awards (мероприятия и конкурсы)', callback_data='0')],
                 [InlineKeyboardButton('Зарубежное кино', callback_data='1')],
                 [InlineKeyboardButton('Наше кино', callback_data='2')],
                 [InlineKeyboardButton('Арт-хаус и авторское кино', callback_data='3')],
                 [InlineKeyboardButton('Театр', callback_data='4')],
                 [InlineKeyboardButton('DVD Video', callback_data='5')],
                 [InlineKeyboardButton('HD Video', callback_data='6')],
                 [InlineKeyboardButton('3D/Стерео Кино, Видео, TV и Спорт', callback_data='7')],
                 [InlineKeyboardButton('Мультфильмы', callback_data='8')],
                 [InlineKeyboardButton('Мультсериалы', callback_data='9')],
                 [InlineKeyboardButton('Аниме', callback_data='10')],
                 [InlineKeyboardButton('Русские сериалы', callback_data='11')],
                 [InlineKeyboardButton('Зарубежные сериалы', callback_data='12')],
                 [InlineKeyboardButton('Зарубежные сериалы (HD Video)', callback_data='13')],
                 [InlineKeyboardButton('Сериалы Латинской Америки, Турции и Индии', callback_data='14')],
                 [InlineKeyboardButton('Азиатские сериалы', callback_data='15')],
                 [InlineKeyboardButton('Вера и религия', callback_data='16')],
                 [InlineKeyboardButton('Документальные фильмы и телепередачи', callback_data='17')],
                 [InlineKeyboardButton('Документальные (HD Video)', callback_data='18')],
                 [InlineKeyboardButton('Развлекательные телепередачи и шоу, приколы и юмор', callback_data='19')],
                 [InlineKeyboardButton('Зимние Олимпийские игры 2018', callback_data='20')],
                 [InlineKeyboardButton('Спортивные турниры, фильмы и передачи', callback_data='21')],
                 [InlineKeyboardButton('⚽ Футбол', callback_data='22')],
                 [InlineKeyboardButton('🏀 Баскетбол', callback_data='23')],
                 [InlineKeyboardButton('🏒 Хоккей', callback_data='24')],
                 [InlineKeyboardButton('Рестлинг', callback_data='25')],
                 [InlineKeyboardButton('Сканирование, обработка сканов', callback_data='26')],
                 [InlineKeyboardButton('Книги и журналы (общий раздел)', callback_data='27')],
                 [InlineKeyboardButton('Для детей, родителей и учителей', callback_data='28')],
                 [InlineKeyboardButton('Спорт, физическая культура, боевые искусства', callback_data='29')],
                 [InlineKeyboardButton('Гуманитарные науки', callback_data='30')],
                 [InlineKeyboardButton('Исторические науки', callback_data='31')],
                 [InlineKeyboardButton('Точные, естественные и инженерные науки', callback_data='32')],
                 [InlineKeyboardButton('Ноты и Музыкальная литература', callback_data='33')],
                 [InlineKeyboardButton('Военное дело', callback_data='34')],
                 [InlineKeyboardButton('Психология', callback_data='35')],
                 [InlineKeyboardButton('Коллекционирование, увлечения и хобби', callback_data='36')],
                 [InlineKeyboardButton('Художественная литература', callback_data='37')],
                 [InlineKeyboardButton('Компьютерная литература', callback_data='38')],
                 [InlineKeyboardButton('Комиксы, манга, ранобэ', callback_data='39')],
                 [InlineKeyboardButton('Коллекции книг и библиотеки', callback_data='40')],
                 [InlineKeyboardButton('Мультимедийные и интерактивные издания', callback_data='41')],
                 [InlineKeyboardButton('Медицина и здоровье', callback_data='42')],
                 [InlineKeyboardButton('Иностранные языки для взрослых', callback_data='43')],
                 [InlineKeyboardButton('Иностранные языки для детей', callback_data='44')],
                 [InlineKeyboardButton('Художественная литература (ин.языки)', callback_data='45')],
                 [InlineKeyboardButton('Аудиокниги на иностранных языках', callback_data='46')],
                 [InlineKeyboardButton('Видеоуроки и обучающие интерактивные DVD', callback_data='47')],
                 [InlineKeyboardButton('Боевые искусства (Видеоуроки)', callback_data='48')],
                 [InlineKeyboardButton('Компьютерные видеоуроки и обучающие интерактивные DVD', callback_data='49')],
                 [InlineKeyboardButton('Радиоспектакли, история, мемуары', callback_data='50')],
                 [InlineKeyboardButton('Фантастика, фэнтези, мистика, ужасы, фанфики', callback_data='51')],
                 [InlineKeyboardButton('Религии', callback_data='52')],
                 [InlineKeyboardButton('Прочая литература', callback_data='53')],
                 [InlineKeyboardButton('Ремонт и эксплуатация транспортных средств', callback_data='54')],
                 [InlineKeyboardButton('Фильмы и передачи по авто/мото', callback_data='55')],
                 [InlineKeyboardButton('Классическая и современная академическая музыка', callback_data='56')],
                 [InlineKeyboardButton('Фольклор, Народная и Этническая музыка', callback_data='57')],
                 [InlineKeyboardButton('New Age, Relax, Meditative & Flamenco', callback_data='58')],
                 [InlineKeyboardButton('Еще категории', callback_data='e1')],
                 [InlineKeyboardButton('Меню', callback_data='m')],
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, 'Выберите категорию', reply_markup=reply_markup)


def second_categories(update, context):
    query = update.callback_query
    bot = context.bot
    chat_id = query.message.chat.id

    keyboard = [[InlineKeyboardButton('Рэп, Хип-Хоп, R\'n\'B', callback_data='59')],
                 [InlineKeyboardButton('Reggae, Ska, Dub', callback_data='60')],
                 [InlineKeyboardButton('Саундтреки, караоке и мюзиклы', callback_data='61')],
                 [InlineKeyboardButton('Шансон, Авторская и Военная песня', callback_data='62')],
                 [InlineKeyboardButton('Музыка других жанров', callback_data='63')],
                 [InlineKeyboardButton('Отечественная поп-музыка', callback_data='64')],
                 [InlineKeyboardButton('Зарубежная поп-музыка', callback_data='65')],
                 [InlineKeyboardButton('Eurodance, Disco, Hi-NRG', callback_data='66')],
                 [InlineKeyboardButton('Видео, DVD Video, HD Video (поп-музыка)', callback_data='67')],
                 [InlineKeyboardButton('Зарубежный джаз', callback_data='68')],
                 [InlineKeyboardButton('Зарубежный блюз', callback_data='69')],
                 [InlineKeyboardButton('Отечественный джаз и блюз', callback_data='70')],
                 [InlineKeyboardButton('Видео, DVD Video, HD Video (Джаз и блюз)', callback_data='71')],
                 [InlineKeyboardButton('Зарубежный Rock', callback_data='72')],
                 [InlineKeyboardButton('Зарубежный Metal', callback_data='73')],
                 [InlineKeyboardButton('Зарубежные Alternative, Punk, Independent', callback_data='74')],
                 [InlineKeyboardButton('Отечественный Rock, Metal', callback_data='75')],
                 [InlineKeyboardButton('Видео, DVD Video, HD Video (Рок-музыка)', callback_data='76')],
                 [InlineKeyboardButton('Trance, Goa Trance, Psy-Trance, PsyChill, Ambient, Dub', callback_data='77')],
                 [InlineKeyboardButton('House, Techno, Hardcore, Hardstyle, Jumpstyle', callback_data='78')],
                 [InlineKeyboardButton('Drum & Bass, Jungle, Breakbeat, Dubstep, IDM, Electro', callback_data='79')],
                 [InlineKeyboardButton('Chillout, Lounge, Downtempo, Trip-Hop', callback_data='80')],
                 [InlineKeyboardButton('Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Ex..', callback_data='81')],
                 [InlineKeyboardButton('Industrial, Noise, EBM, Dark Electro, Aggrotech, Synthpop, New Wave', callback_data='82')],
                 [InlineKeyboardButton('Label Packs (lossless)', callback_data='83')],
                 [InlineKeyboardButton('Label packs, Scene packs (lossy)', callback_data='84')],
                 [InlineKeyboardButton('Электронная музыка (Видео, DVD Video, HD Video)', callback_data='85')],
                 [InlineKeyboardButton('Hi-Res stereo и многоканальная музыка', callback_data='86')],
                 [InlineKeyboardButton('Оцифровки с аналоговых носителей', callback_data='87')],
                 [InlineKeyboardButton('Неофициальные конверсии цифровых форматов', callback_data='88')],
                 [InlineKeyboardButton('Игры для Windows', callback_data='89')],
                 [InlineKeyboardButton('Прочее для Windows-игр', callback_data='90')],
                 [InlineKeyboardButton('Прочее для Microsoft Flight Simulator, Prepar3D, X-Plane', callback_data='91')],
                 [InlineKeyboardButton('Игры для Macintosh', callback_data='92')],
                 [InlineKeyboardButton('Игры для Linux', callback_data='93')],
                 [InlineKeyboardButton('Игры для консолей', callback_data='94')],
                 [InlineKeyboardButton('Видео для консолей', callback_data='95')],
                 [InlineKeyboardButton('Игры для мобильных устройств', callback_data='96')],
                 [InlineKeyboardButton('Игровое видео', callback_data='97')],
                 [InlineKeyboardButton('Операционные системы от Microsoft', callback_data='98')],
                 [InlineKeyboardButton('Linux, Unix и другие ОС', callback_data='99')],
                 [InlineKeyboardButton('Тестовые диски для настройки аудио/видео аппаратуры', callback_data='100')],
                 [InlineKeyboardButton('Системные программы', callback_data='101')],
                 [InlineKeyboardButton('Системы для бизнеса, офиса, научной и проектной работы', callback_data='102')],
                 [InlineKeyboardButton('Веб-разработка и Программирование', callback_data='103')],
                 [InlineKeyboardButton('Программы для работы с мультимедиа и 3D', callback_data='104')],
                 [InlineKeyboardButton('Материалы для мультимедиа и дизайна', callback_data='105')],
                 [InlineKeyboardButton('ГИС, системы навигации и карты', callback_data='106')],
                 [InlineKeyboardButton('Приложения для мобильных устройств', callback_data='107')],
                 [InlineKeyboardButton('Видео для мобильных устройств', callback_data='108')],
                 [InlineKeyboardButton('Apple Macintosh', callback_data='109')],
                 [InlineKeyboardButton('iOS', callback_data='110')],
                 [InlineKeyboardButton('Видео', callback_data='111')],
                 [InlineKeyboardButton('Видео HD', callback_data='112')],
                 [InlineKeyboardButton('Аудио', callback_data='113')],
                 [InlineKeyboardButton('Разное (раздачи)', callback_data='114')],
                 [InlineKeyboardButton('Тестовый форум', callback_data='115')],
                 [InlineKeyboardButton('Еще категории', callback_data='e2')],
                 [InlineKeyboardButton('Меню', callback_data='m')]
                ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    bot.sendMessage(chat_id, 'Выберите категорию', reply_markup=reply_markup)


def choose_handler(update, context):
    global CATEGORY

    with open(cat_dict, 'r', encoding='utf-8') as dict:
        d = json.load(dict)
        ctgs = [x for i, x in enumerate(d)]

    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    data = update.callback_query.data

    if int(data) in list(range(117)):
        CATEGORY = ctgs[int(data)]
        bot.sendMessage(chat_id, 'Выбрана категория: {}'.format(CATEGORY))
        subcategory(update, context)


def subcategory(update, context):
    global SUBCATEGORY
    bot = context.bot
    chat_id = update.callback_query.message.chat.id

    no_subcategory_text = """Сперва необходимо выбрать категорию. Сделать это можно в меню"""

    subcategory_choose_text = """Перенаправляю вас на выбор подкатегории. Обратите внимание, что в каждой категории \
    свое количество подкатегорий. В некоторых категориях подкатегорий нет."""
    if CATEGORY == None:
        bot.sendMessage(chat_id, no_subcategory_text)
        menu(update, context)

    with open(cat_dict, 'r', encoding='utf-8') as dictionary:
        d = json.load(dictionary)
        ctgs = [x for i, x in enumerate(d)]
        subcategories = d[CATEGORY]
        if len(subcategories) == 0:
            SUBCATEGORY = None
            text = """У категории ({}) нет подкатегорий. Перенаправляю вас на адресный поиск."""
            bot.sendMessage(chat_id, text)
            target_search(update, context)

        keyboard = []

        # for sbct in subcategories:
        #     clean_sbct = sbct.replace("'", "\'")
        #     clbk = '{}-{}'.format(ctgs.index(CATEGORY), subcategories.index(sbct))
        #     keyboard.append([InlineKeyboardButton(clean_sbct, callback_data=clbk)])
        # keyboard.append([InlineKeyboardButton('Назад', callback_data='back')])

        bot.sendMessage(chat_id, 'Выберите подкатегорию: ', reply_markup=keyboard)
        target_search(update, context)


def target_search(update, context):
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    bot.sendMessage(chat_id, 'Здесь будет реализован адресный поиск')


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

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueryies with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'



    # Add conversationhandler to dispatcher it will be used for handling
    # updates
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(instruction, pattern='Инструкция'))
    dp.add_handler(CallbackQueryHandler(first_categories, pattern='Выбор категории 1-58'))
    dp.add_handler(CallbackQueryHandler(second_categories, pattern='Выбор категории 59-117'))
    dp.add_handler(CallbackQueryHandler(menu, pattern='m'))
    dp.add_handler(CallbackQueryHandler(choose_handler, pattern=re.compile('\d')))


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