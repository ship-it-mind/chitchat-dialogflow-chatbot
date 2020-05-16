import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dot_env_path = os.path.join(os.path.dirname(__file__),
                            os.path.join(os.getcwd(), '.env'))
load_dotenv(dot_env_path)


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
