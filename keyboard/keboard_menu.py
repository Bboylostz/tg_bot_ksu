from aiogram.types import (InlineKeyboardButton,
                           InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton)

'''это клавиатура снизу, она пока нам не нужна'''

'''кейборд клавиатура'''
# main = ReplyKeyboardMarkup(keyboard=[
# [KeyboardButton(text="Услуги банка", callback_data="bank_services"),KeyboardButton(text="Информация", callback_data="info")],
# [KeyboardButton(text="Помощь", callback_data="help"), KeyboardButton(text="Выход", callback_data="exit")],],
# resize_keyboard=True, input_field_placeholder='выберите пункт', )
# оставил для будующего


'''инлайн клавиатура'''
credit_card = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ОФОРМИТЬ КАРТУ',
                          url='https://alfabank.ru/get-money/credit-cards/land/60-days-partners/?platformId=alfapartners_msv_CC-60_962348_3469224&utm_source=alfapartners&utm_medium=msv&utm_term=CC-60&utm_campaign=962348&utm_content=alfapartners_msv_CC-60_962348_3469224')],

])

debet_card = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ОФОРМИТЬ КАРТУ',
                          url='https://alfabank.ru/lp/retail/dc/flexible-agent/?platformId=alfapartners_msv_DC-flexible_962348_3469097&utm_source=alfapartners&utm_medium=msv&utm_term=DC-flexible&utm_campaign=962348be&utm_content=alfapartners_msv_DC-flexible_962348_3469097')],

])

inline_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ОФОРМИТЬ КАРТУ', callback_data='apply_for_a_card')],
    [InlineKeyboardButton(text='СТАТЬ ПАРТНЕРОМ', callback_data='become_a_partner')],
    [InlineKeyboardButton(text='СУТЬ РАБОТЫ', callback_data='work')],
])

inline_menu_choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ДЕБЕТОВУЮ', callback_data='debet')],
    [InlineKeyboardButton(text='КРЕДИТНУЮ', callback_data='credit')],

])

partners_enter = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ШАГ 1. СДЕЛАТЬ ДЕБЕТОВУЮ КАРТУ', callback_data='debet')],
    [InlineKeyboardButton(text='ШАГ 2. РЕГИСТРАЦИЯ (карта есть)', callback_data='register_debet')],
    [InlineKeyboardButton(text='СКОЛЬКО БУДУТ ПЛАТИТЬ?', callback_data='income_many')],
    [InlineKeyboardButton(text='МОЖНО ЛИ СОВМЕЩАТЬ', callback_data='combine')],
])

ip_check = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ДА, я ИП', callback_data='ip_check_yes')],
    [InlineKeyboardButton(text='НЕТ, я не ИП', callback_data='ip_check_no')],

])

continue_ip_check_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как зарегистрироваться Агентом', callback_data='continue_ip_check_no')],

])

info_ip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я ИП на УСН, надо открыть счет', callback_data='ip_usn_1')],
    [InlineKeyboardButton(text='Я ИП на УСН, уже есть счет', callback_data='ip_usn_2')],
    [InlineKeyboardButton(text='Я ИП на НПД', callback_data='ip_usn_3')],

])
ip_usn_1_enter = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ОТКРЫТЬ СЧЕТ ИП',
                          url='https://alfabank.ru/sme/partner/ag/?platformId=alfapartners_msv_rko-anketa_962348_3469333&utm_source=alfapartners&utm_medium=msv&utm_term=rko-anketa&utm_campaign=962348&utm_content=alfapartners_msv_rko-anketa_962348_3469333')],
    [InlineKeyboardButton(text='Я ОТКРЫЛ(А) СЧЕТ ИП', callback_data='ip_usn_1_yes')],
    [InlineKeyboardButton(text='ХЕЛП', callback_data='help')],

])

instruktion_register_ip_na_usp = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ССЫЛКА НА РЕГИСТРАЦИЮ', callback_data='register_url')],
    [InlineKeyboardButton(text='Я зарегистрировался! Что дальше?', callback_data='i_register_to')],
    [InlineKeyboardButton(text='Нужна помощь', callback_data='help')], ])

register_receiving_card = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='РЕГИСТРАЦИЯ (когда получишь карту)', callback_data='register_receiving_card')]])
