import API as keys
import responses as R
from telegram.ext import *

print("Bot Initiated...")

def start_command(update, context):
    update.message.reply_text("Type something to get started.\n\nEscribe algo para comenzar.")

def contact_command(update, context):
    update.message.reply_text("You can find my creator at:\n\nTwitter: https://twitter.com/TheCryptoChad_\n\nLinkedIn: https://www.linkedin.com/in/adham-elneser-issa-87524a22a/\n\nGitHub: https://github.com/TheCryptoChad")

def contacto_command(update, context):
    update.message.reply_text("Puedes encontrar a mi creador en:\n\nTwitter: https://twitter.com/TheCryptoChad_\n\nLinkedIn: https://www.linkedin.com/in/adham-elneser-issa-87524a22a/\n\nGitHub: https://github.com/TheCryptoChad")

def help_command(update, context):
    update.message.reply_text("/start - Start the bot.\n/contact - Show my creator's profile.\n/help - Display a list of English commands.\n/ayuda - Mostrar una lista de comandos en Español.\n\nYou can also strike up conversation, or type the name of any cryptocurrency to display it's market data.")

def ayuda_command(update, context):
    update.message.reply_text("/start - Iniciar el bot.\n/contacto - Mostrar el perfil de mi creador.\n/ayuda - Mostrar una lista de comandos en Español.\n/help - Display a list of Enslish commands.\n\nTambién puedes conversar conmigo, o escribir el nombre de cualquier criptomoneda para mostrar su información de mercado.")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("contact", contact_command))
    dp.add_handler(CommandHandler("contacto", contacto_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("ayuda", ayuda_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()