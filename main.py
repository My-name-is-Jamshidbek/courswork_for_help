from aiogram import executor


if __name__ == '__main__':
    from app import dp
    executor.start_polling(dp)
