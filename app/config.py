from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Line Bot API"
    line_channel_secret: str
    line_channel_access_token: str

    class Config:
        env_file = "../.env"
