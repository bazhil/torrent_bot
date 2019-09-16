# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import sqlite3
import json
# import utils
import config
from pprint import pprint


bot = telebot.TeleBot(config.token)


cat_dict = 'categories_dict.json'

CATEGORY = None
SUBCATEGORY = None
QUERY = None
isRunning = False


@bot.callback_query_handler(func=lambda call: True)
def category_query(call):
    """
    Function - handler of choosing caterory.
    :param call:
    :return:
    """
    global CATEGORY
    category_choose_text = """Перенаправляю вас на выбор категории. Обратите внимание, что всего 117 категорий, \
    но за 1 раз вам будет выведено только 58. На остальные категории вы сможете переключиться внутри меню выбора. \
    Если оно не выводится, вы можете вызвать его с помощью команд /categories58 и /categories117"""
    if call.data == 'Выбор категории 1-58':
        send = bot.send_message(call.from_user.id, category_choose_text)
        bot.register_next_step_handler(send, first_categories(call))
    elif call.data == 'Выбор категории 59-117':
        send = bot.send_message(call.from_user.id, category_choose_text)
        bot.register_next_step_handler(send, second_categories(call))
    elif call.data == 'm':
        send = bot.send_message(call.from_user.id, 'Возврат в стартовое меню')
        bot.register_next_step_handler(send, start(call))
    elif call.data == '0':
        CATEGORY = 'Rutracker Awards (мероприятия и конкурсы)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '1':
        CATEGORY = 'Зарубежное кино'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '2':
        CATEGORY = 'Наше кино'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '3':
        CATEGORY = 'Арт-хаус и авторское кино'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '4':
        CATEGORY = 'Театр'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '5':
        CATEGORY = 'DVD Video'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '6':
        CATEGORY = 'HD Video'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '7':
        CATEGORY = '3D/Стерео Кино, Видео, TV и Спорт'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '8':
        CATEGORY = 'Мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '9':
        CATEGORY = 'Мультсериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '10':
        CATEGORY = 'Аниме'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '11':
        CATEGORY = 'Русские сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '12':
        CATEGORY = 'Зарубежные сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '13':
        CATEGORY = 'Зарубежные сериалы (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '14':
        CATEGORY = 'Сериалы Латинской Америки, Турции и Индии'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '15':
        CATEGORY = 'Азиатские сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '16':
        CATEGORY = 'Вера и религия'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '17':
        CATEGORY = 'Документальные фильмы и телепередачи'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '18':
        CATEGORY = 'Документальные (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '19':
        CATEGORY = 'Развлекательные телепередачи и шоу, приколы и юмор'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '20':
        CATEGORY = 'Зимние Олимпийские игры 2018'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '21':
        CATEGORY = 'Спортивные турниры, фильмы и передачи'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '22':
        CATEGORY = '⚽ Футбол'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '23':
        CATEGORY = '🏀 Баскетбол'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '244':
        CATEGORY = '🏒 Хоккей'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '25':
        CATEGORY = 'Рестлинг'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '26':
        CATEGORY = 'Сканирование, обработка сканов'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '27':
        CATEGORY = 'Книги и журналы (общий раздел)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '28':
        CATEGORY = 'Для детей, родителей и учителей'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '29':
        CATEGORY = 'Спорт, физическая культура, боевые искусства'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '30':
        CATEGORY = 'Гуманитарные науки'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '31':
        CATEGORY = 'Исторические науки'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '32':
        CATEGORY = 'Точные, естественные и инженерные науки'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '33':
        CATEGORY = 'Ноты и Музыкальная литература'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '34':
        CATEGORY = 'Военное дело'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '35':
        CATEGORY = 'Психология'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '36':
        CATEGORY = 'Коллекционирование, увлечения и хобби'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '37':
        CATEGORY = 'Художественная литература'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '38':
        CATEGORY = 'Компьютерная литература'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '39':
        CATEGORY = 'Комиксы, манга, ранобэ'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '40':
        CATEGORY = 'Коллекции книг и библиотеки'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '41':
        CATEGORY = 'Мультимедийные и интерактивные издания'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '42':
        CATEGORY = 'Медицина и здоровье'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '43':
        CATEGORY = 'Иностранные языки для взрослых'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '44':
        CATEGORY = 'Иностранные языки для детей'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '45':
        CATEGORY = 'Художественная литература (ин.языки)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '46':
        CATEGORY = 'Аудиокниги на иностранных языках'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '47':
        CATEGORY = 'Видеоуроки и обучающие интерактивные DVD'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '48':
        CATEGORY = 'Боевые искусства (Видеоуроки)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '49':
        CATEGORY = 'Компьютерные видеоуроки и обучающие интерактивные DVD'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '50':
        CATEGORY = 'Радиоспектакли, история, мемуары'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '51':
        CATEGORY = 'Фантастика, фэнтези, мистика, ужасы, фанфики'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '52':
        CATEGORY = 'Религии'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '53':
        CATEGORY = 'Прочая литература'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '54':
        CATEGORY = 'Ремонт и эксплуатация транспортных средств'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '55':
        CATEGORY = 'Фильмы и передачи по авто/мото'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '56':
        CATEGORY = 'Классическая и современная академическая музыка'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '57':
        CATEGORY = 'Фольклор, Народная и Этническая музыка'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '58':
        CATEGORY = 'New Age, Relax, Meditative & Flamenco'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '59':
        CATEGORY = 'Рэп, Хип-Хоп, R\'n\'B'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '60':
        CATEGORY = 'Reggae, Ska, Dub'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '61':
        CATEGORY = 'Саундтреки, караоке и мюзиклы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '62':
        CATEGORY = 'Шансон, Авторская и Военная песня'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '63':
        CATEGORY = 'Музыка других жанров'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '64':
        CATEGORY = 'Отечественная поп-музыка'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '65':
        CATEGORY = 'Зарубежная поп-музыка'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '66':
        CATEGORY = 'Eurodance, Disco, Hi-NRG'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '67':
        CATEGORY = 'Видео, DVD Video, HD Video (поп-музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '68':
        CATEGORY = 'Зарубежный джаз'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '69':
        CATEGORY = 'Зарубежный блюз'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '70':
        CATEGORY = 'Отечественный джаз и блюз'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '71':
        CATEGORY = 'Видео, DVD Video, HD Video (Джаз и блюз)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '72':
        CATEGORY = 'Зарубежный Rock'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '73':
        CATEGORY = 'Зарубежный Metal'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '74':
        CATEGORY = 'Зарубежные Alternative, Punk, Independent'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '75':
        CATEGORY = 'Отечественный Rock, Metal'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '76':
        CATEGORY = 'Видео, DVD Video, HD Video (Рок-музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '77':
        CATEGORY = 'Trance, Goa Trance, Psy-Trance, PsyChill, Ambient, Dub'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '78':
        CATEGORY = 'House, Techno, Hardcore, Hardstyle, Jumpstyle'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '79':
        CATEGORY = 'Drum & Bass, Jungle, Breakbeat, Dubstep, IDM, Electro'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '80':
        CATEGORY = 'Chillout, Lounge, Downtempo, Trip-Hop'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '81':
        CATEGORY = 'Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Ex..'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '82':
        CATEGORY = 'Industrial, Noise, EBM, Dark Electro, Aggrotech, Synthpop, New Wave'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '83':
        CATEGORY = 'Label Packs (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '84':
        CATEGORY = 'Label packs, Scene packs (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '85':
        CATEGORY = 'Электронная музыка (Видео, DVD Video, HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '86':
        CATEGORY = 'Hi-Res stereo и многоканальная музыка'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '87':
        CATEGORY = 'Оцифровки с аналоговых носителей'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '88':
        CATEGORY = 'Неофициальные конверсии цифровых форматов'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '89':
        CATEGORY = 'Игры для Windows'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '90':
        CATEGORY = 'Прочее для Windows-игр'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '91':
        CATEGORY = 'Прочее для Microsoft Flight Simulator, Prepar3D, X-Plane'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '92':
        CATEGORY = 'Игры для Macintosh'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '93':
        CATEGORY = 'Игры для Linux'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '94':
        CATEGORY = 'Игры для консолей'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '95':
        CATEGORY = 'Видео для консолей'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '96':
        CATEGORY = 'Игры для мобильных устройств'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '97':
        CATEGORY = 'Игровое видео'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '98':
        CATEGORY = 'Операционные системы от Microsoft'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '99':
        CATEGORY = 'Linux, Unix и другие ОС'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '100':
        CATEGORY = 'Тестовые диски для настройки аудио/видео аппаратуры'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '101':
        CATEGORY = 'Системные программы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '102':
        CATEGORY = 'Системы для бизнеса, офиса, научной и проектной работы'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '103':
        CATEGORY = 'Веб-разработка и Программирование'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '104':
        CATEGORY = 'Программы для работы с мультимедиа и 3D'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '105':
        CATEGORY = 'Материалы для мультимедиа и дизайна'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '106':
        CATEGORY = 'ГИС, системы навигации и карты'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '107':
        CATEGORY = 'Приложения для мобильных устройств'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '108':
        CATEGORY = 'Видео для мобильных устройств'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '109':
        CATEGORY = 'Apple Macintosh'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '110':
        CATEGORY = 'iOS'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '111':
        CATEGORY = 'Видео'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '112':
        CATEGORY = 'Видео HD'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '113':
        CATEGORY = 'Аудио'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '114':
        CATEGORY = 'Разное (раздачи)'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '115':
        CATEGORY = 'Тестовый форум'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    elif call.data == '116':
        CATEGORY = 'Отчеты о встречах'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(CATEGORY))
        bot.register_next_step_handler(send, subcategories(call))
    # make handlers for subcategories
    elif call.data == '52-0':
        SUBCATEGORY = '[Аудио] Православие'
        send = bot.send_message(call.from_user.id, 'Выбрана категория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))



@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(InlineKeyboardButton('Инструкция', callback_data='Инструкция'),
                 InlineKeyboardButton('Выбор категории 1-58', callback_data='Выбор категории 1-58'),
                 InlineKeyboardButton('Выбор категории 59-117', callback_data='Выбор категории 59-117'),
                 InlineKeyboardButton('Поиск по категориям', callback_data='Поиск по категориям'),
                 InlineKeyboardButton('Глобальный поиск', callback_data='Глобальный поиск')
                 )
    introduction = """
    Добро пожаловать!\n\
    Данный бот осуществляет поиск magnet-ссылки на раздачу с сайта rutracker.org.\n\
    Чтобы понять, как работать с ботом рекомендуется прочитать инструкцию. Сделать это можно с помощью выбора \
    соответствующего пункта в меню, либо с помощью команды /instruction.
    """
    bot.send_message(message.from_user.id, introduction, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['instruction'])
def instruction(message):
    instruction = """
    Мы все привыкли пользоваться сайтом rutracker.org и скачивать оттуда много полезного и приятного. \
    К сожалению, в последние годы доступ к нему хоть и не запрещен, но ограничен. \
    Данный бот предоставляет доступ к некоторым загрузкам, основываясь на архивах 2014 года. \
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
    keyboard = InlineKeyboardMarkup()
    keyboard.row_width = 1
    keyboard.add(InlineKeyboardButton('Выбор категории 1-58', callback_data='Выбор категории 1-58'),
                 InlineKeyboardButton('Выбор категории 59-117', callback_data='Выбор категории 59-117'),
                 InlineKeyboardButton('Поиск по категориям', callback_data='Поиск по категориям'),
                 InlineKeyboardButton('Глобальный поиск', callback_data='Глобальный поиск'),
                 InlineKeyboardButton('Меню', callback_data='Меню'),
                 )

    bot.send_message(message.from_user.id, instruction, reply_markup=keyboard)



@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['categories58'])
def first_categories(message):
    keyboard = InlineKeyboardMarkup()

    keyboard.row_width = 1

    keyboard.add(InlineKeyboardButton('Rutracker Awards (мероприятия и конкурсы)', callback_data='0'),
                 InlineKeyboardButton('Зарубежное кино', callback_data='1'),
                 InlineKeyboardButton('Наше кино', callback_data='2'),
                 InlineKeyboardButton('Арт-хаус и авторское кино', callback_data='3'),
                 InlineKeyboardButton('Театр', callback_data='4'),
                 InlineKeyboardButton('DVD Video', callback_data='5'),
                 InlineKeyboardButton('HD Video', callback_data='6'),
                 InlineKeyboardButton('3D/Стерео Кино, Видео, TV и Спорт', callback_data='7'),
                 InlineKeyboardButton('Мультфильмы', callback_data='8'),
                 InlineKeyboardButton('Мультсериалы', callback_data='9'),
                 InlineKeyboardButton('Аниме', callback_data='10'),
                 InlineKeyboardButton('Русские сериалы', callback_data='11'),
                 InlineKeyboardButton('Зарубежные сериалы', callback_data='12'),
                 InlineKeyboardButton('Зарубежные сериалы (HD Video)', callback_data='13'),
                 InlineKeyboardButton('Сериалы Латинской Америки, Турции и Индии', callback_data='14'),
                 InlineKeyboardButton('Азиатские сериалы', callback_data='15'),
                 InlineKeyboardButton('Вера и религия', callback_data='16'),
                 InlineKeyboardButton('Документальные фильмы и телепередачи', callback_data='17'),
                 InlineKeyboardButton('Документальные (HD Video)', callback_data='18'),
                 InlineKeyboardButton('Развлекательные телепередачи и шоу, приколы и юмор', callback_data='19'),
                 InlineKeyboardButton('Зимние Олимпийские игры 2018', callback_data='20'),
                 InlineKeyboardButton('Спортивные турниры, фильмы и передачи', callback_data='21'),
                 InlineKeyboardButton('⚽ Футбол', callback_data='22'),
                 InlineKeyboardButton('🏀 Баскетбол', callback_data='23'),
                 InlineKeyboardButton('🏒 Хоккей', callback_data='24'),
                 InlineKeyboardButton('Рестлинг', callback_data='25'),
                 InlineKeyboardButton('Сканирование, обработка сканов', callback_data='26'),
                 InlineKeyboardButton('Книги и журналы (общий раздел)', callback_data='27'),
                 InlineKeyboardButton('Для детей, родителей и учителей', callback_data='28'),
                 InlineKeyboardButton('Спорт, физическая культура, боевые искусства', callback_data='29'),
                 InlineKeyboardButton('Гуманитарные науки', callback_data='30'),
                 InlineKeyboardButton('Исторические науки', callback_data='31'),
                 InlineKeyboardButton('Точные, естественные и инженерные науки', callback_data='32'),
                 InlineKeyboardButton('Ноты и Музыкальная литература', callback_data='33'),
                 InlineKeyboardButton('Военное дело', callback_data='34'),
                 InlineKeyboardButton('Психология', callback_data='35'),
                 InlineKeyboardButton('Коллекционирование, увлечения и хобби', callback_data='36'),
                 InlineKeyboardButton('Художественная литература', callback_data='37'),
                 InlineKeyboardButton('Компьютерная литература', callback_data='38'),
                 InlineKeyboardButton('Комиксы, манга, ранобэ', callback_data='39'),
                 InlineKeyboardButton('Коллекции книг и библиотеки', callback_data='40'),
                 InlineKeyboardButton('Мультимедийные и интерактивные издания', callback_data='41'),
                 InlineKeyboardButton('Медицина и здоровье', callback_data='42'),
                 InlineKeyboardButton('Иностранные языки для взрослых', callback_data='43'),
                 InlineKeyboardButton('Иностранные языки для детей', callback_data='44'),
                 InlineKeyboardButton('Художественная литература (ин.языки)', callback_data='45'),
                 InlineKeyboardButton('Аудиокниги на иностранных языках', callback_data='46'),
                 InlineKeyboardButton('Видеоуроки и обучающие интерактивные DVD', callback_data='47'),
                 InlineKeyboardButton('Боевые искусства (Видеоуроки)', callback_data='48'),
                 InlineKeyboardButton('Компьютерные видеоуроки и обучающие интерактивные DVD', callback_data='49'),
                 InlineKeyboardButton('Радиоспектакли, история, мемуары', callback_data='50'),
                 InlineKeyboardButton('Фантастика, фэнтези, мистика, ужасы, фанфики', callback_data='51'),
                 InlineKeyboardButton('Религии', callback_data='52'),
                 InlineKeyboardButton('Прочая литература', callback_data='53'),
                 InlineKeyboardButton('Ремонт и эксплуатация транспортных средств', callback_data='54'),
                 InlineKeyboardButton('Фильмы и передачи по авто/мото', callback_data='55'),
                 InlineKeyboardButton('Классическая и современная академическая музыка', callback_data='56'),
                 InlineKeyboardButton('Фольклор, Народная и Этническая музыка', callback_data='57'),
                 InlineKeyboardButton('New Age, Relax, Meditative & Flamenco', callback_data='58'),
                 InlineKeyboardButton('Еще категории', callback_data='e1'),
                 InlineKeyboardButton('Меню', callback_data='m')
                 )
    bot.send_message(message.from_user.id, 'Выберите категорию из списка', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['categories117'])
def second_categories(message):
    keyboard = InlineKeyboardMarkup()

    keyboard.row_width = 1

    keyboard.add(InlineKeyboardButton('Рэп, Хип-Хоп, R\'n\'B', callback_data='59'),
                 InlineKeyboardButton('Reggae, Ska, Dub', callback_data='60'),
                 InlineKeyboardButton('Саундтреки, караоке и мюзиклы', callback_data='61'),
                 InlineKeyboardButton('Шансон, Авторская и Военная песня', callback_data='62'),
                 InlineKeyboardButton('Музыка других жанров', callback_data='63'),
                 InlineKeyboardButton('Отечественная поп-музыка', callback_data='64'),
                 InlineKeyboardButton('Зарубежная поп-музыка', callback_data='65'),
                 InlineKeyboardButton('Eurodance, Disco, Hi-NRG', callback_data='66'),
                 InlineKeyboardButton('Видео, DVD Video, HD Video (поп-музыка)', callback_data='67'),
                 InlineKeyboardButton('Зарубежный джаз', callback_data='68'),
                 InlineKeyboardButton('Зарубежный блюз', callback_data='69'),
                 InlineKeyboardButton('Отечественный джаз и блюз', callback_data='70'),
                 InlineKeyboardButton('Видео, DVD Video, HD Video (Джаз и блюз)', callback_data='71'),
                 InlineKeyboardButton('Зарубежный Rock', callback_data='72'),
                 InlineKeyboardButton('Зарубежный Metal', callback_data='73'),
                 InlineKeyboardButton('Зарубежные Alternative, Punk, Independent', callback_data='74'),
                 InlineKeyboardButton('Отечественный Rock, Metal', callback_data='75'),
                 InlineKeyboardButton('Видео, DVD Video, HD Video (Рок-музыка)', callback_data='76'),
                 InlineKeyboardButton('Trance, Goa Trance, Psy-Trance, PsyChill, Ambient, Dub', callback_data='77'),
                 InlineKeyboardButton('House, Techno, Hardcore, Hardstyle, Jumpstyle', callback_data='78'),
                 InlineKeyboardButton('Drum & Bass, Jungle, Breakbeat, Dubstep, IDM, Electro', callback_data='79'),
                 InlineKeyboardButton('Chillout, Lounge, Downtempo, Trip-Hop', callback_data='80'),
                 InlineKeyboardButton('Traditional Electronic, Ambient, Modern Classical, Electroacoustic, Ex..', callback_data='81'),
                 InlineKeyboardButton('Industrial, Noise, EBM, Dark Electro, Aggrotech, Synthpop, New Wave', callback_data='82'),
                 InlineKeyboardButton('Label Packs (lossless)', callback_data='83'),
                 InlineKeyboardButton('Label packs, Scene packs (lossy)', callback_data='84'),
                 InlineKeyboardButton('Электронная музыка (Видео, DVD Video, HD Video)', callback_data='85'),
                 InlineKeyboardButton('Hi-Res stereo и многоканальная музыка', callback_data='86'),
                 InlineKeyboardButton('Оцифровки с аналоговых носителей', callback_data='87'),
                 InlineKeyboardButton('Неофициальные конверсии цифровых форматов', callback_data='88'),
                 InlineKeyboardButton('Игры для Windows', callback_data='89'),
                 InlineKeyboardButton('Прочее для Windows-игр', callback_data='90'),
                 InlineKeyboardButton('Прочее для Microsoft Flight Simulator, Prepar3D, X-Plane', callback_data='91'),
                 InlineKeyboardButton('Игры для Macintosh', callback_data='92'),
                 InlineKeyboardButton('Игры для Linux', callback_data='93'),
                 InlineKeyboardButton('Игры для консолей', callback_data='94'),
                 InlineKeyboardButton('Видео для консолей', callback_data='95'),
                 InlineKeyboardButton('Игры для мобильных устройств', callback_data='96'),
                 InlineKeyboardButton('Игровое видео', callback_data='97'),
                 InlineKeyboardButton('Операционные системы от Microsoft', callback_data='98'),
                 InlineKeyboardButton('Linux, Unix и другие ОС', callback_data='99'),
                 InlineKeyboardButton('Тестовые диски для настройки аудио/видео аппаратуры', callback_data='100'),
                 InlineKeyboardButton('Системные программы', callback_data='101'),
                 InlineKeyboardButton('Системы для бизнеса, офиса, научной и проектной работы', callback_data='102'),
                 InlineKeyboardButton('Веб-разработка и Программирование', callback_data='103'),
                 InlineKeyboardButton('Программы для работы с мультимедиа и 3D', callback_data='104'),
                 InlineKeyboardButton('Материалы для мультимедиа и дизайна', callback_data='105'),
                 InlineKeyboardButton('ГИС, системы навигации и карты', callback_data='106'),
                 InlineKeyboardButton('Приложения для мобильных устройств', callback_data='107'),
                 InlineKeyboardButton('Видео для мобильных устройств', callback_data='108'),
                 InlineKeyboardButton('Apple Macintosh', callback_data='109'),
                 InlineKeyboardButton('iOS', callback_data='110'),
                 InlineKeyboardButton('Видео', callback_data='111'),
                 InlineKeyboardButton('Видео HD', callback_data='112'),
                 InlineKeyboardButton('Аудио', callback_data='113'),
                 InlineKeyboardButton('Разное (раздачи)', callback_data='114'),
                 InlineKeyboardButton('Тестовый форум', callback_data='115'),
                 InlineKeyboardButton('Еще категории', callback_data='e2'),
                 InlineKeyboardButton('Меню', callback_data='m')
                 )
    bot.send_message(message.from_user.id, 'Выберите категорию из списка', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['subcategories'])
def subcategories(message):
    global SUBCATEGORY
    no_subcategory_text = """Сперва необходимо выбрать категорию. Сделать это можно из меню по команде /start или с помощью \
    команд /categories58 и /categories117"""

    subcategory_choose_text = """Перенаправляю вас на выбор подкатегории. Обратите внимание, что в каждой категории \
    свое количество подкатегорий. В некоторых категориях подкатегорий нет."""

    if CATEGORY == None:
        send = bot.send_message(message.from_user.id, no_subcategory_text)
        bot.register_next_step_handler(send, first_categories)

    with open(cat_dict, 'r', encoding='utf-8') as dictionary:
        d = json.load(dictionary)
        ctgs = [x for i, x in enumerate(d)]
        subcategories = d[CATEGORY]
        if len(subcategories) == 0:
            SUBCATEGORY = None
            text = """У данной категории ({}) нет подкатегорий"""
            send = bot.send_message(message.from_user.id, text.format(CATEGORY))
            bot.register_next_step_handler(send, targetsearch(message))

        keyboard = InlineKeyboardMarkup()

        keyboard.row_width = 1

        for sbct in subcategories:
            clean_sbct = sbct.replace("'", "\'")
            clbk = '{}-{}'.format(ctgs.index(CATEGORY), subcategories.index(sbct))
            keyboard.add(InlineKeyboardButton(clean_sbct, callback_data=clbk))
        bot.send_message(message.from_user.id, subcategory_choose_text, reply_markup=keyboard)



@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['globalsearch'])
def globalsearch(message):
    bot.send_message(message.from_user.id, 'Здесь будет реализован глобальный поиск')


@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['targetsearch'])
def targetsearch(message):
    bot.send_message(message.from_user.id, 'Здесь будет реализован адресный поиск')



if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0, timeout=20)
    # bot.polling(none_stop=True)
    # bot.infinity_polling()
