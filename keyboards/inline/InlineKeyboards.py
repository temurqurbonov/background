from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='πΊπΏ uz',callback_data='uzbek'),
            InlineKeyboardButton(text='πΊπΈ eng',callback_data='english'),
            InlineKeyboardButton(text='π·πΊ ru',callback_data='rus')
        ],
    ]
)

