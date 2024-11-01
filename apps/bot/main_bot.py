import telebot
import logging
from telebot import util
from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
import asyncio


bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')

telebot.logger.setLevel(settings.LOG)

logger = logging.getLogger(__name__)

@bot.chat_member_handler()
async def chat_member_handler_bot(message):

    status = message.difference.get('status')
    full_name = message.from_user.full_name
    username = message.from_user.username
    id = message.from_user.id
    invite_link_creator = None
    invite_link = None

    try:
        invite_link_creator = getattr(invite_link.creator, 'full_name')
        invite_link = getattr(invite_link, 'invite_link')
    except AttributeError as err:
        logger.info(f'Зашёл не по ссылке {err}')
    current_status = status[1]
    if current_status == 'member':
        status = 'Подписались 🎉'
    elif current_status == 'left':
        status = 'Отписались 😩'
    else:
        status = 'Не понятненько'
    text_message = (f'Статус {status}\n'
                    f'Имя {full_name}\n'
                    f'ID {id}')
    if username:
        text_message += f'\nНик @{username}'
    if invite_link_creator:
        text_message += f'\nСоздатель инвайта {invite_link_creator}'
    if invite_link:
        text_message += f'\nИнвайт {invite_link}'
    #
    # logger.info(f'{status=}')
    # logger.info(f'{full_name=}')
    # logger.info(f'{username=}')
    # logger.info(f'{id=}')
    # logger.info(f'{invite_link=}')
    await bot.send_message(chat_id=settings.TELEGA_ID_ADMIN, text=text_message)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi bro!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

