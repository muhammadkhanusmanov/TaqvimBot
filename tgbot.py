from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton,ChatAdministratorRights

from db import DB

token = ''

db = DB('db.json')

def starting(update: Update, context: CallbackContext):
    bot=context.bot 
    chat_id=update.message.chat.id
    db.checkin(str(chat_id))
    db.save()
    name=update.message.chat.first_name
    text=f'Aссалому алайкум {name}'
    uz=InlineKeyboardButton('🇺🇿Узбекча',callback_data='til uz')
    ru=InlineKeyboardButton('🇷🇺Руский',callback_data='til ru')
    button=InlineKeyboardMarkup([[uz,ru]])
    bot.sendMessage(chat_id,text,reply_markup=button)

def tekshir(chat_id,bot):
    data=DB('db.json')
    kan1=data.kanal()
    chan1=bot.getChatMember(f'@{kan1[13:]}',str(chat_id))['status']

    if chan1=='left':
        return False
    return True

def obuna(update:Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    bot=context.bot 
    message_iid = query.message.message_id
    dt = db.get()
    kanal = dt['obuna']
    lang = db.get_lang(str(chat_id))
    db.add_lang(str(chat_id),lang)
    if lang=='uz':
        text='Ботдан тўлиқ фойдаланиш учун каналга обуна бўлинг ва текшириш тугмасини босинг.'
        obuna = InlineKeyboardButton('1-Канал',callback_data='obuna 1', url=kanal)
        tek=InlineKeyboardButton('Текшириш',callback_data='obuna tek')
        button=InlineKeyboardMarkup([[obuna],[tek]])
        bot.edit_message_text(text,chat_id,message_id=message_iid,reply_markup=button)
    else:
        text='Чтобы полноценно использовать бота, подпишитесь на канал и нажмите кнопку подтверждения.'
        obuna = InlineKeyboardButton('Канал 1',callback_data='obuna 1', url=kanal)
        tek=InlineKeyboardButton('Проверять',callback_data='obuna tek')
        button=InlineKeyboardMarkup([[obuna],[tek]])
        bot.edit_message_text(text,chat_id=chat_id,message_id=message_iid,reply_markup=button)
    db.save()












updater=Updater(token)

updater.dispatcher.add_handler(CommandHandler('start',starting))
updater.dispatcher.add_handler(CallbackQueryHandler(obuna,pattern='til'))



updater.start_polling()
updater.idle()