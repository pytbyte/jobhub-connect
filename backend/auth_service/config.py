# auth_service/config.py

import os

class Config:
    # MySQL database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://username:password@localhost/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'

    # Redis configuration (if using Redis for caching)
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
