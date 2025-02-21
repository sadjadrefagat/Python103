from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# botbot123456bot
TOKEN = '7998237751:AAFOWW_VmADPw8k8GeWk90BOizWcc8jrwTc'


# تابعی برای دریافت محصول
def get_products():
    site_address = 'https://www.digikala.com/search/category-notebook-netbook-ultrabook/'
    response = requests.get(site_address)

    # کد وضعیت 200 یعنی درخواست با موفقیت پاسخ داده شده است
    if response.status_code == 200:
        return "محصولات با موفقیت دریافت شدند!"
    else:
        return "خطا در دریافت محصولات!"


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('''سلام!
لطفا برای دریافت لیست محصولات ما، /products را بفرستید.''')


async def products(update: Update, context: CallbackContext):
    products_text = get_products()
    await update.message.reply_text(products_text)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('products', products))

    print("ربات در حال اجرا است...")
    app.run_polling()


if __name__ == '__main__':
    main()
