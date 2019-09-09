# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import sqlite3
import json
# import utils
import config
from pprint import pprint


bot = telebot.TeleBot(config.token)


CATEGORY = ''
SUBCATEGORY = ''
QUERY = ''


@bot.message_handler(commands=['start'])
def first(message):
    key = InlineKeyboardMarkup()
    key.row('Инструкция', 'Выбор категории', 'Выбор подкатегории', 'Поиск по категориям', 'Глобальный поиск')
    send = bot.send_message(message.from_user.id, 'Добро пожаловать в телеграм бота', reply_markup=key)
    bot.register_next_step_handler(send, second)


def second(message):
    global CATEGORY
    if message.text == 'Инструкция':
        keyboard = InlineKeyboardMarkup()
        keyboard.row('Выбор категории', 'Глобальный поиск', 'Меню')
        instruction = """
        Чтобы бот нашел именно то, что вам нужно, рекомендуется:
        1) Выбрать категорию, в которой будет осуществляться поиск
        2) Внутри категории выбрать подкатегорию, если такие имеются
        3) Произвести поиск по категориям, перейдя в соответствующий пункт меню и отправить боту поисковой запрос.
        4) Если вы не знаете категории, можете воспользоваться глобальным поиском. Процесс аналогичен описанному в п.4, 
        с той лишь разницей, что бот выведет все варианты, в которых встречается указанный в запросе текст.

        Предлагаю приступить к поиску.
        """
        send = bot.send_message(message.from_user.id, instruction, reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == 'Выбор категории':
        keyboard = InlineKeyboardMarkup()
        keyboard.row('Кино', 'Музыка', 'Мультфильмы', 'Программы', 'Назад')
        send = bot.send_message(message.from_user.id, 'Выберите интересующую вас категорию:', reply_markup=keyboard)
        # попытка получить значение от нажатой кнопки
        bot.register_next_step_handler(send, third)
        CATEGORY = message.text
        print(CATEGORY)
    elif message.text == 'Выбор подкатегории':
        global SUBCATEGORY
        keyboard = InlineKeyboardMarkup()
        if message.text == 'Кино':
            keyboard.row('Фантастика', 'Комедия', 'Боевик', 'Мелодрама', 'Назад')
        elif message.text == 'Музыка':
            keyboard.row('Рок', 'Рэп', 'Джаз', 'Блюз', 'Назад')
        elif message.text == 'Мультфильмы':
            keyboard.row('Отечественные', 'Японские', 'Дисней', 'Дримворкс', 'Назад')
        elif message.text == 'Программы':
            keyboard.row('Adobe', 'Autodesk', 'Microsoft', 'Sabi', 'Назад')
        elif message.text == 'Назад':
            send = bot.send_message(message.from_user.id, 'Возврат в меню')
            bot.register_next_step_handler(send, first)
        send = bot.send_message(message.from_user.id, 'Выберите интересующую вас подкатегорию:', reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
        SUBCATEGORY = message.text
        print(SUBCATEGORY)
    elif message.text == 'Поиск по категориям':
        global QUERY
        send = bot.send_message(message.from_user.id, 'Введите поисковой запрос:')
        QUERY = message.text
        bot.register_next_step_handler(send, third)
    elif message.text == 'Глобальный поиск':
        send = bot.send_message(message.from_user.id, 'Введите поисковой запрос:')
        QUERY = message.text
        print('Поиск глобального запроса {}'.format(QUERY))
        bot.register_next_step_handler(send, third)


def third(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row('Выбор категории', 'Глобальный поиск', 'Меню')
    send = bot.send_message(message.from_user.id,
                            'Результаты поиска в запроса {} по категории {} и подкатегории {}'.format(QUERY, CATEGORY,
                                                                                                      SUBCATEGORY),
                            reply_markup=keyboard)

    bot.register_next_step_handler(send, first)


if __name__ == '__main__':
    bot.polling(none_stop=True)


# dict = 'categories_dict.json'
#
# CATEGORY = ''
# SUBCATEGORY = ''
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     """
#     Function - handler of choosing caterory.
#     :param call:
#     :return:
#     """
#     global CATEGORY
#     if call.data == '1':
#         CATEGORY = 'Rutracker Awards (мероприятия и конкурсы)'
#         bot.answer_callback_query(call.id, 'Выбрана категория {}'.format(CATEGORY))
#     elif call.data == '2':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежное кино')
#         CATEGORY = 'Зарубежное кино'
#     elif call.data == '3':
#         bot.answer_callback_query(call.id, 'Выбрана категория Наше кино')
#         CATEGORY = 'Наше кино'
#     elif call.data == '4':
#         bot.answer_callback_query(call.id, 'Выбрана категория Арт-хаус и авторское кино')
#         CATEGORY = 'Арт-хаус и авторское кино'
#     elif call.data == '5':
#         bot.answer_callback_query(call.id, 'Выбрана категория Театр')
#         CATEGORY = 'Театр'
#     elif call.data == '6':
#         bot.answer_callback_query(call.id, 'Выбрана категория DVD Video')
#         CATEGORY = 'DVD Video'
#     elif call.data == '7':
#         bot.answer_callback_query(call.id, 'Выбрана категория HD Video')
#         CATEGORY = 'HD Video'
#     elif call.data == '8':
#         bot.answer_callback_query(call.id, 'Выбрана категория 3D/Стерео Кино, Видео, TV и Спорт')
#         CATEGORY = '3D/Стерео Кино, Видео, TV и Спорт'
#     elif call.data == '9':
#         bot.answer_callback_query(call.id, 'Выбрана категория Мультфильмы')
#         CATEGORY = 'Мультфильмы'
#     elif call.data == '10':
#         bot.answer_callback_query(call.id, 'Выбрана категория Мультсериалы')
#         CATEGORY = 'Мультсериалы'
#     elif call.data == '11':
#         bot.answer_callback_query(call.id, 'Выбрана категория Аниме')
#         CATEGORY = 'Аниме'
#     elif call.data == '12':
#         bot.answer_callback_query(call.id, 'Выбрана категория Русские сериалы')
#         CATEGORY = 'Русские сериалы'
#     elif call.data == '13':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежные сериалы')
#         CATEGORY = 'Зарубежные сериалы'
#     elif call.data == '14':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежные сериалы (HD Video)')
#         CATEGORY = 'Зарубежные сериалы (HD Video)'
#     elif call.data == '15':
#         bot.answer_callback_query(call.id, 'Выбрана категория Сериалы Латинской Америки, Турции и Индии')
#         CATEGORY = 'Сериалы Латинской Америки, Турции и Индии'
#     elif call.data == '16':
#         bot.answer_callback_query(call.id, 'Выбрана категория Азиатские сериалы')
#         CATEGORY = 'Азиатские сериалы'
#     elif call.data == '17':
#         bot.answer_callback_query(call.id, 'Выбрана категория Вера и религия')
#         CATEGORY = 'Вера и религия'
#     elif call.data == '18':
#         bot.answer_callback_query(call.id, 'Выбрана категория Документальные фильмы и телепередачи')
#         CATEGORY = 'Документальные фильмы и телепередачи'
#     elif call.data == '19':
#         bot.answer_callback_query(call.id, 'Выбрана категория Документальные (HD Video)')
#         CATEGORY = 'Документальные (HD Video)'
#     elif call.data == '20':
#         bot.answer_callback_query(call.id, 'Выбрана категория Развлекательные телепередачи и шоу, приколы и юмор')
#         CATEGORY = 'Развлекательные телепередачи и шоу, приколы и юмор'
#     elif call.data == '21':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зимние Олимпийские игры 2018')
#         CATEGORY = 'Зимние Олимпийские игры 2018'
#     elif call.data == '22':
#         bot.answer_callback_query(call.id, 'Выбрана категория Спортивные турниры, фильмы и передачи')
#         CATEGORY = 'Спортивные турниры, фильмы и передачи'
#     elif call.data == '23':
#         bot.answer_callback_query(call.id, 'Выбрана категория ⚽ Футбол')
#         CATEGORY = '⚽ Футбол'
#     elif call.data == '24':
#         bot.answer_callback_query(call.id, 'Выбрана категория 🏀 Баскетбол')
#         CATEGORY = '🏀 Баскетбол'
#     elif call.data == '25':
#         bot.answer_callback_query(call.id, 'Выбрана категория 🏒 Хоккей')
#         CATEGORY = '🏒 Хоккей'
#     elif call.data == '26':
#         bot.answer_callback_query(call.id, 'Выбрана категория Рестлинг')
#         CATEGORY = 'Рестлинг'
#     elif call.data == '27':
#         bot.answer_callback_query(call.id, 'Выбрана категория Сканирование, обработка сканов')
#         CATEGORY = 'Сканирование, обработка сканов'
#     elif call.data == '28':
#         bot.answer_callback_query(call.id, 'Выбрана категория Книги и журналы (общий раздел)')
#         CATEGORY = 'Книги и журналы (общий раздел)'
#     elif call.data == '29':
#         bot.answer_callback_query(call.id, 'Выбрана категория Для детей, родителей и учителей')
#         CATEGORY = 'Для детей, родителей и учителей'
#     elif call.data == '30':
#         bot.answer_callback_query(call.id, 'Выбрана категория Спорт, физическая культура, боевые искусства')
#         CATEGORY = 'Спорт, физическая культура, боевые искусства'
#     elif call.data == '31':
#         bot.answer_callback_query(call.id, 'Выбрана категория Гуманитарные науки')
#         CATEGORY = 'Гуманитарные науки'
#     elif call.data == '32':
#         bot.answer_callback_query(call.id, 'Выбрана категория Исторические науки')
#         CATEGORY = 'Исторические науки'
#     elif call.data == '33':
#         bot.answer_callback_query(call.id, 'Выбрана категория Точные, естественные и инженерные науки')
#         CATEGORY = 'Точные, естественные и инженерные науки'
#     elif call.data == '34':
#         bot.answer_callback_query(call.id, 'Выбрана категория Ноты и Музыкальная литература')
#         CATEGORY = 'Ноты и Музыкальная литература'
#     elif call.data == '35':
#         bot.answer_callback_query(call.id, 'Выбрана категория Военное дело')
#         CATEGORY = 'Военное дело'
#     elif call.data == '36':
#         bot.answer_callback_query(call.id, 'Выбрана категория Психология')
#         CATEGORY = 'Психология'
#     elif call.data == '37':
#         bot.answer_callback_query(call.id, 'Выбрана категория Коллекционирование, увлечения и хобби')
#         CATEGORY = 'Коллекционирование, увлечения и хобби'
#     elif call.data == '38':
#         bot.answer_callback_query(call.id, 'Выбрана категория Художественная литература')
#         CATEGORY = 'Художественная литература'
#     elif call.data == '39':
#         bot.answer_callback_query(call.id, 'Выбрана категория Компьютерная литература')
#         CATEGORY = 'Компьютерная литература'
#     elif call.data == '40':
#         bot.answer_callback_query(call.id, 'Выбрана категория Комиксы, манга, ранобэ')
#         CATEGORY = 'Комиксы, манга, ранобэ'
#     elif call.data == '41':
#         bot.answer_callback_query(call.id, 'Выбрана категория Коллекции книг и библиотеки')
#         CATEGORY = 'Коллекции книг и библиотеки'
#     elif call.data == '42':
#         bot.answer_callback_query(call.id, 'Выбрана категория Мультимедийные и интерактивные издания')
#         CATEGORY = 'Мультимедийные и интерактивные издания'
#     elif call.data == '43':
#         bot.answer_callback_query(call.id, 'Выбрана категория Медицина и здоровье')
#         CATEGORY = 'Медицина и здоровье'
#     elif call.data == '44':
#         bot.answer_callback_query(call.id, 'Выбрана категория Иностранные языки для взрослых')
#         CATEGORY = 'Иностранные языки для взрослых'
#     elif call.data == '45':
#         bot.answer_callback_query(call.id, 'Выбрана категория Иностранные языки для детей')
#         CATEGORY = 'Иностранные языки для детей'
#     elif call.data == '46':
#         bot.answer_callback_query(call.id, 'Выбрана категория Художественная литература (ин.языки)')
#         CATEGORY = 'Художественная литература (ин.языки)'
#     elif call.data == '47':
#         bot.answer_callback_query(call.id, 'Выбрана категория Аудиокниги на иностранных языках')
#         CATEGORY = 'Аудиокниги на иностранных языках'
#     elif call.data == '48':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видеоуроки и обучающие интерактивные DVD')
#         CATEGORY = 'Видеоуроки и обучающие интерактивные DVD'
#     elif call.data == '49':
#         bot.answer_callback_query(call.id, 'Выбрана категория Боевые искусства (Видеоуроки)')
#         CATEGORY = 'Боевые искусства (Видеоуроки)'
#     elif call.data == '50':
#         bot.answer_callback_query(call.id, 'Выбрана категория Компьютерные видеоуроки и обучающие интерактивные DVD')
#         CATEGORY = 'Компьютерные видеоуроки и обучающие интерактивные DVD'
#     elif call.data == '51':
#         bot.answer_callback_query(call.id, 'Выбрана категория Радиоспектакли, история, мемуары')
#         CATEGORY = 'Радиоспектакли, история, мемуары'
#     elif call.data == '52':
#         bot.answer_callback_query(call.id, 'Выбрана категория Фантастика, фэнтези, мистика, ужасы, фанфики')
#         CATEGORY = 'Фантастика, фэнтези, мистика, ужасы, фанфики'
#     elif call.data == '53':
#         bot.answer_callback_query(call.id, 'Выбрана категория Религии')
#         CATEGORY = 'Религии'
#     elif call.data == '54':
#         bot.answer_callback_query(call.id, 'Выбрана категория Прочая литература')
#         CATEGORY = 'Прочая литература'
#     elif call.data == '55':
#         bot.answer_callback_query(call.id, 'Выбрана категория Ремонт и эксплуатация транспортных средств')
#         CATEGORY = 'Ремонт и эксплуатация транспортных средств'
#     elif call.data == '56':
#         bot.answer_callback_query(call.id, 'Выбрана категория Фильмы и передачи по авто/мото')
#         CATEGORY = 'Фильмы и передачи по авто/мото'
#     elif call.data == '57':
#         bot.answer_callback_query(call.id, 'Выбрана категория Классическая и современная академическая музыка')
#         CATEGORY = 'Классическая и современная академическая музыка'
#     elif call.data == '58':
#         bot.answer_callback_query(call.id, 'Выбрана категория Фольклор, Народная и Этническая музыка')
#         CATEGORY = 'Фольклор, Народная и Этническая музыка'
#     elif call.data == '59':
#         bot.answer_callback_query(call.id, 'Выбрана категория New Age, Relax, Meditative & Flamenco')
#         CATEGORY = 'New Age, Relax, Meditative & Flamenco'
#     elif call.data == '60':
#         bot.answer_callback_query(call.id, 'Выбрана категория Рэп, Хип-Хоп, R\'n\'B')
#         CATEGORY = 'Рэп, Хип-Хоп, R\'n\'B'
#     elif call.data == '61':
#         bot.answer_callback_query(call.id, 'Выбрана категория Reggae, Ska, Dub')
#         CATEGORY = 'Reggae, Ska, Dub'
#     elif call.data == '62':
#         bot.answer_callback_query(call.id, 'Выбрана категория Саундтреки, караоке и мюзиклы')
#         CATEGORY = 'Саундтреки, караоке и мюзиклы'
#     elif call.data == '63':
#         bot.answer_callback_query(call.id, 'Выбрана категория Шансон, Авторская и Военная песня')
#         CATEGORY = 'Шансон, Авторская и Военная песня'
#     elif call.data == '64':
#         bot.answer_callback_query(call.id, 'Выбрана категория Музыка других жанров')
#         CATEGORY = 'Музыка других жанров'
#     elif call.data == '65':
#         bot.answer_callback_query(call.id, 'Выбрана категория Отечественная поп-музыка')
#         CATEGORY = 'Отечественная поп-музыка'
#     elif call.data == '66':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежная поп-музыка')
#         CATEGORY = 'Зарубежная поп-музыка'
#     elif call.data == '67':
#         bot.answer_callback_query(call.id, 'Выбрана категория Eurodance, Disco, Hi-NRG')
#         CATEGORY = 'Eurodance, Disco, Hi-NRG'
#     elif call.data == '68':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео, DVD Video, HD Video (поп-музыка)')
#         CATEGORY = 'Видео, DVD Video, HD Video (поп-музыка)'
#     elif call.data == '69':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежный джаз')
#         CATEGORY = 'Зарубежный джаз'
#     elif call.data == '70':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежный блюз')
#         CATEGORY = 'Зарубежный блюз'
#     elif call.data == '71':
#         bot.answer_callback_query(call.id, 'Выбрана категория Отечественный джаз и блюз')
#         CATEGORY = 'Отечественный джаз и блюз'
#     elif call.data == '72':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео, DVD Video, HD Video (Джаз и блюз)')
#         CATEGORY = 'Видео, DVD Video, HD Video (Джаз и блюз)'
#     elif call.data == '73':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежный Rock')
#         CATEGORY = 'Зарубежный Rock'
#     elif call.data == '74':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежный Metal')
#         CATEGORY = 'Зарубежный Metal'
#     elif call.data == '75':
#         bot.answer_callback_query(call.id, 'Выбрана категория Зарубежные Alternative, Punk, Independent')
#         CATEGORY = 'Зарубежные Alternative, Punk, Independent'
#     elif call.data == '76':
#         bot.answer_callback_query(call.id, 'Выбрана категория Отечественный Rock, Metal')
#         CATEGORY = 'Отечественный Rock, Metal'
#     elif call.data == '77':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео, DVD Video, HD Video (Рок-музыка)')
#         CATEGORY = 'Видео, DVD Video, HD Video (Рок-музыка)'
#     elif call.data == '78':
#         bot.answer_callback_query(call.id, 'Выбрана категория Trance, Goa Trance, Psy-Trance, PsyChill, Ambient, Dub')
#         CATEGORY = 'Trance, Goa Trance, Psy-Trance, PsyChill, Ambient, Dub'
#     elif call.data == '79':
#         bot.answer_callback_query(call.id, 'Выбрана категория House, Techno, Hardcore, Hardstyle, Jumpstyle')
#         CATEGORY = 'House, Techno, Hardcore, Hardstyle, Jumpstyle'
#     elif call.data == '80':
#         bot.answer_callback_query(call.id, 'Выбрана категория Drum & Bass, Jungle, Breakbeat, Dubstep, IDM, Electro')
#         CATEGORY = 'Drum & Bass, Jungle, Breakbeat, Dubstep, IDM, Electro'
#     elif call.data == '81':
#         bot.answer_callback_query(call.id, 'Выбрана категория Chillout, Lounge, Downtempo, Trip-Hop')
#         CATEGORY = 'Chillout, Lounge, Downtempo, Trip-Hop'
#     elif call.data == '82':
#         bot.answer_callback_query(call.id,
#                                   'Выбрана категория Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Ex..')
#         CATEGORY = 'Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Ex..'
#     elif call.data == '83':
#         bot.answer_callback_query(call.id,
#                                   'Выбрана категория Industrial, Noise, EBM, Dark Electro, Aggrotech, Synthpop, New Wave')
#         CATEGORY = 'Industrial, Noise, EBM, Dark Electro, Aggrotech, Synthpop, New Wave'
#     elif call.data == '84':
#         bot.answer_callback_query(call.id, 'Выбрана категория Label Packs (lossless)')
#         CATEGORY = 'Label Packs (lossless)'
#     elif call.data == '85':
#         bot.answer_callback_query(call.id, 'Выбрана категория Label packs, Scene packs (lossy)')
#         CATEGORY = 'Label packs, Scene packs (lossy)'
#     elif call.data == '86':
#         bot.answer_callback_query(call.id, 'Выбрана категория Электронная музыка (Видео, DVD Video, HD Video)')
#         CATEGORY = 'Электронная музыка (Видео, DVD Video, HD Video)'
#     elif call.data == '87':
#         bot.answer_callback_query(call.id, 'Выбрана категория Hi-Res stereo и многоканальная музыка')
#         CATEGORY = 'Hi-Res stereo и многоканальная музыка'
#     elif call.data == '88':
#         bot.answer_callback_query(call.id, 'Выбрана категория Оцифровки с аналоговых носителей')
#         CATEGORY = 'Оцифровки с аналоговых носителей'
#     elif call.data == '89':
#         bot.answer_callback_query(call.id, 'Выбрана категория Неофициальные конверсии цифровых форматов')
#         CATEGORY = 'Неофициальные конверсии цифровых форматов'
#     elif call.data == '90':
#         bot.answer_callback_query(call.id, 'Выбрана категория Игры для Windows')
#         CATEGORY = 'Игры для Windows'
#     elif call.data == '91':
#         bot.answer_callback_query(call.id, 'Выбрана категория Прочее для Windows-игр')
#         CATEGORY = 'Прочее для Windows-игр'
#     elif call.data == '92':
#         bot.answer_callback_query(call.id, 'Выбрана категория Прочее для Microsoft Flight Simulator, Prepar3D, X-Plane')
#         CATEGORY = 'Прочее для Microsoft Flight Simulator, Prepar3D, X-Plane'
#     elif call.data == '93':
#         bot.answer_callback_query(call.id, 'Выбрана категория Игры для Macintosh')
#         CATEGORY = 'Игры для Macintosh'
#     elif call.data == '94':
#         bot.answer_callback_query(call.id, 'Выбрана категория Игры для Linux')
#         CATEGORY = 'Игры для Linux'
#     elif call.data == '95':
#         bot.answer_callback_query(call.id, 'Выбрана категория Игры для консолей')
#         CATEGORY = 'Игры для консолей'
#     elif call.data == '96':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео для консолей')
#         CATEGORY = 'Видео для консолей'
#     elif call.data == '97':
#         bot.answer_callback_query(call.id, 'Выбрана категория Игры для мобильных устройств')
#         CATEGORY = 'Игры для мобильных устройств'
#     elif call.data == '98':
#         bot.answer_callback_query(call.id, 'Выбрана категория Игровое видео')
#         CATEGORY = 'Игровое видео'
#     elif call.data == '99':
#         bot.answer_callback_query(call.id, 'Выбрана категория Операционные системы от Microsoft')
#         CATEGORY = 'Операционные системы от Microsoft'
#     elif call.data == '100':
#         bot.answer_callback_query(call.id, 'Выбрана категория Linux, Unix и другие ОС')
#         CATEGORY = 'Linux, Unix и другие ОС'
#     elif call.data == '101':
#         bot.answer_callback_query(call.id, 'Выбрана категория Тестовые диски для настройки аудио/видео аппаратуры')
#         CATEGORY = 'Тестовые диски для настройки аудио/видео аппаратуры'
#     elif call.data == '102':
#         bot.answer_callback_query(call.id, 'Выбрана категория Системные программы')
#         CATEGORY = 'Системные программы'
#     elif call.data == '103':
#         bot.answer_callback_query(call.id, 'Выбрана категория Системы для бизнеса, офиса, научной и проектной работы')
#         CATEGORY = 'Системы для бизнеса, офиса, научной и проектной работы'
#     elif call.data == '104':
#         bot.answer_callback_query(call.id, 'Выбрана категория Веб-разработка и Программирование')
#         CATEGORY = 'Веб-разработка и Программирование'
#     elif call.data == '105':
#         bot.answer_callback_query(call.id, 'Выбрана категория Программы для работы с мультимедиа и 3D')
#         CATEGORY = 'Программы для работы с мультимедиа и 3D'
#     elif call.data == '106':
#         bot.answer_callback_query(call.id, 'Выбрана категория Материалы для мультимедиа и дизайна')
#         CATEGORY = 'Материалы для мультимедиа и дизайна'
#     elif call.data == '107':
#         bot.answer_callback_query(call.id, 'Выбрана категория ГИС, системы навигации и карты')
#         CATEGORY = 'ГИС, системы навигации и карты'
#     elif call.data == '108':
#         bot.answer_callback_query(call.id, 'Выбрана категория Приложения для мобильных устройств')
#         CATEGORY = 'Приложения для мобильных устройств'
#     elif call.data == '109':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео для мобильных устройств')
#         CATEGORY = 'Видео для мобильных устройств'
#     elif call.data == '110':
#         bot.answer_callback_query(call.id, 'Выбрана категория Apple Macintosh')
#         CATEGORY = 'Apple Macintosh'
#     elif call.data == '111':
#         bot.answer_callback_query(call.id, 'Выбрана категория iOS')
#         CATEGORY = 'iOS'
#     elif call.data == '112':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео')
#         CATEGORY = 'Видео'
#     elif call.data == '113':
#         bot.answer_callback_query(call.id, 'Выбрана категория Видео HD')
#         CATEGORY = 'Видео HD'
#     elif call.data == '114':
#         bot.answer_callback_query(call.id, 'Выбрана категория Аудио')
#         CATEGORY = 'Аудио'
#     elif call.data == '115':
#         bot.answer_callback_query(call.id, 'Выбрана категория Разное (раздачи)')
#         CATEGORY = 'Разное (раздачи)'
#     elif call.data == '116':
#         bot.answer_callback_query(call.id, 'Выбрана категория Тестовый форум')
#         CATEGORY = 'Тестовый форум'
#     elif call.data == '117':
#         bot.answer_callback_query(call.id, 'Выбрана категория Отчеты о встречах')
#         CATEGORY = 'Отчеты о встречах'
#
#
# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#     bot.send_message(message.chat.id, "Выберете категорию в которой следует производить поиск",
#                      reply_markup=gen_categories_keyboard())
#
# def gen_categories_keyboard():
#     """
#     Function, which generate menu with categories
#     :return: keyboard
#     """
#     keyboard = InlineKeyboardMarkup()
#
#     keyboard.row_width = 1
#
#     j = 0
#     with open(dict, 'r', encoding='utf-8') as dictionary:
#         d = json.load(dictionary)
#     for i in d:
#         j += 1
#         keyboard.add(InlineKeyboardButton(text=i, callback_data=str(j)))
#     return keyboard
#
#
# def gen_subcategory_keyboard():
#     """
#     Function, which generate menu with subcategories
#     :param
#     :return: keyboard:
#     """
#     keyboard = InlineKeyboardMarkup()
#
#     keyboard.row_width = 1
#
#     j = 200
#     with open(dict, 'r', encoding='utf-8') as dictionary:
#         d = json.load(dictionary)
#     for i in d[CATEGORY]:
#         if len(d[CATEGORY]) == 0:
#             break
#         j += 1
#         keyboard.add(InlineKeyboardButton(text=i, callback_data=str(j)))
#     return keyboard
#
# if __name__ == '__main__':
#     bot.polling(none_stop=True)