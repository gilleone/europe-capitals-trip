import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.config import TOKEN_API

logger = logging.getLogger(__name__)


def setup_logger(level: logging) -> None:
    format = "| %(asctime)s | - | %(levelname)s | - | %(name)s | - | %(message)s"
    logging.basicConfig(level=level, format=format)


bot = Bot(token=TOKEN_API)
dp = Dispatcher()


async def main():
    from app.handlers_a3 import dp

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        setup_logger(logging.INFO)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("bot stopped by ctrl+c")
