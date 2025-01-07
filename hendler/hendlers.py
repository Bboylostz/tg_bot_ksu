from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import Message

import keyboard.keboard_menu as kbm

router = Router()
router_last = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f"Здравствуйте, <b>{message.from_user.first_name.title()}!</b>\n"
                              f"Давайте разберемся, что вас интересует")
    await message.answer(
        '👉 Оформить бесплатную дебетовую карту Альфа Банка и получать доход в виде кэшбэка до 5000 рублей в месяц за привычные покупки?\n\n'
        '👉 Стать партнёром проекта \"Свой в Альфе\" и зарабатывать удалённо без продаж и вложений в своём темпе?\n\n'
        '👉 Принять участие в акции от Альфа Банка и ЗАРАБОТАТЬ 80 тыс за месяц\n\n'
        'Выбирай, что тебе интересно, и начнём 🚀', reply_markup=kbm.inline_menu)

# команды меню
@router.message(F.text == '/all_products')
async def all_products(message: Message):
    await message.answer(f'вы выбрали все продукты')


@router.message(F.text == '/discount')
async def discount(message: Message):
    await message.answer(f'вы выбрали все discount')


@router.message(F.text == '/my_mentor')
async def my_mentor(message: Message):
    await message.answer(
        f'<b>{message.from_user.first_name}</b> мы рады вам помочь, если есть какие-нибудь вопросы, пишите @kseni_iv')

#для всех не описанных команд
@router_last.message()
async def non_cmd(message: Message):
    await message.answer(
        text=f'Извините {message.from_user.first_name.title()}, я не понял, о чем вы спрашиваете. Попробуйте использовать команду /start для просмотра доступных действий.')
