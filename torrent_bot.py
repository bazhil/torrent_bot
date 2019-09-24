# -*- coding: utf-8 -*-

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import sqlite3
import json
import utils
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
    global SUBCATEGORY


    category_choose_text = """Перенаправляю вас на выбор категории. Обратите внимание, что всего 117 категорий, \
    но за 1 раз вам будет выведено только 58. На остальные категории вы сможете переключиться внутри меню выбора. \
    Если оно не выводится, вы можете вызвать его с помощью команд /categories58 и /categories117"""
    if call.data == 'Выбор категории 1-58' or call.data == 'e2':
        send = bot.send_message(call.from_user.id, category_choose_text)
        bot.register_next_step_handler(send, first_categories(call))
    elif call.data == 'Выбор категории 59-117' or call.data == 'e1':
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
    elif call.data == 'back':
        send = bot.send_message(call.from_user.id, 'Возвращаемся в выбор категорий')
        bot.register_next_step_handler(send, first_categories(call))
    elif call.data == '0-0':
        SUBCATEGORY = 'Конкурсы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '0-1':
        SUBCATEGORY = 'Rutracker Awards (Раздачи)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-0':
        SUBCATEGORY = 'Классика мирового кинематографа'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-1':
        SUBCATEGORY = 'Фильмы до 1990 года'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-2':
        SUBCATEGORY = 'Фильмы 1991-2000'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-3':
        SUBCATEGORY = 'Фильмы 2001-2005'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-4':
        SUBCATEGORY = 'Фильмы 2006-2010'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-5':
        SUBCATEGORY = 'Фильмы 2011-2015'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-6':
        SUBCATEGORY = 'Фильмы 2016-2018'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-7':
        SUBCATEGORY = 'Фильмы 2019'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-8':
        SUBCATEGORY = 'Фильмы Ближнего Зарубежья'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-9':
        SUBCATEGORY = 'Азиатские фильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-10':
        SUBCATEGORY = 'Индийское кино'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-11':
        SUBCATEGORY = 'Сборники фильмов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-12':
        SUBCATEGORY = 'Короткий метр'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-13':
        SUBCATEGORY = 'Грайндхаус'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '1-14':
        SUBCATEGORY = 'Звуковые дорожки и Переводы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '2-0':
        SUBCATEGORY = 'Кино СССР'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '2-1':
        SUBCATEGORY = 'Детские отечественные фильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '2-2':
        SUBCATEGORY = 'Авторские дебюты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '3-0':
        SUBCATEGORY = 'Короткий метр (Арт-хаус и авторское кино)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '3-1':
        SUBCATEGORY = 'Документальные фильмы (Арт-хаус и авторское кино)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '3-2':
        SUBCATEGORY = 'Анимация (Арт-хаус и авторское кино)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-0':
        SUBCATEGORY = 'Классика мирового кинематографа (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-1':
        SUBCATEGORY = 'Азиатские фильмы (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-2':
        SUBCATEGORY = 'Зарубежное кино (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-3':
        SUBCATEGORY = 'Наше кино (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-4':
        SUBCATEGORY = 'Фильмы Ближнего Зарубежья (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-5':
        SUBCATEGORY = 'Арт-хаус и авторское кино (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-6':
        SUBCATEGORY = 'Индийское кино (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '5-7':
        SUBCATEGORY = 'Грайндхаус (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-0':
        SUBCATEGORY = 'UHD Video'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-1':
        SUBCATEGORY = 'Классика мирового кинематографа (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-2':
        SUBCATEGORY = 'Зарубежное кино (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-3':
        SUBCATEGORY = 'Азиатские фильмы (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-4':
        SUBCATEGORY = 'Наше кино (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-5':
        SUBCATEGORY = 'Арт-хаус и авторское кино (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-6':
        SUBCATEGORY = 'Индийское кино (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '6-7':
        SUBCATEGORY = 'Грайндхаус (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '7-0':
        SUBCATEGORY = '3D Кинофильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '7-1':
        SUBCATEGORY = '3D Мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '7-2':
        SUBCATEGORY = '3D Документальные фильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '7-3':
        SUBCATEGORY = '3D Спорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '7-4':
        SUBCATEGORY = '3D Ролики, Музыкальное видео, Трейлеры к фильмам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-0':
        SUBCATEGORY = 'Отечественные мультфильмы (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-1':
        SUBCATEGORY = 'Иностранные мультфильмы (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-2':
        SUBCATEGORY = 'Иностранные короткометражные мультфильмы (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-3':
        SUBCATEGORY = 'Отечественные мультфильмы (DVD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-4':
        SUBCATEGORY = 'Иностранные мультфильмы (DVD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-5':
        SUBCATEGORY = 'Иностранные короткометражные мультфильмы (DVD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-6':
        SUBCATEGORY = 'Отечественные мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-7':
        SUBCATEGORY = 'Отечественные полнометражные мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-8':
        SUBCATEGORY = 'Иностранные мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-9':
        SUBCATEGORY = 'Иностранные короткометражные мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '8-10':
        SUBCATEGORY = 'Сборники мультфильмов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '9-0':
        SUBCATEGORY = 'Мультсериалы (SD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '9-1':
        SUBCATEGORY = 'Мультсериалы (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '9-2':
        SUBCATEGORY = 'Мультсериалы (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-0':
        SUBCATEGORY = 'Артбуки и журналы (Аниме)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-1':
        SUBCATEGORY = 'Обои, сканы, аватары, арт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-2':
        SUBCATEGORY = 'AMV и другие ролики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-3':
        SUBCATEGORY = 'Аниме (DVD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-4':
        SUBCATEGORY = 'Аниме (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-5':
        SUBCATEGORY = 'Аниме (основной подраздел)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-6':
        SUBCATEGORY = 'Аниме (плеерный подраздел)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-7':
        SUBCATEGORY = 'Аниме (QC подраздел)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-8':
        SUBCATEGORY = 'Покемоны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-9':
        SUBCATEGORY = 'Наруто'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-10':
        SUBCATEGORY = 'Гандам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-11':
        SUBCATEGORY = 'Японские мультфильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '10-12':
        SUBCATEGORY = 'Звуковые дорожки (Аниме)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-0':
        SUBCATEGORY = 'Возвращение Мухтара'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-1':
        SUBCATEGORY = 'Воронины'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-2':
        SUBCATEGORY = 'Глухарь / Пятницкий / Карпов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-3':
        SUBCATEGORY = 'Земский доктор'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-4':
        SUBCATEGORY = 'Каменская'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-5':
        SUBCATEGORY = 'Кухня / Отель Элеон'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-6':
        SUBCATEGORY = 'Ментовские войны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-7':
        SUBCATEGORY = 'Молодежка / Интерны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-8':
        SUBCATEGORY = 'Морские дьяволы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-9':
        SUBCATEGORY = 'Москва. Три вокзала'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-10':
        SUBCATEGORY = 'Нюхач'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-11':
        SUBCATEGORY = 'Обратная сторона Луны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-12':
        SUBCATEGORY = 'Ольга / Физрук'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-13':
        SUBCATEGORY = 'Пуля Дура'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-14':
        SUBCATEGORY = 'Сваты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-15':
        SUBCATEGORY = 'След'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-16':
        SUBCATEGORY = 'Солдаты и пр.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-17':
        SUBCATEGORY = 'Тайны следствия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '11-18':
        SUBCATEGORY = 'Улицы разбитых фонарей (Менты) / Опера / Убойная сила'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-0':
        SUBCATEGORY = 'Новинки и сериалы в стадии показа'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-1':
        SUBCATEGORY = 'Сериалы США и Канады'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-2':
        SUBCATEGORY = 'Сериалы Великобритании и Ирландии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-3':
        SUBCATEGORY = 'Скандинавские сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-4':
        SUBCATEGORY = 'Испанские сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-5':
        SUBCATEGORY = 'Итальянские сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-6':
        SUBCATEGORY = 'Европейские сериалы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-7':
        SUBCATEGORY = 'Сериалы стран Африки, Ближнего и Среднего Востока'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-8':
        SUBCATEGORY = 'Сериалы Австралии и Новой Зеландии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-9':
        SUBCATEGORY = 'Сериалы Ближнего Зарубежья'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-10':
        SUBCATEGORY = 'Сериалы совместного производства нескольких стран'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-11':
        SUBCATEGORY = 'Веб-сериалы, Вебизоды к сериалам и Пилотные серии сериалов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-12':
        SUBCATEGORY = 'Анатомия Грей + Частная Практика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-13':
        SUBCATEGORY = 'Бесстыжие / Shameless (US)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-14':
        SUBCATEGORY = 'Вавилон 5 / Babylon 5'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-15':
        SUBCATEGORY = 'Викинги / Vikings'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-16':
        SUBCATEGORY = 'Во все тяжкие / Breaking Bad'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-17':
        SUBCATEGORY = 'Дневники вампира + Настоящая кровь'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-18':
        SUBCATEGORY = 'Доктор Кто + Торчвуд'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-19':
        SUBCATEGORY = 'Доктор Хаус / House M.D.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-20':
        SUBCATEGORY = 'Друзья + Джоуи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-21':
        SUBCATEGORY = 'Звёздные Врата : Атлантида; Вселенная'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-22':
        SUBCATEGORY = 'Звёздные Врата: СГ1 / Stargate: SG1'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-23':
        SUBCATEGORY = 'Звёздный крейсер Галактика + Каприка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-24':
        SUBCATEGORY = 'Звёздный путь / Star Trek'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-25':
        SUBCATEGORY = 'Игра престолов / Game of Thrones'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-26':
        SUBCATEGORY = 'Карточный Домик / House of Cards'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-27':
        SUBCATEGORY = 'Клан Сопрано / The Sopranos'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-28':
        SUBCATEGORY = 'Кости / Bones'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-29':
        SUBCATEGORY = 'Менталист + Касл'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-30':
        SUBCATEGORY = 'Место преступления / CSI: Crime Scene Investigation'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-31':
        SUBCATEGORY = 'Морская полиция: Спецотдел; Лос-Анджелес; Новый Орлеан'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-32':
        SUBCATEGORY = 'Оранжевый — хит сезона / Orange Is the New Black'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-33':
        SUBCATEGORY = 'Остаться в Живых / LOST'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-34':
        SUBCATEGORY = 'Отчаянные домохозяйки / Desperate Housewives'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-35':
        SUBCATEGORY = 'Побег из тюрьмы / Prison Break'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-36':
        SUBCATEGORY = 'Сверхъестественное / Supernatural'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-37':
        SUBCATEGORY = 'Секретные материалы / The X-Files'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-38':
        SUBCATEGORY = 'Секс в большом городе / Sex And The City'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-39':
        SUBCATEGORY = 'Твин пикс / Twin Peaks'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-40':
        SUBCATEGORY = 'Теория большого взрыва / The Big Bang Theory'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-41':
        SUBCATEGORY = 'Форс-мажоры / Костюмы в законе / Suits'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-42':
        SUBCATEGORY = 'Ходячие мертвецы + Бойтесь ходячих мертвецов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-43':
        SUBCATEGORY = 'Черное зеркало / Black Mirror'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '12-44':
        SUBCATEGORY = 'Для некондиционных раздач'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-0':
        SUBCATEGORY = 'Викинги / Vikings (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-1':
        SUBCATEGORY = 'Друзья / Friends (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-2':
        SUBCATEGORY = 'Доктор Кто + Торчвуд (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-3':
        SUBCATEGORY = 'Доктор Хаус / House M.D. (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-4':
        SUBCATEGORY = 'Звёздные Врата (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-5':
        SUBCATEGORY = 'Звёздный крейсер Галактика + Каприка (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-6':
        SUBCATEGORY = 'Звёздный путь / Star Trek (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-7':
        SUBCATEGORY = 'Игра престолов / Game of Thrones (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-8':
        SUBCATEGORY = 'Карточный домик (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-9':
        SUBCATEGORY = 'Кости / Bones (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-10':
        SUBCATEGORY = 'Менталист + Касл (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-11':
        SUBCATEGORY = 'Место преступления / CSI: Crime Scene Investigation (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-12':
        SUBCATEGORY = 'Оранжевый — хит сезона / Orange Is the New Black (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-13':
        SUBCATEGORY = 'Остаться в Живых / LOST (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-14':
        SUBCATEGORY = 'Побег из тюрьмы / Prison Break (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-15':
        SUBCATEGORY = 'Сверхъестественное / Supernatural (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-16':
        SUBCATEGORY = 'Секретные материалы / The X-Files (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-17':
        SUBCATEGORY = 'Твин пикс / Twin Peaks (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-18':
        SUBCATEGORY = 'Теория Большого Взрыва / The Big Bang Theory (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-19':
        SUBCATEGORY = 'Ходячие мертвецы + Бойтесь ходячих мертвецов (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-20':
        SUBCATEGORY = 'Черное зеркало / Black Mirror (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '13-21':
        SUBCATEGORY = 'Для некондиционных раздач (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-0':
        SUBCATEGORY = 'Актёры и актрисы латиноамериканских сериалов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-1':
        SUBCATEGORY = 'Сериалы Аргентины'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-2':
        SUBCATEGORY = 'Сериалы Бразилии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-3':
        SUBCATEGORY = 'Сериалы Венесуэлы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-4':
        SUBCATEGORY = 'Сериалы Индии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-5':
        SUBCATEGORY = 'Сериалы Колумбии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-6':
        SUBCATEGORY = 'Сериалы Латинской Америки с озвучкой (раздачи папками)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-7':
        SUBCATEGORY = 'Сериалы Латинской Америки с субтитрами'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-8':
        SUBCATEGORY = 'Официальные краткие версии сериалов Латинской Америки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-9':
        SUBCATEGORY = 'Сериалы Мексики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-10':
        SUBCATEGORY = 'Сериалы Перу, Сальвадора, Чили и других стран'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-11':
        SUBCATEGORY = 'Сериалы совместного производства'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-12':
        SUBCATEGORY = 'Сериалы США (латиноамериканские)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-13':
        SUBCATEGORY = 'Сериалы Турции'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-14':
        SUBCATEGORY = 'Для некондиционных раздач'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '14-15':
        SUBCATEGORY = 'OST Сериалы Латинской Америки, Турции и Индии (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-0':
        SUBCATEGORY = 'Китайские сериалы с субтитрами'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-1':
        SUBCATEGORY = 'Корейские сериалы с озвучкой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-2':
        SUBCATEGORY = 'Корейские сериалы с субтитрами'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-3':
        SUBCATEGORY = 'Прочие азиатские сериалы с озвучкой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-4':
        SUBCATEGORY = 'Тайваньские сериалы с субтитрами'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-5':
        SUBCATEGORY = 'Японские сериалы с субтитрами'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-6':
        SUBCATEGORY = 'Японские сериалы с озвучкой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-7':
        SUBCATEGORY = 'VMV и др. ролики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '15-8':
        SUBCATEGORY = 'OST Азиатские сериалы (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '16-0':
        SUBCATEGORY = '[Видео Религия] Христианство'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '16-1':
        SUBCATEGORY = '[Видео Религия] Ислам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '16-2':
        SUBCATEGORY = '[Видео Религия] Религии Индии, Тибета и Восточной Азии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '16-3':
        SUBCATEGORY = '[Видео Религия] Культы и новые религиозные движения'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-0':
        SUBCATEGORY = 'Документальные (DVD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-1':
        SUBCATEGORY = '[Док] Биографии. Личности и кумиры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-2':
        SUBCATEGORY = '[Док] Кинематограф и мультипликация'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-3':
        SUBCATEGORY = '[Док] Мастера искусств Театра и Кино'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-4':
        SUBCATEGORY = '[Док] Искусство, история искусств'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-5':
        SUBCATEGORY = '[Док] Музыка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-6':
        SUBCATEGORY = '[Док] Криминальная документалистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-7':
        SUBCATEGORY = '[Док] Тайны века / Спецслужбы / Теории Заговоров'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-8':
        SUBCATEGORY = '[Док] Военное дело'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-9':
        SUBCATEGORY = '[Док] Вторая мировая война'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-10':
        SUBCATEGORY = '[Док] Аварии / Катастрофы / Катаклизмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-11':
        SUBCATEGORY = '[Док] Авиация'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-12':
        SUBCATEGORY = '[Док] Космос'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-13':
        SUBCATEGORY = '[Док] Научно-популярные фильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-14':
        SUBCATEGORY = '[Док] Флора и фауна'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-15':
        SUBCATEGORY = '[Док] Путешествия и туризм'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-16':
        SUBCATEGORY = '[Док] Медицина'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-17':
        SUBCATEGORY = '[Док] Социальные ток-шоу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-18':
        SUBCATEGORY = '[Док] Информационно-аналитические и общественно-политические перед..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-19':
        SUBCATEGORY = '[Док] Архитектура и строительство'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-20':
        SUBCATEGORY = '[Док] Всё о доме, быте и дизайне'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-21':
        SUBCATEGORY = '[Док] BBC'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-22':
        SUBCATEGORY = '[Док] Discovery'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-23':
        SUBCATEGORY = '[Док] National Geographic'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-24':
        SUBCATEGORY = '[Док] История: Древний мир / Античность / Средневековье'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-25':
        SUBCATEGORY = '[Док] История: Новое и Новейшее время'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-26':
        SUBCATEGORY = '[Док] Эпоха СССР'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-27':
        SUBCATEGORY = '[Док] Битва экстрасенсов / Теория невероятности / Искатели / Галил..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-28':
        SUBCATEGORY = '[Док] Русские сенсации / Программа Максимум / Профессия репортёр'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-29':
        SUBCATEGORY = '[Док] Паранормальные явления'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-30':
        SUBCATEGORY = '[Док] Альтернативная история и наука'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-31':
        SUBCATEGORY = '[Док] Внежанровая документалистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '17-32':
        SUBCATEGORY = '[Док] Разное / некондиция'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-0':
        SUBCATEGORY = 'Информационно-аналитические и общественно-политические (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-1':
        SUBCATEGORY = 'Биографии. Личности и кумиры (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-2':
        SUBCATEGORY = 'Военное дело (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-3':
        SUBCATEGORY = 'Естествознание, наука и техника (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-4':
        SUBCATEGORY = 'Путешествия и туризм (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-5':
        SUBCATEGORY = 'Флора и фауна (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-6':
        SUBCATEGORY = 'История (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-7':
        SUBCATEGORY = 'BBC, Discovery, National Geographic (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '18-8':
        SUBCATEGORY = 'Криминальная документалистика (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-0':
        SUBCATEGORY = '[Видео Юмор] Интеллектуальные игры и викторины'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-1':
        SUBCATEGORY = '[Видео Юмор] Реалити и ток-шоу / номинации / показы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-2':
        SUBCATEGORY = '[Видео Юмор] Детские телешоу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-3':
        SUBCATEGORY = '[Видео Юмор] КВН'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-4':
        SUBCATEGORY = '[Видео Юмор] Пост КВН'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-5':
        SUBCATEGORY = '[Видео Юмор] Кривое Зеркало / Городок / В Городке'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-6':
        SUBCATEGORY = '[Видео Юмор] Ледовые шоу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-7':
        SUBCATEGORY = '[Видео Юмор] Музыкальные шоу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-8':
        SUBCATEGORY = '[Видео Юмор] Званый ужин'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-9':
        SUBCATEGORY = '[Видео Юмор] Хорошие Шутки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-10':
        SUBCATEGORY = '[Видео Юмор] Вечерний Квартал'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-11':
        SUBCATEGORY = '[Видео Юмор] Фильмы со смешным переводом (пародии)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-12':
        SUBCATEGORY = '[Видео Юмор] Stand-up comedy'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-13':
        SUBCATEGORY = '[Видео Юмор] Украинские Шоу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-14':
        SUBCATEGORY = '[Видео Юмор] Танцевальные шоу, концерты, выступления'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-15':
        SUBCATEGORY = '[Видео Юмор] Цирк'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-16':
        SUBCATEGORY = '[Видео Юмор] Школа злословия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-17':
        SUBCATEGORY = '[Видео Юмор] Сатирики и юмористы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-18':
        SUBCATEGORY = 'Юмористические аудиопередачи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '19-19':
        SUBCATEGORY = 'Аудио и видео ролики (Приколы и юмор)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-0':
        SUBCATEGORY = 'Биатлон'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-1':
        SUBCATEGORY = 'Лыжные гонки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-2':
        SUBCATEGORY = 'Прыжки на лыжах с трамплина / Лыжное двоеборье'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-3':
        SUBCATEGORY = 'Горные лыжи / Сноубординг / Фристайл'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-4':
        SUBCATEGORY = 'Бобслей / Санный спорт / Скелетон'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-5':
        SUBCATEGORY = 'Конькобежный спорт / Шорт-трек'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-6':
        SUBCATEGORY = 'Фигурное катание'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-7':
        SUBCATEGORY = 'Хоккей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-8':
        SUBCATEGORY = 'Керлинг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '20-9':
        SUBCATEGORY = 'Обзорные и аналитические программы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-0':
        SUBCATEGORY = 'Автоспорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-1':
        SUBCATEGORY = 'Мотоспорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-2':
        SUBCATEGORY = 'Формула-1 (2018)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-3':
        SUBCATEGORY = 'Формула-1 (2012-2017)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-4':
        SUBCATEGORY = 'Формула 1 (до 2011 вкл.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-5':
        SUBCATEGORY = 'Велоспорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-6':
        SUBCATEGORY = 'Волейбол/Гандбол'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-7':
        SUBCATEGORY = 'Бильярд'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-8':
        SUBCATEGORY = 'Покер'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-9':
        SUBCATEGORY = 'Бодибилдинг/Силовые виды спорта'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-10':
        SUBCATEGORY = 'Бокс'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-11':
        SUBCATEGORY = 'Классические единоборства'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-12':
        SUBCATEGORY = 'Смешанные единоборства и K-1'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-13':
        SUBCATEGORY = 'Американский футбол'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-14':
        SUBCATEGORY = 'Регби'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-15':
        SUBCATEGORY = 'Бейсбол'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-16':
        SUBCATEGORY = 'Теннис'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-17':
        SUBCATEGORY = 'Бадминтон/Настольный теннис'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-18':
        SUBCATEGORY = 'Гимнастика/Соревнования по танцам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-19':
        SUBCATEGORY = 'Лёгкая атлетика/Водные виды спорта'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-20':
        SUBCATEGORY = 'Зимние виды спорта'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-21':
        SUBCATEGORY = 'Фигурное катание'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-22':
        SUBCATEGORY = 'Биатлон'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-23':
        SUBCATEGORY = 'Экстрим'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '21-24':
        SUBCATEGORY = 'Спорт (видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-0':
        SUBCATEGORY = 'Чемпионат Мира 2018 (плей-офф финального турнира)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-1':
        SUBCATEGORY = 'Чемпионат Мира 2018 (групповой этап финального турнира)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-2':
        SUBCATEGORY = 'Чемпионат Мира 2018 (обзорные передачи, документалистика)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-3':
        SUBCATEGORY = 'Чемпионат Мира 2018 (отборочный турнир)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-4':
        SUBCATEGORY = 'Чемпионаты Мира'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-5':
        SUBCATEGORY = 'Россия 2018-2019'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-6':
        SUBCATEGORY = 'Лига Наций 2018'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-7':
        SUBCATEGORY = 'Товарищеские турниры и матчи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-8':
        SUBCATEGORY = 'Россия/СССР'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-9':
        SUBCATEGORY = 'Англия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-10':
        SUBCATEGORY = 'Испания'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-11':
        SUBCATEGORY = 'Италия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-12':
        SUBCATEGORY = 'Германия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-13':
        SUBCATEGORY = 'Франция'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-14':
        SUBCATEGORY = 'Украина'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-15':
        SUBCATEGORY = 'Другие национальные чемпионаты и кубки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-16':
        SUBCATEGORY = 'Международные турниры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-17':
        SUBCATEGORY = 'Еврокубки 2018-2019'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-18':
        SUBCATEGORY = 'Еврокубки 2017-2018'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-19':
        SUBCATEGORY = 'Еврокубки 2011-2017'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-20':
        SUBCATEGORY = 'Еврокубки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-21':
        SUBCATEGORY = 'Чемпионаты Европы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-22':
        SUBCATEGORY = 'Обзорные и аналитические передачи 2018-2019'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-23':
        SUBCATEGORY = 'Обзорные и аналитические передачи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '22-24':
        SUBCATEGORY = 'Мини-футбол/Пляжный футбол'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '23-0':
        SUBCATEGORY = 'Международные соревнования'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '23-1':
        SUBCATEGORY = 'NBA / NCAA (до 2000 г.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '23-2':
        SUBCATEGORY = 'NBA / NCAA (2000-2010 гг.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '23-3':
        SUBCATEGORY = 'NBA / NCAA (2010-2019 гг.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '23-4':
        SUBCATEGORY = 'Европейский клубный баскетбол'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-0':
        SUBCATEGORY = 'Хоккей с мячом / Бенди'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-1':
        SUBCATEGORY = 'Международные турниры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-2':
        SUBCATEGORY = 'КХЛ'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-3':
        SUBCATEGORY = 'НХЛ (до 2011/12)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-4':
        SUBCATEGORY = 'НХЛ (с 2013)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-5':
        SUBCATEGORY = 'СССР - Канада'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '24-6':
        SUBCATEGORY = 'Документальные фильмы и аналитика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '25-0':
        SUBCATEGORY = 'Professional Wrestling'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '25-1':
        SUBCATEGORY = 'Independent Wrestling'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '25-2':
        SUBCATEGORY = 'International Wrestling'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '25-3':
        SUBCATEGORY = 'Oldschool Wrestling'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '25-4':
        SUBCATEGORY = 'Documentary Wrestling'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-0':
        SUBCATEGORY = 'Кино, театр, ТВ, мультипликация, цирк'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-1':
        SUBCATEGORY = 'Рисунок, графический дизайн'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-2':
        SUBCATEGORY = 'Фото и видеосъемка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-3':
        SUBCATEGORY = 'Журналы и газеты (общий раздел)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-4':
        SUBCATEGORY = 'Эзотерика, гадания, магия, фен-шуй'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-5':
        SUBCATEGORY = 'Астрология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-6':
        SUBCATEGORY = 'Красота. Уход. Домоводство'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-7':
        SUBCATEGORY = 'Мода. Стиль. Этикет'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-8':
        SUBCATEGORY = 'Путешествия и туризм'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-9':
        SUBCATEGORY = 'Знаменитости и кумиры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '27-10':
        SUBCATEGORY = 'Разное (книги)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-0':
        SUBCATEGORY = 'Учебная литература для детского сада и начальной школы (до 4 класс..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-1':
        SUBCATEGORY = 'Учебная литература для старших классов (5-11 класс)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-2':
        SUBCATEGORY = 'Учителям и педагогам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-3':
        SUBCATEGORY = 'Научно-популярная и познавательная литература (для детей)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-4':
        SUBCATEGORY = 'Досуг и творчество'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-5':
        SUBCATEGORY = 'Воспитание и развитие'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-6':
        SUBCATEGORY = 'Худ. лит-ра для дошкольников и младших классов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '28-7':
        SUBCATEGORY = 'Худ. лит-ра для средних и старших классов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-0':
        SUBCATEGORY = 'Футбол (книги и журналы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-1':
        SUBCATEGORY = 'Хоккей (книги и журналы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-2':
        SUBCATEGORY = 'Игровые виды спорта'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-3':
        SUBCATEGORY = 'Легкая атлетика. Плавание. Гимнастика. Тяжелая атлетика. Гребля'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-4':
        SUBCATEGORY = 'Автоспорт. Мотоспорт. Велоспорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-5':
        SUBCATEGORY = 'Шахматы. Шашки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-6':
        SUBCATEGORY = 'Боевые искусства, единоборства'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-7':
        SUBCATEGORY = 'Экстрим (книги)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-8':
        SUBCATEGORY = 'Физкультура, фитнес, бодибилдинг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '29-9':
        SUBCATEGORY = 'Спортивная пресса'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-0':
        SUBCATEGORY = 'Искусствоведение. Культурология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-1':
        SUBCATEGORY = 'Фольклор. Эпос. Мифология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-2':
        SUBCATEGORY = 'Литературоведение'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-3':
        SUBCATEGORY = 'Лингвистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-4':
        SUBCATEGORY = 'Философия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-5':
        SUBCATEGORY = 'Политология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-6':
        SUBCATEGORY = 'Социология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-7':
        SUBCATEGORY = 'Публицистика, журналистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-8':
        SUBCATEGORY = 'Бизнес, менеджмент'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-9':
        SUBCATEGORY = 'Маркетинг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-10':
        SUBCATEGORY = 'Экономика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-11':
        SUBCATEGORY = 'Финансы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '30-12':
        SUBCATEGORY = 'Юридические науки. Право. Криминалистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-0':
        SUBCATEGORY = 'Методология и философия исторической науки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-1':
        SUBCATEGORY = 'Исторические источники (книги, периодика)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-2':
        SUBCATEGORY = 'Исторические источники (документы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-3':
        SUBCATEGORY = 'Исторические персоны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-4':
        SUBCATEGORY = 'Альтернативные исторические теории'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-5':
        SUBCATEGORY = 'Археология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-6':
        SUBCATEGORY = 'Древний мир. Античность'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-7':
        SUBCATEGORY = 'Средние века'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-8':
        SUBCATEGORY = 'История Нового и Новейшего времени'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-9':
        SUBCATEGORY = 'История Европы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-10':
        SUBCATEGORY = 'История Азии и Африки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-11':
        SUBCATEGORY = 'История Америки, Австралии, Океании'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-12':
        SUBCATEGORY = 'История России'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-13':
        SUBCATEGORY = 'Эпоха СССР'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-14':
        SUBCATEGORY = 'История стран бывшего СССР'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-15':
        SUBCATEGORY = 'Этнография, антропология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '31-16':
        SUBCATEGORY = 'Международные отношения. Дипломатия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-0':
        SUBCATEGORY = 'Авиация / Космонавтика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-1':
        SUBCATEGORY = 'Физика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-2':
        SUBCATEGORY = 'Астрономия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-3':
        SUBCATEGORY = 'Биология / Экология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-4':
        SUBCATEGORY = 'Химия / Биохимия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-5':
        SUBCATEGORY = 'Математика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-6':
        SUBCATEGORY = 'География / Геология / Геодезия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-7':
        SUBCATEGORY = 'Электроника / Радио'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-8':
        SUBCATEGORY = 'Схемы и сервис-мануалы (оригинальная документация)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-9':
        SUBCATEGORY = 'Архитектура / Строительство / Инженерные сети'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-10':
        SUBCATEGORY = 'Машиностроение'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-11':
        SUBCATEGORY = 'Сварка / Пайка / Неразрушающий контроль'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-12':
        SUBCATEGORY = 'Автоматизация / Робототехника'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-13':
        SUBCATEGORY = 'Металлургия / Материаловедение'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-14':
        SUBCATEGORY = 'Механика, сопротивление материалов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-15':
        SUBCATEGORY = 'Энергетика / электротехника'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-16':
        SUBCATEGORY = 'Нефтяная, газовая и химическая промышленность'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-17':
        SUBCATEGORY = 'Сельское хозяйство и пищевая промышленность'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-18':
        SUBCATEGORY = 'Железнодорожное дело'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-19':
        SUBCATEGORY = 'Нормативная документация'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '32-20':
        SUBCATEGORY = 'Журналы: научные, научно-популярные, радио и др.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '33-0':
        SUBCATEGORY = 'Академическая музыка (Ноты и Media CD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '33-1':
        SUBCATEGORY = 'Другие направления (Ноты, табулатуры)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '33-2':
        SUBCATEGORY = 'Самоучители и Школы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '33-3':
        SUBCATEGORY = 'Песенники (Songbooks)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '33-4':
        SUBCATEGORY = 'Музыкальная литература и Теория'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '33-5':
        SUBCATEGORY = 'Музыкальные журналы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-0':
        SUBCATEGORY = 'Милитария'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-1':
        SUBCATEGORY = 'Военная история'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-2':
        SUBCATEGORY = 'История Второй мировой войны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-3':
        SUBCATEGORY = 'Биографии и мемуары военных деятелей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-4':
        SUBCATEGORY = 'Военная техника'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-5':
        SUBCATEGORY = 'Стрелковое оружие'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-6':
        SUBCATEGORY = 'Учебно-методическая литература'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '34-7':
        SUBCATEGORY = 'Спецслужбы мира'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-0':
        SUBCATEGORY = 'Общая и прикладная психология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-1':
        SUBCATEGORY = 'Психотерапия и консультирование'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-2':
        SUBCATEGORY = 'Психодиагностика и психокоррекция'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-3':
        SUBCATEGORY = 'Социальная психология и психология отношений'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-4':
        SUBCATEGORY = 'Тренинг и коучинг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-5':
        SUBCATEGORY = 'Саморазвитие и самосовершенствование'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-6':
        SUBCATEGORY = 'Популярная психология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '35-7':
        SUBCATEGORY = 'Сексология. Взаимоотношения полов (18+)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-0':
        SUBCATEGORY = 'Коллекционирование и вспомогательные ист. дисциплины'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-1':
        SUBCATEGORY = 'Вышивание'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-2':
        SUBCATEGORY = 'Вязание'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-3':
        SUBCATEGORY = 'Шитье, пэчворк'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-4':
        SUBCATEGORY = 'Кружевоплетение'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-5':
        SUBCATEGORY = 'Бисероплетение. Ювелирика. Украшения из проволоки.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-6':
        SUBCATEGORY = 'Бумажный арт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-7':
        SUBCATEGORY = 'Другие виды декоративно-прикладного искусства'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-8':
        SUBCATEGORY = 'Домашние питомцы и аквариумистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-9':
        SUBCATEGORY = 'Охота и рыбалка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-10':
        SUBCATEGORY = 'Кулинария (книги)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-11':
        SUBCATEGORY = 'Кулинария (газеты и журналы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-12':
        SUBCATEGORY = 'Моделизм'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-13':
        SUBCATEGORY = 'Приусадебное хозяйство / Цветоводство'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-14':
        SUBCATEGORY = 'Ремонт, частное строительство, дизайн интерьеров'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-15':
        SUBCATEGORY = 'Деревообработка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-16':
        SUBCATEGORY = 'Настольные игры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '36-17':
        SUBCATEGORY = 'Прочие хобби'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-0':
        SUBCATEGORY = 'Русская литература'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-1':
        SUBCATEGORY = 'Зарубежная литература (до 1900 г.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-2':
        SUBCATEGORY = 'Зарубежная литература (XX и XXI век)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-3':
        SUBCATEGORY = 'Детектив, боевик'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-4':
        SUBCATEGORY = 'Женский роман'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-5':
        SUBCATEGORY = 'Отечественная фантастика / фэнтези / мистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-6':
        SUBCATEGORY = 'Зарубежная фантастика / фэнтези / мистика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-7':
        SUBCATEGORY = 'Приключения'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '37-8':
        SUBCATEGORY = 'Литературные журналы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-0':
        SUBCATEGORY = 'Программы от Microsoft'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-1':
        SUBCATEGORY = 'Другие программы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-2':
        SUBCATEGORY = 'Mac OS; Linux, FreeBSD и прочие *NIX'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-3':
        SUBCATEGORY = 'СУБД'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-4':
        SUBCATEGORY = 'Веб-дизайн и программирование'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-5':
        SUBCATEGORY = 'Программирование (книги)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-6':
        SUBCATEGORY = 'Графика, обработка видео'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-7':
        SUBCATEGORY = 'Сети / VoIP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-8':
        SUBCATEGORY = 'Хакинг и безопасность'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-9':
        SUBCATEGORY = 'Железо (книги о ПК)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-10':
        SUBCATEGORY = 'Инженерные и научные программы (книги)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-11':
        SUBCATEGORY = 'Компьютерные журналы и приложения к ним'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '38-12':
        SUBCATEGORY = 'Дисковые приложения к игровым журналам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-0':
        SUBCATEGORY = 'Комиксы на русском языке'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-1':
        SUBCATEGORY = 'Комиксы издательства Marvel'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-2':
        SUBCATEGORY = 'Комиксы издательства DC'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-3':
        SUBCATEGORY = 'Комиксы других издательств'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-4':
        SUBCATEGORY = 'Комиксы на других языках'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-5':
        SUBCATEGORY = 'Манга (на русском языке)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-6':
        SUBCATEGORY = 'Манга (на иностранных языках)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '39-7':
        SUBCATEGORY = 'Ранобэ'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '40-0':
        SUBCATEGORY = 'Библиотеки (зеркала сетевых библиотек/коллекций)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '40-1':
        SUBCATEGORY = 'Тематические коллекции (подборки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '40-2':
        SUBCATEGORY = 'Многопредметные коллекции (подборки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '41-0':
        SUBCATEGORY = 'Мультимедийные энциклопедии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '41-1':
        SUBCATEGORY = 'Интерактивные обучающие и развивающие материалы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '41-2':
        SUBCATEGORY = 'Обучающие издания для детей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '41-3':
        SUBCATEGORY = 'Кулинария. Цветоводство. Домоводство'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '41-4':
        SUBCATEGORY = 'Культура. Искусство. История'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-0':
        SUBCATEGORY = 'Клиническая медицина до 1980 г.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-1':
        SUBCATEGORY = 'Клиническая медицина с 1980 по 2000 г.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-2':
        SUBCATEGORY = 'Клиническая медицина после 2000 г.'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-3':
        SUBCATEGORY = 'Научная медицинская периодика (газеты и журналы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-4':
        SUBCATEGORY = 'Медико-биологические науки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-5':
        SUBCATEGORY = 'Фармация и фармакология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-6':
        SUBCATEGORY = 'Популярная медицинская периодика (газеты и журналы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-7':
        SUBCATEGORY = 'Нетрадиционная, народная медицина и популярные книги о здоровье'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-8':
        SUBCATEGORY = 'Ветеринария, разное'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '42-9':
        SUBCATEGORY = 'Тематические коллекции книг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-0':
        SUBCATEGORY = 'Английский язык (для взрослых)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-1':
        SUBCATEGORY = 'Немецкий язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-2':
        SUBCATEGORY = 'Французский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-3':
        SUBCATEGORY = 'Испанский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-4':
        SUBCATEGORY = 'Итальянский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-5':
        SUBCATEGORY = 'Финский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-6':
        SUBCATEGORY = 'Другие европейские языки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-7':
        SUBCATEGORY = 'Арабский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-8':
        SUBCATEGORY = 'Китайский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-9':
        SUBCATEGORY = 'Японский язык'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-10':
        SUBCATEGORY = 'Другие восточные языки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-11':
        SUBCATEGORY = 'Русский язык как иностранный'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-12':
        SUBCATEGORY = 'Мультиязычные сборники'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-13':
        SUBCATEGORY = 'LIM-курсы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '43-14':
        SUBCATEGORY = 'Разное (иностранные языки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '44-0':
        SUBCATEGORY = 'Английский язык (для детей)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '44-1':
        SUBCATEGORY = 'Другие европейские языки (для детей)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '44-2':
        SUBCATEGORY = 'Восточные языки (для детей)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '44-3':
        SUBCATEGORY = 'Школьные учебники, ЕГЭ'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '45-0':
        SUBCATEGORY = 'Художественная литература на английском языке'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '45-1':
        SUBCATEGORY = 'Художественная литература на французском языке'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '45-2':
        SUBCATEGORY = 'Художественная литература на других европейских языках'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '45-3':
        SUBCATEGORY = 'Художественная литература на восточных языках'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '46-0':
        SUBCATEGORY = 'Аудиокниги на английском языке'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '46-1':
        SUBCATEGORY = 'Аудиокниги на немецком языке'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '46-2':
        SUBCATEGORY = 'Аудиокниги на других иностранных языках'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-0':
        SUBCATEGORY = 'Кулинария'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-1':
        SUBCATEGORY = 'Спорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-2':
        SUBCATEGORY = 'Фитнес - Кардио-Силовые Тренировки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-3':
        SUBCATEGORY = 'Фитнес - Разум и Тело'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-4':
        SUBCATEGORY = 'Бодибилдинг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-5':
        SUBCATEGORY = 'Оздоровительные практики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-6':
        SUBCATEGORY = 'Йога'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-7':
        SUBCATEGORY = 'Видео- и фотосъёмка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-8':
        SUBCATEGORY = 'Уход за собой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-9':
        SUBCATEGORY = 'Рисование'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-10':
        SUBCATEGORY = 'Игра на гитаре'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-11':
        SUBCATEGORY = 'Ударные инструменты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-12':
        SUBCATEGORY = 'Другие музыкальные инструменты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-13':
        SUBCATEGORY = 'Игра на бас-гитаре'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-14':
        SUBCATEGORY = 'Бальные танцы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-15':
        SUBCATEGORY = 'Танец живота'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-16':
        SUBCATEGORY = 'Уличные и клубные танцы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-17':
        SUBCATEGORY = 'Танцы, разное'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-18':
        SUBCATEGORY = 'Охота'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-19':
        SUBCATEGORY = 'Рыболовство и подводная охота'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-20':
        SUBCATEGORY = 'Фокусы и трюки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-21':
        SUBCATEGORY = 'Образование'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-22':
        SUBCATEGORY = 'Финансы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-23':
        SUBCATEGORY = 'Продажи, бизнес'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-24':
        SUBCATEGORY = 'Беременность, роды, материнство'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-25':
        SUBCATEGORY = 'Учебные видео для детей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-26':
        SUBCATEGORY = 'Психология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-27':
        SUBCATEGORY = 'Эзотерика, саморазвитие'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-28':
        SUBCATEGORY = 'Пикап, знакомства'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-29':
        SUBCATEGORY = 'Строительство, ремонт и дизайн'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-30':
        SUBCATEGORY = 'Дерево- и металлообработка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-31':
        SUBCATEGORY = 'Растения и животные'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-32':
        SUBCATEGORY = 'Хобби и рукоделие'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-33':
        SUBCATEGORY = 'Медицина и стоматология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-34':
        SUBCATEGORY = 'Психотерапия и клиническая психология'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-35':
        SUBCATEGORY = 'Массаж'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-36':
        SUBCATEGORY = 'Здоровье'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-37':
        SUBCATEGORY = 'Медицина - интерактивный софт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '47-38':
        SUBCATEGORY = 'Разное'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-0':
        SUBCATEGORY = 'Айкидо и айки-дзюцу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-1':
        SUBCATEGORY = 'Вин чун'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-2':
        SUBCATEGORY = 'Джиу-джитсу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-3':
        SUBCATEGORY = 'Дзюдо и самбо'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-4':
        SUBCATEGORY = 'Каратэ'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-5':
        SUBCATEGORY = 'Работа с оружием'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-6':
        SUBCATEGORY = 'Русский стиль'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-7':
        SUBCATEGORY = 'Рукопашный бой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-8':
        SUBCATEGORY = 'Смешанные стили'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-9':
        SUBCATEGORY = 'Ударные стили'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-10':
        SUBCATEGORY = 'Ушу'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '48-11':
        SUBCATEGORY = 'Разное'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-0':
        SUBCATEGORY = 'Компьютерные сети и безопасность'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-1':
        SUBCATEGORY = 'ОС и серверные программы Microsoft'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-2':
        SUBCATEGORY = 'Офисные программы Microsoft'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-3':
        SUBCATEGORY = 'ОС и программы семейства UNIX'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-4':
        SUBCATEGORY = 'Adobe Photoshop'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-5':
        SUBCATEGORY = 'Autodesk Maya'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-6':
        SUBCATEGORY = 'Autodesk 3ds Max'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-7':
        SUBCATEGORY = 'Autodesk Softimage (XSI)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-8':
        SUBCATEGORY = 'ZBrush'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-9':
        SUBCATEGORY = 'Flash, Flex и ActionScript'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-10':
        SUBCATEGORY = '2D-графика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-11':
        SUBCATEGORY = '3D-графика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-12':
        SUBCATEGORY = 'Инженерные и научные программы (видеоуроки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-13':
        SUBCATEGORY = 'Web-дизайн'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-14':
        SUBCATEGORY = 'WEB, SMM, SEO, интернет-маркетинг'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-15':
        SUBCATEGORY = 'Программирование (видеоуроки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-16':
        SUBCATEGORY = 'Программы для Mac OS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-17':
        SUBCATEGORY = 'Работа с видео'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-18':
        SUBCATEGORY = 'Работа со звуком'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '49-19':
        SUBCATEGORY = 'Разное (Компьютерные видеоуроки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '50-0':
        SUBCATEGORY = '[Аудио] Радиоспектакли и литературные чтения'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '50-1':
        SUBCATEGORY = '[Аудио] Жизнь замечательных людей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '50-2':
        SUBCATEGORY = '[Аудио] История, культурология, философия'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '51-0':
        SUBCATEGORY = '[Аудио] Зарубежная фантастика, фэнтези, мистика, ужасы, фанфики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '51-1':
        SUBCATEGORY = '[Аудио] Российская фантастика, фэнтези, мистика, ужасы, фанфики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '51-2':
        SUBCATEGORY = '[Аудио] Любовно-фантастический роман'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '51-3':
        SUBCATEGORY = '[Аудио] Сборники/разное Фантастика, фэнтези, мистика, ужасы, фанфи..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '52-0':
        SUBCATEGORY = '[Аудио] Православие'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '52-1':
        SUBCATEGORY = '[Аудио] Ислам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '52-2':
        SUBCATEGORY = '[Аудио] Другие традиционные религии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '52-3':
        SUBCATEGORY = '[Аудио] Нетрадиционные религиозно-философские учения'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '53-0':
        SUBCATEGORY = '[Аудио] Книги по медицине'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '53-1':
        SUBCATEGORY = '[Аудио] Учебная и научно-популярная литература'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '53-2':
        SUBCATEGORY = '[Аудио] lossless-аудиокниги'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '53-3':
        SUBCATEGORY = '[Аудио] Бизнес'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '53-4':
        SUBCATEGORY = '[Аудио] Разное'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '53-5':
        SUBCATEGORY = '[Аудио] Некондиционные раздачи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-0':
        SUBCATEGORY = 'Оригинальные каталоги по подбору запчастей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-1':
        SUBCATEGORY = 'Неоригинальные каталоги по подбору запчастей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-2':
        SUBCATEGORY = 'Программы по диагностике и ремонту'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-3':
        SUBCATEGORY = 'Тюнинг, чиптюнинг, настройка'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-4':
        SUBCATEGORY = 'Книги по ремонту/обслуживанию/эксплуатации ТС'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-5':
        SUBCATEGORY = 'Мультимедийки по ремонту/обслуживанию/эксплуатации ТС'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-6':
        SUBCATEGORY = 'Учет, утилиты и прочее'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-7':
        SUBCATEGORY = 'Виртуальная автошкола'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-8':
        SUBCATEGORY = 'Видеоуроки по вождению транспортных средств'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-9':
        SUBCATEGORY = 'Видеоуроки по ремонту транспортных средств'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-10':
        SUBCATEGORY = 'Журналы по авто/мото'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '54-11':
        SUBCATEGORY = 'Водный транспорт'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '55-0':
        SUBCATEGORY = 'Документальные/познавательные фильмы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '55-1':
        SUBCATEGORY = 'Развлекательные передачи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '55-2':
        SUBCATEGORY = 'Top Gear/Топ Гир'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '55-3':
        SUBCATEGORY = 'Тест драйв/Обзоры/Автосалоны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '55-4':
        SUBCATEGORY = 'Тюнинг/форсаж'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-0':
        SUBCATEGORY = 'Классическая музыка (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-1':
        SUBCATEGORY = 'Классическая музыка (DVD и HD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-2':
        SUBCATEGORY = 'Опера (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-3':
        SUBCATEGORY = 'Опера (DVD и HD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-4':
        SUBCATEGORY = 'Балет и современная хореография (Видео, DVD и HD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-5':
        SUBCATEGORY = 'Полные собрания сочинений и многодисковые издания (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-6':
        SUBCATEGORY = 'Опера (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-7':
        SUBCATEGORY = 'Вокальная музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-8':
        SUBCATEGORY = 'Хоровая музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-9':
        SUBCATEGORY = 'Оркестровая музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-10':
        SUBCATEGORY = 'Концерт для инструмента с оркестром (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-11':
        SUBCATEGORY = 'Камерная инструментальная музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-12':
        SUBCATEGORY = 'Сольная инструментальная музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-13':
        SUBCATEGORY = 'Духовные песнопения и музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-14':
        SUBCATEGORY = 'Духовные песнопения и музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-15':
        SUBCATEGORY = 'Полные собрания сочинений и многодисковые издания (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-16':
        SUBCATEGORY = 'Вокальная и хоровая музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-17':
        SUBCATEGORY = 'Оркестровая музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-18':
        SUBCATEGORY = 'Камерная и сольная инструментальная музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '56-19':
        SUBCATEGORY = 'Классика в современной обработке, Classical Crossover (lossy и los..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-0':
        SUBCATEGORY = 'Восточноевропейский фолк (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-1':
        SUBCATEGORY = 'Восточноевропейский фолк (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-2':
        SUBCATEGORY = 'Западноевропейский фолк (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-3':
        SUBCATEGORY = 'Западноевропейский фолк (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-4':
        SUBCATEGORY = 'Klezmer и Еврейский фольклор (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-5':
        SUBCATEGORY = 'Этническая музыка Сибири, Средней и Восточной Азии (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-6':
        SUBCATEGORY = 'Этническая музыка Сибири, Средней и Восточной Азии (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-7':
        SUBCATEGORY = 'Этническая музыка Индии (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-8':
        SUBCATEGORY = 'Этническая музыка Индии (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-9':
        SUBCATEGORY = 'Этническая музыка Африки и Ближнего Востока (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-10':
        SUBCATEGORY = 'Этническая музыка Африки и Ближнего Востока (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-11':
        SUBCATEGORY = 'Фольклорная, Народная, Эстрадная музыка Кавказа и Закавказья (loss..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-12':
        SUBCATEGORY = 'Этническая музыка Северной и Южной Америки (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-13':
        SUBCATEGORY = 'Этническая музыка Северной и Южной Америки (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-14':
        SUBCATEGORY = 'Этническая музыка Австралии, Тихого и Индийского океанов (lossy и ..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-15':
        SUBCATEGORY = 'Country, Bluegrass (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-16':
        SUBCATEGORY = 'Country, Bluegrass (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-17':
        SUBCATEGORY = 'Фольклор, Народная и Этническая музыка (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-18':
        SUBCATEGORY = 'Фольклор, Народная и Этническая музыка (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '57-19':
        SUBCATEGORY = 'Фольклор, Народная и Этническая музыка (HD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-0':
        SUBCATEGORY = 'New Age & Meditative (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-1':
        SUBCATEGORY = 'New Age & Meditative (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-2':
        SUBCATEGORY = 'Фламенко и акустическая гитара (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-3':
        SUBCATEGORY = 'Фламенко и акустическая гитара (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-4':
        SUBCATEGORY = 'Музыка для бальных танцев (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-5':
        SUBCATEGORY = 'New Age, Relax, Meditative & Flamenco (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-6':
        SUBCATEGORY = 'New Age, Relax, Meditative & Flamenco (DVD и HD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '58-7':
        SUBCATEGORY = 'Звуки природы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-0':
        SUBCATEGORY = 'Отечественный Рэп, Хип-Хоп (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-1':
        SUBCATEGORY = 'Отечественный R\'n\'B (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-2':
        SUBCATEGORY = 'Отечественный Рэп, Хип-Хоп, R\'n\'B (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-3':
        SUBCATEGORY = 'Зарубежный R\'n\'B (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-4':
        SUBCATEGORY = 'Зарубежный Рэп, Хип-Хоп (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-5':
        SUBCATEGORY = 'Зарубежный Рэп, Хип-Хоп (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-6':
        SUBCATEGORY = 'Зарубежный R\'n\'B (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-7':
        SUBCATEGORY = 'Отечественный Рэп, Хип-Хоп (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-8':
        SUBCATEGORY = 'Отечественный R\'n\'B (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-9':
        SUBCATEGORY = 'Зарубежный Рэп, Хип-Хоп (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-10':
        SUBCATEGORY = 'Зарубежный R\'n\'B (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-11':
        SUBCATEGORY = 'Рэп, Хип-Хоп, R\'n\'B (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '59-12':
        SUBCATEGORY = 'Рэп, Хип-Хоп, R\'n\'B (HD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-0':
        SUBCATEGORY = 'Rocksteady, Early Reggae, Ska-Jazz, Trad.Ska (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-1':
        SUBCATEGORY = 'Punky-Reggae, Rocksteady-Punk, Ska Revival (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-2':
        SUBCATEGORY = '3rd Wave Ska (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-3':
        SUBCATEGORY = 'Ska-Punk, Ska-Core (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-4':
        SUBCATEGORY = 'Reggae (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-5':
        SUBCATEGORY = 'Dub (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-6':
        SUBCATEGORY = 'Dancehall, Raggamuffin (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-7':
        SUBCATEGORY = 'Reggae, Dancehall, Dub (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-8':
        SUBCATEGORY = 'Ska, Ska-Punk, Ska-Jazz (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-9':
        SUBCATEGORY = 'Отечественный Reggae, Dub (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-10':
        SUBCATEGORY = 'Отечественная Ska музыка (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-11':
        SUBCATEGORY = 'Reggae, Ska, Dub (компиляции) (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-12':
        SUBCATEGORY = 'Reggae, Ska, Dub (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '60-13':
        SUBCATEGORY = 'Reggae, Ska, Dub (DVD и HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-0':
        SUBCATEGORY = 'Караоке (аудио)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-1':
        SUBCATEGORY = 'Караоке (видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-2':
        SUBCATEGORY = 'Минусовки (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-3':
        SUBCATEGORY = 'Саундтреки к отечественным фильмам (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-4':
        SUBCATEGORY = 'Саундтреки к отечественным фильмам (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-5':
        SUBCATEGORY = 'Саундтреки к зарубежным фильмам (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-6':
        SUBCATEGORY = 'Саундтреки к зарубежным фильмам (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-7':
        SUBCATEGORY = 'Саундтреки к сериалам (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-8':
        SUBCATEGORY = 'Саундтреки к сериалам (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-9':
        SUBCATEGORY = 'Саундтреки к мультфильмам (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-10':
        SUBCATEGORY = 'Саундтреки к аниме (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-11':
        SUBCATEGORY = 'Саундтреки к аниме (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-12':
        SUBCATEGORY = 'Неофициальные саундтреки к фильмам и сериалам (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-13':
        SUBCATEGORY = 'Саундтреки к играм (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-14':
        SUBCATEGORY = 'Саундтреки к играм (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-15':
        SUBCATEGORY = 'Неофициальные саундтреки к играм (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-16':
        SUBCATEGORY = 'Аранжировки музыки из игр (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-17':
        SUBCATEGORY = 'Мюзикл (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '61-18':
        SUBCATEGORY = 'Мюзикл (Видео и DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-0':
        SUBCATEGORY = 'Отечественный шансон (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-1':
        SUBCATEGORY = 'Отечественный шансон (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-2':
        SUBCATEGORY = 'Сборники отечественного шансона (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-3':
        SUBCATEGORY = 'Военная песня, марши (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-4':
        SUBCATEGORY = 'Военная песня, марши (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-5':
        SUBCATEGORY = 'Авторская песня (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-6':
        SUBCATEGORY = 'Авторская песня (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-7':
        SUBCATEGORY = 'Менестрели и ролевики (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-8':
        SUBCATEGORY = 'Видео (Шансон, Авторская и Военная песня)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '62-9':
        SUBCATEGORY = 'DVD Видео (Шансон, Авторская и Военная песня)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '63-0':
        SUBCATEGORY = 'Видео (Музыка других жанров)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '63-1':
        SUBCATEGORY = 'DVD Video (Музыка других жанров)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '64-0':
        SUBCATEGORY = 'Отечественная поп-музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '64-1':
        SUBCATEGORY = 'Отечественная поп-музыка (сборники) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '64-2':
        SUBCATEGORY = 'Отечественная поп-музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '64-3':
        SUBCATEGORY = 'Советская эстрада, ретро, романсы (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '64-4':
        SUBCATEGORY = 'Советская эстрада, ретро, романсы (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-0':
        SUBCATEGORY = 'Зарубежная поп-музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-1':
        SUBCATEGORY = 'Зарубежная поп-музыка (сборники) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-2':
        SUBCATEGORY = 'Зарубежная поп-музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-3':
        SUBCATEGORY = 'Итальянская поп-музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-4':
        SUBCATEGORY = 'Итальянская поп-музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-5':
        SUBCATEGORY = 'Латиноамериканская поп-музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-6':
        SUBCATEGORY = 'Латиноамериканская поп-музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-7':
        SUBCATEGORY = 'Восточноазиатская поп-музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-8':
        SUBCATEGORY = 'Восточноазиатская поп-музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-9':
        SUBCATEGORY = 'Зарубежный шансон (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-10':
        SUBCATEGORY = 'Зарубежный шансон (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-11':
        SUBCATEGORY = 'Easy Listening, Instrumental Pop (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-12':
        SUBCATEGORY = 'Easy Listening, Instrumental Pop (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '65-13':
        SUBCATEGORY = 'Сборники песен для детей (lossy и lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '66-0':
        SUBCATEGORY = 'Eurodance, Euro-House, Technopop (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '66-1':
        SUBCATEGORY = 'Eurodance, Euro-House, Technopop (сборники) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '66-2':
        SUBCATEGORY = 'Eurodance, Euro-House, Technopop (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '66-3':
        SUBCATEGORY = 'Disco, Italo-Disco, Euro-Disco, Hi-NRG (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '66-4':
        SUBCATEGORY = 'Disco, Italo-Disco, Euro-Disco, Hi-NRG (сборники) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '66-5':
        SUBCATEGORY = 'Disco, Italo-Disco, Euro-Disco, Hi-NRG (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-0':
        SUBCATEGORY = 'Отечественная поп-музыка (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-1':
        SUBCATEGORY = 'Отечественная поп-музыка (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-2':
        SUBCATEGORY = 'Советская эстрада, ретро, романсы (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-3':
        SUBCATEGORY = 'Советская эстрада, ретро, романсы (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-4':
        SUBCATEGORY = 'Зарубежная поп-музыка (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-5':
        SUBCATEGORY = 'Зарубежная поп-музыка (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-6':
        SUBCATEGORY = 'Eurodance, Disco (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-7':
        SUBCATEGORY = 'Eurodance, Disco (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-8':
        SUBCATEGORY = 'Восточноазиатская поп-музыка (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-9':
        SUBCATEGORY = 'Восточноазиатская поп-музыка (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-10':
        SUBCATEGORY = 'Зарубежный шансон (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-11':
        SUBCATEGORY = 'Зарубежный шансон (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-12':
        SUBCATEGORY = 'Отечественная поп-музыка (Сборные концерты, док. видео) (Видео и D..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-13':
        SUBCATEGORY = 'Зарубежная поп-музыка (Сборные концерты, док. видео) (Видео и DVD)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-14':
        SUBCATEGORY = 'Отечественная Поп-музыка, Шансон, Eurodance, Disco (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '67-15':
        SUBCATEGORY = 'Зарубежная Поп-музыка, Шансон, Eurodance, Disco (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-0':
        SUBCATEGORY = 'Early Jazz, Swing, Gypsy (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-1':
        SUBCATEGORY = 'Bop (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-2':
        SUBCATEGORY = 'Mainstream Jazz, Cool (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-3':
        SUBCATEGORY = 'Jazz Fusion (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-4':
        SUBCATEGORY = 'World Fusion, Ethnic Jazz (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-5':
        SUBCATEGORY = 'Avant-Garde Jazz, Free Improvisation (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-6':
        SUBCATEGORY = 'Modern Creative, Third Stream (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-7':
        SUBCATEGORY = 'Smooth, Jazz-Pop (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-8':
        SUBCATEGORY = 'Vocal Jazz (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-9':
        SUBCATEGORY = 'Funk, Soul, R&B (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-10':
        SUBCATEGORY = 'Сборники зарубежного джаза (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '68-11':
        SUBCATEGORY = 'Зарубежный джаз (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '69-0':
        SUBCATEGORY = 'Blues (Texas, Chicago, Modern and Others) (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '69-1':
        SUBCATEGORY = 'Blues-rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '69-2':
        SUBCATEGORY = 'Roots, Pre-War Blues, Early R&B, Gospel (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '69-3':
        SUBCATEGORY = 'Зарубежный блюз (сборники; Tribute VA) (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '69-4':
        SUBCATEGORY = 'Зарубежный блюз (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '70-0':
        SUBCATEGORY = 'Отечественный джаз (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '70-1':
        SUBCATEGORY = 'Отечественный джаз (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '70-2':
        SUBCATEGORY = 'Отечественный блюз (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '70-3':
        SUBCATEGORY = 'Отечественный блюз (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '71-0':
        SUBCATEGORY = 'Джаз и Блюз (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '71-1':
        SUBCATEGORY = 'Джаз и Блюз (DVD Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '71-2':
        SUBCATEGORY = 'Джаз и Блюз (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-0':
        SUBCATEGORY = 'Classic Rock & Hard Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-1':
        SUBCATEGORY = 'Classic Rock & Hard Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-2':
        SUBCATEGORY = 'Progressive & Art-Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-3':
        SUBCATEGORY = 'Progressive & Art-Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-4':
        SUBCATEGORY = 'Folk-Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-5':
        SUBCATEGORY = 'Folk-Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-6':
        SUBCATEGORY = 'AOR (Melodic Hard Rock, Arena rock) (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-7':
        SUBCATEGORY = 'AOR (Melodic Hard Rock, Arena rock) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-8':
        SUBCATEGORY = 'Pop-Rock & Soft Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-9':
        SUBCATEGORY = 'Pop-Rock & Soft Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-10':
        SUBCATEGORY = 'Instrumental Guitar Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-11':
        SUBCATEGORY = 'Instrumental Guitar Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-12':
        SUBCATEGORY = 'Rockabilly, Psychobilly, Rock\'n\'Roll (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-13':
        SUBCATEGORY = 'Rockabilly, Psychobilly, Rock\'n\'Roll (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-14':
        SUBCATEGORY = 'Сборники зарубежного рока (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-15':
        SUBCATEGORY = 'Сборники зарубежного рока (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-16':
        SUBCATEGORY = 'Восточноазиатский рок (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '72-17':
        SUBCATEGORY = 'Восточноазиатский рок (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-0':
        SUBCATEGORY = 'Avant-garde, Experimental Metal (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-1':
        SUBCATEGORY = 'Avant-garde, Experimental Metal (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-2':
        SUBCATEGORY = 'Black (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-3':
        SUBCATEGORY = 'Black (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-4':
        SUBCATEGORY = 'Death, Doom (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-5':
        SUBCATEGORY = 'Death, Doom (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-6':
        SUBCATEGORY = 'Folk, Pagan, Viking (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-7':
        SUBCATEGORY = 'Folk, Pagan, Viking (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-8':
        SUBCATEGORY = 'Gothic Metal (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-9':
        SUBCATEGORY = 'Gothic Metal (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-10':
        SUBCATEGORY = 'Grind, Brutal Death (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-11':
        SUBCATEGORY = 'Grind, Brutal Death (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-12':
        SUBCATEGORY = 'Heavy, Power, Progressive (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-13':
        SUBCATEGORY = 'Heavy, Power, Progressive (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-14':
        SUBCATEGORY = 'Sludge, Stoner, Post-Metal (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-15':
        SUBCATEGORY = 'Sludge, Stoner, Post-Metal (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-16':
        SUBCATEGORY = 'Thrash, Speed (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-17':
        SUBCATEGORY = 'Thrash, Speed (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-18':
        SUBCATEGORY = 'Сборники (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '73-19':
        SUBCATEGORY = 'Сборники (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-0':
        SUBCATEGORY = 'Alternative & Nu-metal (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-1':
        SUBCATEGORY = 'Alternative & Nu-metal (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-2':
        SUBCATEGORY = 'Punk (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-3':
        SUBCATEGORY = 'Punk (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-4':
        SUBCATEGORY = 'Hardcore (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-5':
        SUBCATEGORY = 'Hardcore (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-6':
        SUBCATEGORY = 'Indie, Post-Rock & Post-Punk (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-7':
        SUBCATEGORY = 'Indie, Post-Rock & Post-Punk (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-8':
        SUBCATEGORY = 'Industrial & Post-industrial (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-9':
        SUBCATEGORY = 'Industrial & Post-industrial (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-10':
        SUBCATEGORY = 'Emocore, Post-hardcore, Metalcore (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-11':
        SUBCATEGORY = 'Emocore, Post-hardcore, Metalcore (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-12':
        SUBCATEGORY = 'Gothic Rock & Dark Folk (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-13':
        SUBCATEGORY = 'Gothic Rock & Dark Folk (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-14':
        SUBCATEGORY = 'Avant-garde, Experimental Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '74-15':
        SUBCATEGORY = 'Avant-garde, Experimental Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-0':
        SUBCATEGORY = 'Rock (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-1':
        SUBCATEGORY = 'Rock (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-2':
        SUBCATEGORY = 'Alternative, Punk, Independent (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-3':
        SUBCATEGORY = 'Alternative, Punk, Independent (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-4':
        SUBCATEGORY = 'Metal (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-5':
        SUBCATEGORY = 'Metal (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-6':
        SUBCATEGORY = 'Rock на языках народов xUSSR (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '75-7':
        SUBCATEGORY = 'Rock на языках народов xUSSR (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-0':
        SUBCATEGORY = 'Rock (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-1':
        SUBCATEGORY = 'Rock (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-2':
        SUBCATEGORY = 'Rock (Неофициальные DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-3':
        SUBCATEGORY = 'Metal (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-4':
        SUBCATEGORY = 'Metal (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-5':
        SUBCATEGORY = 'Metal (Неофициальные DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-6':
        SUBCATEGORY = 'Alternative, Punk, Independent (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-7':
        SUBCATEGORY = 'Alternative, Punk, Independent (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-8':
        SUBCATEGORY = 'Alternative, Punk, Independent (Неофициальные DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-9':
        SUBCATEGORY = 'Отечественный Рок, Панк, Альтернатива (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-10':
        SUBCATEGORY = 'Отечественный Рок, Панк, Альтернатива (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-11':
        SUBCATEGORY = 'Отечественный Металл (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-12':
        SUBCATEGORY = 'Отечественный Металл (DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-13':
        SUBCATEGORY = 'Отечественный Рок, Панк, Альтернатива, Металл (Неофициальные DVD V..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '76-14':
        SUBCATEGORY = 'Рок-музыка (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-0':
        SUBCATEGORY = 'Goa Trance, Psy-Trance (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-1':
        SUBCATEGORY = 'Goa Trance, Psy-Trance (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-2':
        SUBCATEGORY = 'PsyChill, Ambient, Dub (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-3':
        SUBCATEGORY = 'PsyChill, Ambient, Dub (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-4':
        SUBCATEGORY = 'Goa Trance, Psy-Trance, PsyChill, Ambient, Dub (Live Sets, Mixes) ..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-5':
        SUBCATEGORY = 'Trance (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-6':
        SUBCATEGORY = 'Trance (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-7':
        SUBCATEGORY = 'Trance (Singles, EPs) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '77-8':
        SUBCATEGORY = 'Trance (Radioshows, Podcasts, Live Sets, Mixes) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-0':
        SUBCATEGORY = 'Hardcore, Hardstyle, Jumpstyle (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-1':
        SUBCATEGORY = 'Hardcore, Hardstyle, Jumpstyle (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-2':
        SUBCATEGORY = 'Hardcore, Hardstyle, Jumpstyle (vinyl, web)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-3':
        SUBCATEGORY = 'House (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-4':
        SUBCATEGORY = 'House (Radioshow, Podcast, Liveset, Mixes)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-5':
        SUBCATEGORY = 'House (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-6':
        SUBCATEGORY = 'House (Проморелизы, сборники) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-7':
        SUBCATEGORY = 'House (Singles, EPs) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-8':
        SUBCATEGORY = 'Techno (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-9':
        SUBCATEGORY = 'Techno (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-10':
        SUBCATEGORY = 'Techno (Radioshows, Podcasts, Livesets, Mixes)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '78-11':
        SUBCATEGORY = 'Techno (Singles, EPs) (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-0':
        SUBCATEGORY = 'Electro, Electro-Freestyle, Nu Electro (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-1':
        SUBCATEGORY = 'Electro, Electro-Freestyle, Nu Electro (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-2':
        SUBCATEGORY = 'Drum & Bass, Jungle (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-3':
        SUBCATEGORY = 'Drum & Bass, Jungle (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-4':
        SUBCATEGORY = 'Drum & Bass, Jungle (Radioshows, Podcasts, Livesets, Mixes)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-5':
        SUBCATEGORY = 'Breakbeat (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-6':
        SUBCATEGORY = 'Breakbeat (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-7':
        SUBCATEGORY = 'Dubstep (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-8':
        SUBCATEGORY = 'Dubstep (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-9':
        SUBCATEGORY = 'Breakbeat, Dubstep (Radioshows, Podcasts, Livesets, Mixes)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-10':
        SUBCATEGORY = 'IDM (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-11':
        SUBCATEGORY = 'IDM (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '79-12':
        SUBCATEGORY = 'IDM Discography & Collections (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '80-0':
        SUBCATEGORY = 'Chillout, Lounge, Downtempo (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '80-1':
        SUBCATEGORY = 'Chillout, Lounge, Downtempo (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '80-2':
        SUBCATEGORY = 'Nu Jazz, Acid Jazz, Future Jazz (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '80-3':
        SUBCATEGORY = 'Nu Jazz, Acid Jazz, Future Jazz (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '80-4':
        SUBCATEGORY = 'Trip Hop, Abstract Hip-Hop (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '80-5':
        SUBCATEGORY = 'Trip Hop, Abstract Hip-Hop (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-0':
        SUBCATEGORY = 'Traditional Electronic, Ambient (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-1':
        SUBCATEGORY = 'Traditional Electronic, Ambient (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-2':
        SUBCATEGORY = 'Modern Classical, Electroacoustic (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-3':
        SUBCATEGORY = 'Modern Classical, Electroacoustic (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-4':
        SUBCATEGORY = 'Experimental (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-5':
        SUBCATEGORY = 'Experimental (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '81-6':
        SUBCATEGORY = '8-bit, Chiptune (lossy & lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-0':
        SUBCATEGORY = 'EBM, Dark Electro, Aggrotech (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-1':
        SUBCATEGORY = 'EBM, Dark Electro, Aggrotech (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-2':
        SUBCATEGORY = 'Industrial, Noise (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-3':
        SUBCATEGORY = 'Industrial, Noise (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-4':
        SUBCATEGORY = 'Synthpop, Futurepop, New Wave, Electropop (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-5':
        SUBCATEGORY = 'Synthpop, Futurepop, New Wave, Electropop (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-6':
        SUBCATEGORY = 'Synthwave, Spacesynth, Dreamwave, Retrowave, Outrun (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-7':
        SUBCATEGORY = 'Synthwave, Spacesynth, Dreamwave, Retrowave, Outrun (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-8':
        SUBCATEGORY = 'Darkwave, Neoclassical, Ethereal, Dungeon Synth (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '82-9':
        SUBCATEGORY = 'Darkwave, Neoclassical, Ethereal, Dungeon Synth (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '85-0':
        SUBCATEGORY = 'Электронная музыка (Официальные DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '85-1':
        SUBCATEGORY = 'Электронная музыка (Неофициальные, любительские DVD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '85-2':
        SUBCATEGORY = 'Электронная музыка (Видео)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '85-3':
        SUBCATEGORY = 'Электронная музыка (HD Video)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-0':
        SUBCATEGORY = 'Классика и классика в современной обработке (Hi-Res stereo)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-1':
        SUBCATEGORY = 'Классика и классика в современной обработке (многоканальная музыка..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-2':
        SUBCATEGORY = 'New Age, Relax, Meditative & Flamenco (Hi-Res stereo и многоканаль..'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-3':
        SUBCATEGORY = 'Саундтреки (Hi-Res stereo и многоканальная музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-4':
        SUBCATEGORY = 'Музыка разных жанров (Hi-Res stereo и многоканальная музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-5':
        SUBCATEGORY = 'Поп-музыка (Hi-Res stereo)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-6':
        SUBCATEGORY = 'Поп-музыка (многоканальная музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-7':
        SUBCATEGORY = 'Джаз и Блюз (Hi-Res stereo)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-8':
        SUBCATEGORY = 'Джаз и Блюз (многоканальная музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-9':
        SUBCATEGORY = 'Рок-музыка (Hi-Res stereo)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-10':
        SUBCATEGORY = 'Рок-музыка (многоканальная музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-11':
        SUBCATEGORY = 'Электронная музыка (Hi-Res stereo)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '86-12':
        SUBCATEGORY = 'Электронная музыка (многоканальная музыка)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-0':
        SUBCATEGORY = 'Классика и классика в современной обработке (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-1':
        SUBCATEGORY = 'Фольклор, народная и этническая музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-2':
        SUBCATEGORY = 'Rap, Hip-Hop, R\'n\'B, Reggae, Ska, Dub (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-3':
        SUBCATEGORY = 'Саундтреки и мюзиклы (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-4':
        SUBCATEGORY = 'Шансон, авторские, военные песни и марши (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-5':
        SUBCATEGORY = 'Музыка других жанров (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-6':
        SUBCATEGORY = 'Зарубежная поп-музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-7':
        SUBCATEGORY = 'Советская эстрада, ретро, романсы (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-8':
        SUBCATEGORY = 'Отечественная поп-музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-9':
        SUBCATEGORY = 'Инструментальная поп-музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-10':
        SUBCATEGORY = 'Джаз и блюз (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-11':
        SUBCATEGORY = 'Зарубежная рок-музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-12':
        SUBCATEGORY = 'Отечественная рок-музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '87-13':
        SUBCATEGORY = 'Электронная музыка (оцифровки)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '88-0':
        SUBCATEGORY = 'Конверсии Quadraphonic'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '88-1':
        SUBCATEGORY = 'Конверсии SACD'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '88-2':
        SUBCATEGORY = 'Конверсии Blu-Ray, ADVD и DVD-Audio'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '88-3':
        SUBCATEGORY = 'Апмиксы-Upmixes/Даунмиксы-Downmix'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-0':
        SUBCATEGORY = 'Горячие Новинки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-1':
        SUBCATEGORY = 'Экшены от первого лица'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-2':
        SUBCATEGORY = 'Экшены от третьего лица'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-3':
        SUBCATEGORY = 'Хорроры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-4':
        SUBCATEGORY = 'Аркады'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-5':
        SUBCATEGORY = 'Файтинги'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-6':
        SUBCATEGORY = 'Приключения и квесты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-7':
        SUBCATEGORY = 'Квесты в стиле "Поиск предметов"'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-8':
        SUBCATEGORY = 'Визуальные новеллы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-9':
        SUBCATEGORY = 'Для самых маленьких'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-10':
        SUBCATEGORY = 'Логические игры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-11':
        SUBCATEGORY = 'Многопользовательские игры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-12':
        SUBCATEGORY = 'Ролевые игры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-13':
        SUBCATEGORY = 'Симуляторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-14':
        SUBCATEGORY = 'Стратегии в реальном времени'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-15':
        SUBCATEGORY = 'Пошаговые стратегии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-16':
        SUBCATEGORY = 'Шахматы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '89-17':
        SUBCATEGORY = 'IBM PC-несовместимые'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '90-0':
        SUBCATEGORY = 'Официальные патчи, моды, плагины, дополнения'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '90-1':
        SUBCATEGORY = 'Неофициальные моды, плагины, дополнения'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '90-2':
        SUBCATEGORY = 'Русификаторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '91-0':
        SUBCATEGORY = 'Сценарии, меши и аэропорты для FS2004, FSX, P3D'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '91-1':
        SUBCATEGORY = 'Самолёты и вертолёты для FS2004, FSX, P3D'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '91-2':
        SUBCATEGORY = 'Миссии, трафик, звуки, паки и утилиты для FS2004, FSX, P3D'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '91-3':
        SUBCATEGORY = 'Сценарии, миссии, трафик, звуки, паки и утилиты для X-Plane'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '91-4':
        SUBCATEGORY = 'Самолёты и вертолёты для X-Plane'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '92-0':
        SUBCATEGORY = 'Нативные игры для Mac'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '92-1':
        SUBCATEGORY = 'Портированные игры для Mac'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '93-0':
        SUBCATEGORY = 'Нативные игры для Linux'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '93-1':
        SUBCATEGORY = 'Портированные игры для Linux'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-0':
        SUBCATEGORY = 'PS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-1':
        SUBCATEGORY = 'PS2'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-2':
        SUBCATEGORY = 'PS3'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-3':
        SUBCATEGORY = 'Игры PS1, PS2 и PSP для PS3'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-4':
        SUBCATEGORY = 'PS4'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-5':
        SUBCATEGORY = 'PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-6':
        SUBCATEGORY = 'Игры PS1 для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-7':
        SUBCATEGORY = 'PS Vita'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-8':
        SUBCATEGORY = 'Original Xbox'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-9':
        SUBCATEGORY = 'Xbox 360'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-10':
        SUBCATEGORY = 'Wii/WiiU'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-11':
        SUBCATEGORY = 'NDS/3DS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-12':
        SUBCATEGORY = 'Switch'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-13':
        SUBCATEGORY = 'Dreamcast'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '94-14':
        SUBCATEGORY = 'Остальные платформы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-0':
        SUBCATEGORY = 'Видео для PS Vita'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-1':
        SUBCATEGORY = 'Фильмы для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-2':
        SUBCATEGORY = 'Сериалы для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-3':
        SUBCATEGORY = 'Мультфильмы для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-4':
        SUBCATEGORY = 'Дорамы для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-5':
        SUBCATEGORY = 'Аниме для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-6':
        SUBCATEGORY = 'Видео для PSP'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '95-7':
        SUBCATEGORY = 'Видео для PS3 и других консолей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '96-0':
        SUBCATEGORY = 'Игры для Android'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '96-1':
        SUBCATEGORY = 'Игры для Java'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '96-2':
        SUBCATEGORY = 'Игры для Symbian'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '96-3':
        SUBCATEGORY = 'Игры для Windows Mobile'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '96-4':
        SUBCATEGORY = 'Игры для Windows Phone'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '97-0':
        SUBCATEGORY = 'Видеопрохождения игр'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '98-0':
        SUBCATEGORY = 'Настольные ОС от Microsoft - Windows 8 и далее'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '98-1':
        SUBCATEGORY = 'Настольные ОС от Microsoft (выпущенные до Windows XP)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '98-2':
        SUBCATEGORY = 'Настольные ОС от Microsoft - Windows XP - Windows 7'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '98-3':
        SUBCATEGORY = 'Серверные ОС от Microsoft'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '98-4':
        SUBCATEGORY = 'Разное (Операционные системы от Microsoft)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '99-0':
        SUBCATEGORY = 'Операционные системы (Linux, Unix)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '99-1':
        SUBCATEGORY = 'Программное обеспечение (Linux, Unix)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '99-2':
        SUBCATEGORY = 'Другие ОС и ПО под них'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-0':
        SUBCATEGORY = 'Работа с жёстким диском'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-1':
        SUBCATEGORY = 'Резервное копирование'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-2':
        SUBCATEGORY = 'Архиваторы и файловые менеджеры'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-3':
        SUBCATEGORY = 'Программы для настройки и оптимизации ОС'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-4':
        SUBCATEGORY = 'Сервисное обслуживание компьютера'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-5':
        SUBCATEGORY = 'Работа с носителями информации'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-6':
        SUBCATEGORY = 'Информация и диагностика'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-7':
        SUBCATEGORY = 'Программы для интернет и сетей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-8':
        SUBCATEGORY = 'ПО для защиты компьютера (Антивирусное ПО, Фаерволлы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-9':
        SUBCATEGORY = 'Анти-шпионы и анти-трояны'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-10':
        SUBCATEGORY = 'Программы для защиты информации'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-11':
        SUBCATEGORY = 'Драйверы и прошивки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-12':
        SUBCATEGORY = 'Оригинальные диски к компьютерам и комплектующим'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-13':
        SUBCATEGORY = 'Серверное ПО для Windows'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-14':
        SUBCATEGORY = 'Изменение интерфейса ОС Windows'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-15':
        SUBCATEGORY = 'Скринсейверы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '101-16':
        SUBCATEGORY = 'Разное (Системные программы под Windows)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-0':
        SUBCATEGORY = 'Всё для дома: кройка, шитьё, кулинария'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-1':
        SUBCATEGORY = 'Офисные системы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-2':
        SUBCATEGORY = 'Системы для бизнеса'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-3':
        SUBCATEGORY = 'Распознавание текста, звука и синтез речи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-4':
        SUBCATEGORY = 'Работа с PDF и DjVu'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-5':
        SUBCATEGORY = 'Словари, переводчики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-6':
        SUBCATEGORY = 'Системы для научной работы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-7':
        SUBCATEGORY = 'САПР (общие и машиностроительные)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-8':
        SUBCATEGORY = 'САПР (электроника, автоматика, ГАП)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-9':
        SUBCATEGORY = 'Программы для архитекторов и строителей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-10':
        SUBCATEGORY = 'Библиотеки и проекты для архитекторов и дизайнеров интерьеров'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-11':
        SUBCATEGORY = 'Прочие справочные системы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '102-12':
        SUBCATEGORY = 'Разное (Системы для бизнеса, офиса, научной и проектной работы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-0':
        SUBCATEGORY = 'WYSIWYG Редакторы для веб-диза'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-1':
        SUBCATEGORY = 'Текстовые редакторы с подсветкой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-2':
        SUBCATEGORY = 'Среды программирования, компиляторы и вспомогательные программы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-3':
        SUBCATEGORY = 'Компоненты для сред программирования'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-4':
        SUBCATEGORY = 'Системы управления базами данных'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-5':
        SUBCATEGORY = 'Скрипты и движки сайтов, CMS а также расширения к ним'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-6':
        SUBCATEGORY = 'Шаблоны для сайтов и CMS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '103-7':
        SUBCATEGORY = 'Разное (Веб-разработка и программирование)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-0':
        SUBCATEGORY = 'Программные комплекты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-1':
        SUBCATEGORY = 'Плагины для программ компании Adobe'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-2':
        SUBCATEGORY = 'Графические редакторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-3':
        SUBCATEGORY = 'Программы для верстки, печати и работы со шрифтами'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-4':
        SUBCATEGORY = '3D моделирование, рендеринг и плагины для них'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-5':
        SUBCATEGORY = 'Анимация'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-6':
        SUBCATEGORY = 'Создание BD/HD/DVD-видео'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-7':
        SUBCATEGORY = 'Редакторы видео'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-8':
        SUBCATEGORY = 'Видео- Аудио- конверторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-9':
        SUBCATEGORY = 'Аудио- и видео-, CD- проигрыватели и каталогизаторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-10':
        SUBCATEGORY = 'Каталогизаторы и просмотрщики графики'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-11':
        SUBCATEGORY = 'Разное (Программы для работы с мультимедиа и 3D)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-12':
        SUBCATEGORY = 'Виртуальные студии, секвенсоры и аудиоредакторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-13':
        SUBCATEGORY = 'Виртуальные инструменты и синтезаторы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-14':
        SUBCATEGORY = 'Плагины для обработки звука'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '104-15':
        SUBCATEGORY = 'Разное (Программы для работы со звуком)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-0':
        SUBCATEGORY = 'Авторские работы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-1':
        SUBCATEGORY = 'Официальные сборники векторных клипартов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-2':
        SUBCATEGORY = 'Прочие векторные клипарты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-3':
        SUBCATEGORY = 'Photostoсks'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-4':
        SUBCATEGORY = 'Костюмы для фотомонтажа'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-5':
        SUBCATEGORY = 'Рамки и виньетки для оформления фотографий'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-6':
        SUBCATEGORY = 'Прочие растровые клипарты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-7':
        SUBCATEGORY = '3D модели, сцены и материалы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-8':
        SUBCATEGORY = 'Футажи'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-9':
        SUBCATEGORY = 'Прочие сборники футажей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-10':
        SUBCATEGORY = 'Музыкальные библиотеки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-11':
        SUBCATEGORY = 'Звуковые эффекты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-12':
        SUBCATEGORY = 'Библиотеки сэмплов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-13':
        SUBCATEGORY = 'Библиотеки и саундбанки для сэмплеров, пресеты для синтезаторов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-14':
        SUBCATEGORY = 'Multitracks'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-15':
        SUBCATEGORY = 'Материалы для создания меню и обложек DVD'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-16':
        SUBCATEGORY = 'Стили, кисти, формы и узоры для Adobe Photoshop'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-17':
        SUBCATEGORY = 'Шрифты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '105-18':
        SUBCATEGORY = 'Разное (Материалы для мультимедиа и дизайна)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-0':
        SUBCATEGORY = 'ГИС (Геоинформационные системы)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-1':
        SUBCATEGORY = 'Карты, снабженные программной оболочкой'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-2':
        SUBCATEGORY = 'Атласы и карты современные (после 1950 г.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-3':
        SUBCATEGORY = 'Атласы и карты старинные (до 1950 г.)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-4':
        SUBCATEGORY = 'Карты прочие (астрономические, исторические, тематические)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-5':
        SUBCATEGORY = 'Встроенная автомобильная навигация'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-6':
        SUBCATEGORY = 'Garmin'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-7':
        SUBCATEGORY = 'Ozi'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-8':
        SUBCATEGORY = 'TomTom'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-9':
        SUBCATEGORY = 'Navigon / Navitel'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-10':
        SUBCATEGORY = 'Igo'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '106-11':
        SUBCATEGORY = 'Разное - системы навигации и карты'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-0':
        SUBCATEGORY = 'Приложения для Android'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-1':
        SUBCATEGORY = 'Приложения для Java'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-2':
        SUBCATEGORY = 'Приложения для Symbian'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-3':
        SUBCATEGORY = 'Приложения для Windows Mobile'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-4':
        SUBCATEGORY = 'Приложения для Windows Phone'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-5':
        SUBCATEGORY = 'Софт для работы с телефоном'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-6':
        SUBCATEGORY = 'Прошивки для телефонов'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '107-7':
        SUBCATEGORY = 'Обои и темы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '108-0':
        SUBCATEGORY = 'Видео для смартфонов и КПК'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '108-1':
        SUBCATEGORY = 'Видео в формате 3GP для мобильных'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-0':
        SUBCATEGORY = 'Mac OS (для Macintosh)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-1':
        SUBCATEGORY = 'Mac OS (для РС-Хакинтош)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-2':
        SUBCATEGORY = 'Программы для просмотра и обработки видео (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-3':
        SUBCATEGORY = 'Программы для создания и обработки графики (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-4':
        SUBCATEGORY = 'Плагины для программ компании Adobe (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-5':
        SUBCATEGORY = 'Аудио редакторы и конвертеры (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-6':
        SUBCATEGORY = 'Системные программы (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-7':
        SUBCATEGORY = 'Офисные программы (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-8':
        SUBCATEGORY = 'Программы для интернета и сетей (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '109-9':
        SUBCATEGORY = 'Другие программы (Mac OS)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '110-0':
        SUBCATEGORY = 'Программы для iOS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '110-1':
        SUBCATEGORY = 'Игры для iOS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '110-2':
        SUBCATEGORY = 'Разное для iOS'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '111-0':
        SUBCATEGORY = 'Фильмы для iPod, iPhone, iPad'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '111-1':
        SUBCATEGORY = 'Сериалы для iPod, iPhone, iPad'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '111-2':
        SUBCATEGORY = 'Мультфильмы для iPod, iPhone, iPad'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '111-3':
        SUBCATEGORY = 'Аниме для iPod, iPhone, iPad'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '111-4':
        SUBCATEGORY = 'Музыкальное видео для iPod, iPhone, iPad'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '112-0':
        SUBCATEGORY = 'Фильмы HD для Apple TV'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '112-1':
        SUBCATEGORY = 'Сериалы HD для Apple TV'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '112-2':
        SUBCATEGORY = 'Мультфильмы HD для Apple TV'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '112-3':
        SUBCATEGORY = 'Документальное видео HD для Apple TV'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '112-4':
        SUBCATEGORY = 'Музыкальное видео HD для Apple TV'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '113-0':
        SUBCATEGORY = 'Аудиокниги (AAC, ALAC)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '113-1':
        SUBCATEGORY = 'Музыка Lossless (ALAC)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '113-2':
        SUBCATEGORY = 'Музыка Lossy (AAC-iTunes)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '113-3':
        SUBCATEGORY = 'Музыка Lossy (AAC)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '113-4':
        SUBCATEGORY = 'Музыка Lossy (AAC) (Singles, EPs)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-0':
        SUBCATEGORY = 'Психоактивные аудиопрограммы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-1':
        SUBCATEGORY = 'Аватары, Иконки, Смайлы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-2':
        SUBCATEGORY = 'Живопись, Графика, Скульптура, Digital Art'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-3':
        SUBCATEGORY = 'Картинки'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-4':
        SUBCATEGORY = 'Любительские фотографии'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-5':
        SUBCATEGORY = 'Обои'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-6':
        SUBCATEGORY = 'Фото знаменитостей'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-7':
        SUBCATEGORY = 'Аудио'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-8':
        SUBCATEGORY = 'Музыка (lossy)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-9':
        SUBCATEGORY = 'Музыка (lossless)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-10':
        SUBCATEGORY = 'Видео'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-11':
        SUBCATEGORY = 'Публикации и учебные материалы (тексты)'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-12':
        SUBCATEGORY = 'Трейлеры и дополнительные материалы к фильмам'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
        bot.register_next_step_handler(send, targetsearch(call))
    elif call.data == '114-13':
        SUBCATEGORY = 'Любительские видеоклипы'
        send = bot.send_message(call.from_user.id, 'Выбрана подкатегория: "{}"'.format(SUBCATEGORY))
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
            text = """У категории ({}) нет подкатегорий. Перенаправляю вас на адресный поиск."""
            send = bot.send_message(message.from_user.id, text.format(CATEGORY))
            bot.register_next_step_handler(send, targetsearch(message))

        keyboard = InlineKeyboardMarkup()

        keyboard.row_width = 1

        for sbct in subcategories:
            clean_sbct = sbct.replace("'", "\'")
            clbk = '{}-{}'.format(ctgs.index(CATEGORY), subcategories.index(sbct))
            keyboard.add(InlineKeyboardButton(clean_sbct, callback_data=clbk))
        keyboard.add(InlineKeyboardButton('Назад', callback_data='back'))
        bot.send_message(message.from_user.id, subcategory_choose_text, reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['globalsearch'])
def globalsearch(message):
    bot.send_message(message.from_user.id, 'Отправьте ваш запрос ответным сообщением')


@bot.message_handler(func=lambda message: True)
@bot.message_handler(commands=['targetsearch'])
def targetsearch(message):
    if (CATEGORY is None) and (SUBCATEGORY is None):
        bot.send_message(message.from_user.id, 'Сперва необходимо выбрать категорию')
    send = bot.send_message(message.from_user.id, 'Отправьте ваш запрос ответным сообщением')
    bot.register_next_step_handler(send, text_handler)


@bot.message_handler(content_types=['text'])
# @ bot.message_handler(func=lambda message: True)
def text_handler(message):
    global QUERY
    QUERY = message.text.lower()
    send = bot.send_message(message.from_user.id, 'Ваш запрос обрабатывается')
    bot.register_next_step_handler(send, search)



@bot.message_handler(func=lambda call: True)
# @bot.message_handler(content_types=['text'])
def search(message):
    db = 'rutracker.sqlite'
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    answer = ''
    while True:
        try:
            cursor.execute(
                "SELECT * FROM torrents WHERE Category=? AND Subcategory=?", (CATEGORY, SUBCATEGORY)
            )
            result = cursor.fetchall()
            for i in result:
                name = list(i)[2]
                link = list(i)[3]
                if QUERY in name.lower():
                    answer += name + '\n' + link + '\n\n'
                # return answer
            bot.send_message(message.from_user.id, answer)
            conn.commit()
        except sqlite3.DatabaseError as err:
            print("Error: ", err)
        finally:
            conn.close()


if __name__ == '__main__':
    # bot.polling(none_stop=True, interval=0, timeout=20)
    # bot.polling(none_stop=True)
    bot.infinity_polling()
