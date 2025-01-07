import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import load_dotenv

from hendler.hendlers import router, router_last
from hendler.hendlers_menu import private

load_dotenv()


async def main():
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))  # parse_mode=ParseMode.HTML для добавление стилей HTML
    dp = Dispatcher()
    dp.include_router(router)  # подключаем роутер из хендлерс
    dp.include_router(router_last)
    await bot.set_my_commands(commands=private,
                              scope=BotCommandScopeAllPrivateChats())  # команда что бы сделать маленькую
    # кнопочку меню сбоку BotCommandScopeAllPrivateChats для приватного чата, можно сделать для разных чатов типа для групп
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.INFO)
    # замедляет работу но дает вывод в терминал,
    # пользоваться только при дебаге
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('бот выключен')
