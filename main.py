import telebot

import keyboards
import utils
import config

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id,
                     text=config.START_TEXT,
                     reply_markup=keyboards.start_keyboard(),
                     parse_mode='Markdown',
                     )
    

@bot.message_handler(commands=['menu'])
def menu_message(message):
    bot.send_message(chat_id=message.chat.id,
                     text=config.START_TEXT,
                     reply_markup=keyboards.start_keyboard(),
                     parse_mode='Markdown',
                     )
    

@bot.callback_query_handler(func = lambda call: True)
def callback_query(call):
    """Handles queries from inline keyboards."""

    # getting message's and user's ids
    message_id = call.message.id
    chat_id = call.message.chat.id
    user_username = call.from_user.username

    call_data = call.data.split('_')
    query = call_data[0]

    if query == 'services':
        bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.SERVICES_TEXT,
                                parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.services_keyboard(),
                                        )
        
    elif query == 'permit':
        bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.PERMIT_TEXT,
                                parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.permit_keyboard(),
                                        )

    elif query in config.BACK_SERVICES:
        bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.BACK_SERVICES[query],
                                parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.manager_keyboard('services'),
                                        )
    
    elif query in config.BACK_PERMIT:
        bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.BACK_PERMIT[query],
                                parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.manager_keyboard('permit'),
                                        )

    elif query == 'manager':
        destination = call_data[1]

        bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.CONSULTATION_TEXT,
                                parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.manager_keyboard(destination),
                                        )
    
    elif query == 'contacts':
        destination = call_data[1]

        bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.CONTACTS_TEXT,
                                parse_mode='Markdown',
                            )
        
        bot.edit_message_reply_markup(chat_id=chat_id,
                                        message_id=message_id,
                                        reply_markup=keyboards.contacts_keyboard(destination),
                                        )
        
    elif query == 'consultation':
        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        bot.send_message(chat_id=chat_id,
                         text=config.ENTER_NAME_TEXT,
                         reply_markup=keyboards.enter_name_keyboard(),
                         )

    elif query == 'back':
        destination = call_data[1]

        if destination == 'main':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=config.START_TEXT,
                                  parse_mode='Markdown',
                                )
            
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.start_keyboard(),
                                          )
            
        elif destination == 'services':
            bot.edit_message_text(chat_id=chat_id,
                                  message_id=message_id,
                                  text=config.SERVICES_TEXT,
                                  parse_mode='Markdown',
                                )
            
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=message_id,
                                          reply_markup=keyboards.services_keyboard(),
                                          )
        
        elif destination == 'permit':
            bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text=config.PERMIT_TEXT,
                                parse_mode='Markdown',
                            )
        
            bot.edit_message_reply_markup(chat_id=chat_id,
                                            message_id=message_id,
                                            reply_markup=keyboards.permit_keyboard(),
                                            )
    
    elif query == 'menu':
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=message_id,
                                      reply_markup=telebot.types.InlineKeyboardMarkup(),
                                      )

        bot.send_message(chat_id=chat_id,
                     text=config.START_TEXT,
                     reply_markup=keyboards.start_keyboard(),
                     parse_mode='Markdown',
                     )
        

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Handles message with type text."""
    
    if (message.reply_to_message is not None) and\
    (str(message.reply_to_message.from_user.id) == config.BOT_ID):
        
        username = message.from_user.username
        chat_id = message.chat.id
        message_id = message.reply_to_message.id

        try:
            bot.delete_message(chat_id=chat_id, message_id=message_id)
        except:
            pass

        if config.ENTER_NAME_TEXT in message.reply_to_message.text:
            reply_text = f'''
                        \nИмя: {message.text}\
                        \n\
                        \n{config.ENTER_PHONE_TEXT}\
                        '''
            
            bot.send_message(chat_id=chat_id,
                             text=reply_text,
                             reply_markup=keyboards.enter_phone_keyboard(),
                             )

        elif config.ENTER_PHONE_TEXT in message.reply_to_message.text:

            bot.send_message(chat_id=chat_id,
                             text=config.CONFIRM_TEXT,
                             reply_markup=keyboards.menu_keyboard(),
                             )
            
            name = utils.get_name(message.reply_to_message.text)
            phone = message.text

            inform_text = f'''
                            \nПользователь @{username} оставил заявку на консультацию:\
                            \n\
                            \nИмя: {name}\
                            \nНомер телефона: {phone}\
                            '''
            try:
                bot.send_message(chat_id=config.MANAGER_ID,
                                 text=inform_text,
                                 )
            except Exception as ex:
                print(ex)


if __name__ == '__main__':
    # bot.polling(timeout=80)
    while True:
        try:
            bot.polling()
        except:
            pass