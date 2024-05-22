import jwt
from datetime import datetime, timedelta
from app.config import Config

def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, hours=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return e

def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, Config.SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
