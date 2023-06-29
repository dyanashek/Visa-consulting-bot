from telebot import types

import config

def start_keyboard():
    '''Generates start keyboard'''

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Услуги', callback_data = f'services'))
    keyboard.add(types.InlineKeyboardButton('Бесплатная консультация', callback_data = f'manager_main'))
    keyboard.add(types.InlineKeyboardButton('Контакты', callback_data = f'contacts_main'))

    return keyboard


def services_keyboard():
    '''Generates keyboard with services list.'''

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('ВНЖ', callback_data = f'permit'))
    keyboard.add(types.InlineKeyboardButton('Открытие счета', callback_data = f'account'))
    keyboard.add(types.InlineKeyboardButton('Присяжный перевод документов', callback_data = f'translate'))
    keyboard.add(types.InlineKeyboardButton('Получение ипотеки', callback_data = f'mortgage'))
    keyboard.add(types.InlineKeyboardButton('Недвижимость', callback_data = f'property'))
    keyboard.add(types.InlineKeyboardButton('Бесплатная консультация', callback_data = f'manager_services'))
    keyboard.add(types.InlineKeyboardButton('Контакты', callback_data = f'contacts_services'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = f'back_main'))

    return keyboard


def manager_keyboard(destination):
    '''Generates keyboard that allows contact with manager.'''

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Записаться на консультацию', callback_data = f'consultation'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = f'back_{destination}'))

    return keyboard


def permit_keyboard():
    '''Generates keyboard with permit options.'''

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Учебная виза', callback_data = f'study'))
    keyboard.add(types.InlineKeyboardButton('Виза цифрового кочевника', callback_data = f'digital'))
    keyboard.add(types.InlineKeyboardButton('ВНЖ без права на работу', callback_data = f'stay'))
    keyboard.add(types.InlineKeyboardButton('ВНЖ для инвесторов', callback_data = f'invest'))
    keyboard.add(types.InlineKeyboardButton('Продление ВНЖ', callback_data = f'prolongation'))
    keyboard.add(types.InlineKeyboardButton('Гражданство Турции', callback_data = f'turkey'))
    keyboard.add(types.InlineKeyboardButton('Бесплатная консультация', callback_data = f'manager_permit'))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = f'back_services'))

    return keyboard


def enter_name_keyboard():
    """Makes a reply to a message that asks about the name."""
    return types.ForceReply(input_field_placeholder=f'Введите Ваше имя')


def enter_phone_keyboard():
    """Makes a reply to a message that asks about the name."""
    return types.ForceReply(input_field_placeholder=f'Номер телефона или e-mail')


def menu_keyboard():
    '''Generates keyboard with menu button.'''

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('🏠 Главное меню', callback_data = f'menu'))

    return keyboard


def contacts_keyboard(destination):
    '''Generates keyboard with contacts.'''

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('WhatsApp', url = f'http://wa.me/{config.WHATSAPP_PHONE}'))
    keyboard.add(types.InlineKeyboardButton('Менеджер в Telegram', url = f'https://t.me/{config.TELEGRAM_MANAGER}'))
    keyboard.add(types.InlineKeyboardButton('Telegram канал', url = config.TELEGRAM_CHANNEL))
    keyboard.add(types.InlineKeyboardButton('Наш сайт', url = config.WEBSITE))
    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data = f'back_{destination}'))

    return keyboard