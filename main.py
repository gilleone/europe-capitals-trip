import logging
from aiogram import Bot, Dispatcher, executor
from app.config import TOKEN_API

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


if __name__ == "__main__":
    # from app.handlers import dp
    from app.handlerstest import dp

    executor.start_polling(dp, skip_updates=True)
