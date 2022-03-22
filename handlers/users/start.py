from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
# from keyboards.inline.Kanal import inline_uz
from keyboards.inline.azolikni_tekshirish import inline_uz

from filters import Shaxsiy
from filters import Shaxsiy

from loader import dp







@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum , {message.from_user.first_name}Botni ishga tushirish meni guruxingizga qoshib admin qiling ",reply_markup=inline_uz)

