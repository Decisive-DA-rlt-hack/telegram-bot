from aiogram import Bot, Dispatcher, executor, types
import os

import db


TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


class Best_In_World_AI_Bot:

    button_zakazchik = types.KeyboardButton('Заказчик')
    button_pokupatel = types.KeyboardButton('Покупатель')
    gender = types.ReplyKeyboardMarkup()
    gender.add(button_zakazchik)
    gender.add(button_pokupatel)

    BD = {}

    def __init__(self, token: str):
        self.bot = Bot(token=token)

    async def send_welcome(self, message: types.Message):

        user_id = message.from_user.id

        if db.get_user(user_id):
            await message.answer("Вы уже прошли регистрацию")
        else:
            await message.answer("Выберите пол", reply_markup=self.gender)

    async def register_gender(self, message: types.Message):

        user_id = message.from_user.id

        if db.get_user(user_id):
            await message.answer("Вы уже выбрали свой пол")
        else:
            db.add(user_id, message.text)
            await message.answer(f"Вы выбрали пол {message.text}", reply_markup=types.ReplyKeyboardRemove())

    def start(self):
        dp = Dispatcher(self.bot)
        dp.register_message_handler(self.send_welcome, commands=['start'])
        dp.register_message_handler(
            self.register_gender,
            lambda msg: msg.text == "Заказчик" or msg.text == "Покупатель"
        )
        executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    b = Best_In_World_AI_Bot(TELEGRAM_API_TOKEN)
    b.start()
