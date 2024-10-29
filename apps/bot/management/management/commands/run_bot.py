import asyncio

from django.core.management.base import BaseCommand, CommandError
from telebot import util

from project_bot.apps.bot.main_bot import bot


class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **options):
        # logger_level=settings.LOG_LEVEL
        asyncio.run(bot.infinity_polling(allowed_updates=util.update_types))