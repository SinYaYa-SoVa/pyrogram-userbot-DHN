import time
import os.path
from pyrogram import Client
from pyrogram.types import InputMediaPhoto
from scrapper import scrapper
from datetime import datetime

app = Client("my_account")


async def main(user, send_time):
    async with app:
        print('[{}] Ожидание отправки сообщения...'.format(datetime.now().time()))
        while True:
            now_time = datetime.now().time()
            time_ = str(now_time).split('.')
            time_ = time_[0]
            time_ = str(time_).split(':')
            time_.pop(2)
            time_ = ':'.join(time_)

            if send_time == time_:
                text, image = scrapper()
                text = 'Ура! Сегодня**{}**! Поздравляю тебя!'.format(text.lower())
                await app.send_media_group(user, [
                    InputMediaPhoto('picture.jpg', caption=text)
                ])
                print('[{}] Сообщение отправлено!'.format(now_time))
                print('[{}] Ожидание отправки сообщения...'.format(now_time))
                time.sleep(86390)


if __name__ == '__main__':
    if os.path.isfile('my_account.session'):
        input_data = input('Введи никнейм пользователя, его номер телефона или ID в следующих форматах: \n'
                           '@user_name\n79008007060\n0123456789\n')
        input_time = input('Введите время отправки поздравления в формате: 09:00\n')
        app.run(main(input_data, input_time))
    else:
        print('Нужно провести авторизацию!')
        api_id = int(input('Введите api ID: \n'))
        api_hash = input('Введите api HASH: \n')
        app = Client("my_account", api_id=api_id, api_hash=api_hash)
        app.run()
