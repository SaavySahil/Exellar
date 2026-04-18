import os
from dotenv import load_dotenv

load_dotenv()

# Base directory = exellar-backend/
_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _fix_db_url(url):
    """Render gives postgres:// but SQLAlchemy 2.x requires postgresql://"""
    if url and url.startswith('postgres://'):
        return url.replace('postgres://', 'postgresql://', 1)
    return url


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = _fix_db_url(
        os.environ.get('DATABASE_URL', 'sqlite:///exellar.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 280,
        'connect_args': {'connect_timeout': 10},
    }
    _upload_env = os.environ.get('UPLOAD_FOLDER', 'uploads')
    UPLOAD_FOLDER = _upload_env if os.path.isabs(_upload_env) else os.path.join(_BASE_DIR, _upload_env)
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))
    JWT_EXPIRY_HOURS = int(os.environ.get('JWT_EXPIRY_HOURS', 24))
    CORS_ORIGINS = os.environ.get(
        'CORS_ORIGINS',
        'http://localhost:3000,http://localhost:5173,https://exellar-gray.vercel.app'
    ).split(',')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = _fix_db_url(os.environ.get('DATABASE_URL', ''))


config = {
    'development': Config,
    'production': ProductionConfig,
    'default': Config
}
