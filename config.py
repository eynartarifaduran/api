class Config:
    # Secret key for JWT
    SECRET_KEY = 'your-secret-key'

    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
