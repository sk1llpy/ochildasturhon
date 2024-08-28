from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / 'media/'

class PostgresSettings(BaseSettings):
    name: str
    user: str
    password: str
    host: str
    port: int
    
    @property
    def url(self):
        psql = f"{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
        return f"postgresql://{psql}"

    model_config = SettingsConfigDict(
        env_prefix='DB_', 
        env_file=BASE_DIR / '.env',
        extra='ignore'  # Ignore extra environment variables
    )

class DjangoSettings(BaseSettings):
    secret_key: str
    debug: bool
    allowed_hosts: str
    csrf_trusted_origins: str
    
    @property
    def csrf_trusted_origins_list(self):
        return [origin for origin in self.csrf_trusted_origins.split(",")]
    
    @property
    def allowed_hosts_list(self):
        return [allowed_host for allowed_host in self.allowed_hosts.split(",")]

    model_config = SettingsConfigDict(
        env_prefix='DJANGO_', 
        env_file=BASE_DIR / '.env',
        extra='ignore'  # Ignore extra environment variables
    )

class BotSettings(BaseSettings):
    token: str
    name: str
    admins: str
    web_app_url: str
    admins_chat_id: int

    model_config = SettingsConfigDict(
        env_prefix='BOT_', 
        env_file=BASE_DIR / '.env',
        extra='ignore'  # Ignore extra environment variables
    )

    @property
    def bot_admins(self):
        return [int(admin) for admin in self.admins.split(",")]
