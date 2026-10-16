import telebot
import os
from flask import Flask
from threading import Thread
import cleanup

# Handlers import
from handlers import (
    start_handler,
    bgremove_handler,
    gen_handler,
    chk_handler,
    bin_handler,
    reveal_handler,
    gemini_handler,
    gart_handler,
    imagine_handler,
    say_handler,
    translate_handler,
    download_handler,
    gpt_handler,
    converter_handler,
    fkAddress_handler,
    userinfo_handler,
    yt_handler
)

BOT_TOKEN = "8451057287:AAEWkkNW3Ny6374I_YQE2Piln2-Xo0028PQ"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# Flask for web hosting
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

# Register handlers from other files with status tracking
def register_handler(handler_module, handler_name):
    try:
        handler_module.register(bot)
        print(f"✅ {handler_name} handler loaded successfully")
    except Exception as e:
        print(f"❌ {handler_name} handler failed to load: {str(e)}")

print("\n🔄 Loading command handlers...")
print("-" * 40)

# Register all handlers
register_handler(start_handler, "Start")
register_handler(gen_handler, "Gen")
register_handler(chk_handler, "Check")
register_handler(bin_handler, "BIN")
register_handler(reveal_handler, "Reveal")
register_handler(gemini_handler, "Gemini")
register_handler(gart_handler, "Gart")
register_handler(imagine_handler, "Imagine")
register_handler(say_handler, "Say")
register_handler(translate_handler, "Translate")
register_handler(download_handler, "Download")
register_handler(converter_handler, "Converter")
register_handler(bgremove_handler, "BG Remove")
register_handler(gpt_handler, "GPT")
register_handler(fkAddress_handler, "Fake Address")
register_handler(userinfo_handler, "User Info")
register_handler(yt_handler, "yt")

print("-" * 40)
print("✨ Handler registration completed!\n")

cleanup.cleanup_project()

if __name__ == '__main__':
    print("🤖 Bot is running...")
    bot.infinity_polling()
