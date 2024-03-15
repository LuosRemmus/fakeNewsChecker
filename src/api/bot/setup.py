from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
import redis.asyncio

from config import settings

redis = redis.asyncio.from_url(settings.CELERY_BROKER_REDIS_URL)
storage = RedisStorage(redis)

bot = Bot(settings.TELEGRAM_TOKEN)
dp = Dispatcher(storage=storage)

# initialize routers
