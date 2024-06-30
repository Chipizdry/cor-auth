from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlalchemy_database_url: str = "sqlite:///./sql_auth.db"
    algorithm: str = "ALGORITHM"
    secret_key: str = "SECRET_KEY"
    mail_username: str = "MAIL_USERNAME"
    mail_password: str = "MAIL_PASSWORD"
    mail_from: str = "Cor.Auth@EXAMPLE.COM"
    mail_port: int = 0
    mail_server: str = "MAIL_SERVER"
    pythonpath: str = "PYTHONPATH"
    encryption_key: str = "ENCRYPTION_KEY"

    class Config:
        env_file = "cor-auth.env"
        env_file_encoding = "utf-8"


settings = Settings()
