import asyncio
import asyncpg
from app.core.config import settings


async def create_db():
    conn = await asyncpg.connect(
        host=settings.POSTGRES_HOST,
        port=settings.POSTGRES_PORT,
        user=settings.POSTGRES_USER,
        password=settings.POSTGRES_PASSWORD,
        database="postgres"  # подключаемся к системной базе
    )

    # Проверяем, есть ли база
    db_exists = await conn.fetchval(
        "SELECT 1 FROM pg_database WHERE datname = $1",
        settings.POSTGRES_DB
    )
    if not db_exists:
        await conn.execute(f'CREATE DATABASE "{settings.POSTGRES_DB}"')
        print(f"Database {settings.POSTGRES_DB} created")
    else:
        print(f"Database {settings.POSTGRES_DB} already exists")

    await conn.close()


asyncio.run(create_db())
