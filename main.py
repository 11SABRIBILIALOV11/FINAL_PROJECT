import sqlite3  # модуль для работы с базой sqlite
import telebot  # модуль для работы с API Telegram

token = '6172954060:AAEAI11T9FM08oeHx7dbga_U4tAoM6r08XQ'  # токен Телеграм бота

bot = telebot.TeleBot(token)  # bybwbbhetv ,jnf


@bot.message_handler(commands=['start'])  # хендлер бота с командой start
def start_message(message): # функция отправки ботом сообщения
    user_id = message.chat.id # объявляю переменную user_id, которая будет брать id пользователя телеграм для добавления в базу
    with sqlite3.connect('db.sqlite3') as conn: # подключаюсь к базе данных
        cursor = conn.cursor()  # создаю курсор соединения к базе
        cursor.execute('SELECT tgid FROM users WHERE tgid=?', (user_id,)) # запрос выборки id пользователя из базы
        result = cursor.fetchone()  # сохраняю в переменную результат выборки

        if result is None:  # если id пользователя не найден в базе, то ....
            bot.send_message(message.chat.id, "Тебя нет в базе, сейчас добавлю")  # ... отправляю ему соответствующее сообщение
            cursor = conn.cursor()  # создаю курсор соединения к базе
            cursor.execute("INSERT INTO users (tgid) VALUES (?)", (user_id,)) # добавляю в базу данных id пользователя
            conn.commit()  # записываю результат в базу данных (id пользователя)
        else: # иначе, если id уже существует, то ....
            bot.send_message(message.chat.id, "Привет, " + str(message.chat.first_name))  # пишу ему приветственное сообщение


if __name__ == '__main__':
    bot.polling(none_stop=True) # код, чтобы бот постоянно работал
