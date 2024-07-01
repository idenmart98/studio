from django.core.management.base import BaseCommand
from django.conf import settings
import telebot

class Command(BaseCommand):
    help = 'Set the webhook for the Telegram bot'

    def handle(self, *args, **kwargs):
        token = settings.BOT_TOKEN
        webhook_url = settings.WEBHOOK_URL

        if token and webhook_url:
            bot = telebot.TeleBot(token)
            bot.remove_webhook()
            bot.set_webhook(url=webhook_url)
            self.stdout.write(self.style.SUCCESS(f'Successfully set webhook to {webhook_url}'))
        else:
            self.stdout.write(self.style.ERROR('BOT_TOKEN or WEBHOOK_URL is not set'))
