from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Описание по умолчанию'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: EmailStr | None = None
    first_superuser_password: str | None = None

    class Config:
        env_file = '.env'


settings = Settings()
