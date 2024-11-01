import asyncio
import logging

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


from project_bot.apps.bot.main_bot import bot


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **options):
        # logger_level=settings.LOG_LEVEL
        try:
            asyncio.run(bot.infinity_polling(logger_level=settings.LOG))
        except Exception as err:
            logger.error(f'Ошибка: {err}')