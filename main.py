import time
import os.path
from pyrogram import Client
from pyrogram.types import InputMediaPhoto
from scrapper import scrapper
from datetime import datetime

version = 0.1

app = Client("my_account")


async def first_launch():
    async with app:
        print('Авторизация прошла успешно! Сейчас приложение закроется...')
        time.sleep(2)


async def main(user, send_time):
    async with app:
        print('[{}] Ожидание отправки сообщения...'.format(datetime.now().time()))
        print('Сообщение будет отправлено пользователю {} в {}'.format(user, send_time))
        while True:
            now_time = datetime.now().time()
            time_ = str(now_time).split('.')
            time_ = time_[0]
            time_ = str(time_).split(':')
            time_.pop(2)
            time_ = ':'.join(time_)
            time_1 = datetime.strptime(time_, "%H:%M")
            time_2 = datetime.strptime(send_time, "%H:%M")
            wait_time = time_2 - time_1
            wait_time = int(wait_time.total_seconds())
            print('До отправки сообщения ', (wait_time // 60) // 60, ' (часы) ', (wait_time // 60) % 60,
                  ' (минуты)')
            time.sleep(wait_time)
            text, image = scrapper()
            text = 'Ура! Сегодня**{}**! Поздравляю тебя!'.format(text.lower())
            await app.send_media_group(user, [
                InputMediaPhoto('picture.jpg', caption=text)
            ])
            print('[{}] Сообщение отправлено!'.format(now_time))
            print('[{}] Ожидание отправки сообщения...'.format(now_time))
            print('До отправки сообщения 24 часа')
            time.sleep(86400)



if __name__ == '__main__':
    def clear():
        print('\n' * 47)


    def get_data():
        with open('data.txt', 'r', encoding='utf-8') as f:
            lines = [i for i in f.readlines()]
        return lines


    def write_data(user_data, time_data):
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.write(user_data)
            f.write(time_data)
        print('Информация записана!')


    def in_user():
        users_user = input(
            'Введи никнейм пользователя, его номер телефона или ID в следующих форматах: \n'
            '@user_name\n79008007060\n0123456789\n')
        return users_user


    def in_time():
        users_time = input('Введите время отправки поздравления в формате: 09:00\n')
        return users_time


    print('*** Daily Holiday Notifier ***\nA pyrogram userbot\nVer.: ' + str(version))
    if os.path.isfile('my_account.session'):
        while True:
            print('Меню:',
                  '1. Запуск',
                  '2. Получатель',
                  '3. Время отправления',
                  '4. Выход из аккаунта',
                  '5. Помощь',
                  '6. О программе',
                  '0. Закрыть программу', sep='\n')
            menu = input('Введите цифру: ')
            match menu:
                case '0':
                    break
                case '1':
                    if os.path.isfile('data.txt'):
                        data_info = get_data()
                        user_info = data_info[0][:-1]
                        time_info = data_info[1]
                        if len(user_info) < 2 or ':' not in time_info:
                            clear()
                            print('Ошибка! Проверьте никнейм или время отправления!')
                        else:
                            clear()
                            print('Бот успешно запущен!')
                            app.run(main(user_info, time_info))
                    else:
                        input_user = in_user()
                        input_time = in_time()
                        write_data(input_user + '\n', input_time)
                        app.run(main(input_user, input_time))
                case '2':
                    if os.path.isfile('data.txt'):
                        clear()
                        data_info = get_data()
                        print('Получатель: ' + data_info[0])
                        while True:
                            menu_2 = input('Вы хотите изменить получателя?\n1. Да 2. Нет (Выход)\n')
                            match menu_2:
                                case '1':
                                    input_user = in_user()
                                    write_data(input_user + '\n', data_info[1])
                                    break
                                case '2':
                                    clear()
                                    break
                                case _:
                                    print('Введите корректное число!')
                    else:
                        clear()
                        print('Ошибка! Нет информации! Выбери пункт один (1) для первоначального выбора пользователя '
                              'и времени.')
                case '3':
                    if os.path.isfile('data.txt'):
                        clear()
                        data_info = get_data()
                        print('Время отправки сообщения: ' + data_info[1])
                        while True:
                            menu_3 = input('Вы хотите изменить время отправки?\n1. Да 2. Нет (Выход)\n')
                            match menu_3:
                                case '1':
                                    input_time = in_time()
                                    write_data(data_info[0], input_time)
                                    break
                                case '2':
                                    clear()
                                    break
                                case _:
                                    print('Введите корректное число!')
                    else:
                        clear()
                        print('Ошибка! Нет информации! Выбери пункт один (1) для первоначального выбора пользователя '
                              'и времени.')
                case '4':
                    clear()
                    print('Вы уверены, что хотите выйти из аккаунта?\n1. Да 2. Нет')
                    menu_4 = input()
                    match menu_4:
                        case '1':
                            os.remove('my_account.session')
                            print('Вы успешно вышли из аккаунта! Не забудьте удалить сессию бота из Telegram!')
                            break
                        case _:
                            clear()
                case '5':
                    clear()
                    print(
                        'Чтобы запустить бота и указать первоначальные данные о получателе и времени отправления '
                        'выбери пункт один (1).',
                        '\nЧтобы посмотреть/изменить получателя или время отправления выбери пункт меню под номером '
                        'два (2) или три (3) соответственно.',
                        '\nЧтобы заново произвести авторизацию выбери пункт меню под номером четыре (4).',
                        '\nВАЖНО! Чтобы полностью выйти из аккаунта нужно еще в самом Telegram удалить сессию бота!')
                case '6':
                    clear()
                    print('Made by SinYaYaSoVa\nJust4fun')
                case _:
                    clear()
                    print('Введите корректное число!')
    else:
        print('Нужно провести авторизацию!')
        api_id = int(input('Введите api ID: \n'))
        api_hash = input('Введите api HASH: \n')
        print('Далее нужно будет ввести номер СВОЕГО телефона в формате: +79998887766\n')
        time.sleep(1)
        app = Client("my_account", api_id=api_id, api_hash=api_hash)
        app.run(first_launch())