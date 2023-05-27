"""
app file
"""
# imports
from aiogram.types import ContentType as Ct, InputFile

from loader import dp
from aiogram.types import Message as Mm
from keyboardbutton import keyboardbutton
from states import *
from config import PRODUCTS


# cmd start
async def cmd_start(m: Mm):
    """
    :param m:
    :return:
    """
    product_names = []
    for i in PRODUCTS:
        product_names.append(i["nomi"])

    await m.answer(f"{m.from_user.full_name} botga hush kelibsiz.\nMahsulot nomini tanlashingiz mumkin:",
                   reply_markup=keyboardbutton(product_names))
    await User_state.main_menu.set()


async def main_menu(m: Mm):
    """
    :param m:
    :return:
    """
    product = None

    for i in PRODUCTS:
        if i["nomi"] == m.text:
            product = i
            break
        else:
            product = False

    await m.answer_photo(photo=InputFile(product['photo']), caption=f"Nomi: {product['nomi']}\n"
                                                                    f"Razmer: {product['razmer']}\n"
                                                                    f"Eski narx: {product['eski_narx']}❎\n"
                                                                    f"AKSIYADAGI NARX: {product['yangi_narx']}✅"
                         )
    await m.answer("Mahsulot nomini tanlashingiz mumkin:")
    await User_state.main_menu.set()


dp.register_message_handler(cmd_start, content_types=[Ct.TEXT])
dp.register_message_handler(main_menu, content_types=[Ct.TEXT], state=User_state.main_menu)
