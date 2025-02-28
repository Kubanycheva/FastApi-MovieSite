from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = 'bbcb6b6de0affe9361c69f20a71a55baa212b45c762af73e4e528a0d5db4d12c'
ACCESS_TOKEN_EXPIRE_MINUTES = 40
REFRESH_TOKEN_EXPIRE_DAYS = 3
ALGORITHM = 'HS256'
