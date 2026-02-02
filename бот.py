import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8241604307:AAGLkPPQH_kvtxEwgRM9iURiBBYlfXLyqmU"


bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================
# КНОПКИ
# =========================

def main_menu():
    kb = InlineKeyboardBuilder()

    kb.button(text="🎨 Заказать аватарку", callback_data="avatar")
    kb.button(text="👨‍👩‍👦 Вступить в семью BR", callback_data="family")
    kb.button(text="🚇 Скачать 2D Metro Royale", callback_data="metro")
    kb.button(text="⭐ Отзывы", callback_data="reviews")

    kb.adjust(1)
    return kb.as_markup()


def back_button():
    kb = InlineKeyboardBuilder()
    kb.button(text="⬅ Назад в меню", callback_data="back")
    return kb.as_markup()


# =========================
# START
# =========================

@dp.message(CommandStart())
async def start(message: Message):
    text = (
        "👋 *Добро пожаловать!*\n\n"
        "🔥 Здесь ты можешь:\n\n"
        "🎨 Сделать аватарку на заказ\n"
        "👨‍👩‍👦 Вступить в семью Black Russia\n"
        "🚇 Скачать 2D Metro Royale\n"
        "⭐ Почитать отзывы\n\n"
        "👇 Выбирай нужный пункт:"
    )

    await message.answer(text, reply_markup=main_menu(), parse_mode="Markdown")


# =========================
# КНОПКА НАЗАД
# =========================

@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.edit_text(
        "👇 Главное меню:",
        reply_markup=main_menu()
    )
    await callback.answer()


# =========================
# АВАТАРКИ
# =========================

@dp.callback_query(F.data == "avatar")
async def avatar(callback: CallbackQuery):
    text = (
        "🎨 *Заказ аватарки*\n\n"
        "Хочешь крутую аву для профиля, канала или клана?\n"
        "Делаем в любом стиле: аниме, игровые, 3D, минимализм и т.д.\n\n"
        "📩 Для заказа напиши:\n"
        "👉 @zztx15\n\n"
        "Опиши идею + отправь примеры ✨"
    )

    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")
    await callback.answer()


# =========================
# СЕМЬЯ BR
# =========================

@dp.callback_query(F.data == "family")
async def family(callback: CallbackQuery):
    text = (
        "👨‍👩‍👦 *Вступление в семью Black Russia*\n\n"
        "Ищешь активную и дружную семью?\n"
        "Совместные капты, помощь новичкам, фан и движ каждый день 🔥\n\n"
        "📩 Чтобы вступить, напиши:\n"
        "👉 @zztx15\n\n"
        "Укажи: ник, сервер и уровень"
    )

    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")
    await callback.answer()


# =========================
# METRO
# =========================

@dp.callback_query(F.data == "metro")
async def metro(callback: CallbackQuery):
    text = (
        "🚇 *2D Metro Royale*\n\n"
        "Лёгкая 2D версия Metro Royale:\n"
        "• оптимизация для слабых телефонов\n"
        "• плавный FPS\n"
        "• минимальный вес\n\n"
        "📥 Чтобы получить файл, напиши:\n"
        "👉 @zztx15"
    )

    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")
    await callback.answer()


# =========================
# ОТЗЫВЫ
# =========================

@dp.callback_query(F.data == "reviews")
async def reviews(callback: CallbackQuery):
    text = (
        "⭐ *Отзывы*\n\n"
        "💬 «Аватарка просто пушка!»\n"
        "💬 «Приняли в семью за 5 минут»\n"
        "💬 «Метро идёт без лагов»\n\n"
        "Хочешь так же?\n"
        "👉 Напиши @zztx15"
    )

    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")
    await callback.answer()


# =========================
# ЗАПУСК
# =========================

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
