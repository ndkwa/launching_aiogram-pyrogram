import asyncio

import aiogram.bot
import aiogram.dispatcher
import aiogram.types
import aiogram.utils
import pyrogram

# Импорт параметров с config
from config import api_id, api_hash, api_number, token


# Aiogram бот, для настройки параметров Pyrogram (или для другого)
async def aiogram_bot():
    bot = aiogram.bot.Bot(token=token)
    dp = aiogram.dispatcher.Dispatcher(bot)

    @dp.message_handler(commands='start')
    async def cmd_start(message: aiogram.types.Message):
        await message.answer(text='Hi!')

    print('Aiogram bot started')
    await dp.start_polling()


# PYROGRAM, взяты 2 аккаунта, так как соединить хендлер и репит функцию невозможно.
# Проверка на входящие сообщения
async def pyrogram_bot_on_message():
    app = pyrogram.Client('my_account_on_message', api_id=api_id, api_hash=api_hash, phone_number=api_number)

    @app.on_message()  # filters=filrers.text ...
    async def handle(message):
        # ACTION
        # print(message)
        pass

    await app.start()
    print('PyroBot OnMessage запущен')


# Циклированное действие для pyrogram уже второй файл с аккаунтом
async def pyrogram_bot_checker():
    app = pyrogram.Client('my_account_check', api_id=api_id, api_hash=api_hash, phone_number=api_number)

    async def checker():
        while True:
            # ACTION
            # await app.send_message("me", "OMG")
            pass

    # Запуск бота
    print('PyroBot Checker запущен')
    await app.start()
    # Запуск функции чека
    await checker()


if __name__ == '__main__':
    # Главная функция MAIN
    async def main():
        # Запуск 2 ботов одновременно (или 3)
        await asyncio.gather(
            aiogram_bot(),  # Запуск aiogram'a
            pyrogram_bot_checker(),  # Запуск Pyrogram циклированное действие
            pyrogram_bot_on_message(),  # Запуск Pyrogram хендлер на сообщение
        )


    asyncio.run(main())
