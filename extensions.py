import os
import logging

from dotenv import load_dotenv


logging.basicConfig(
    handlers=[logging.FileHandler('logfile.log', 'w', 'utf-8')],
    format='%(levelname)s: %(message)s',
    datefmt='%m-%d %H:%M',
    level=getattr(logging, os.getenv('LOG_LEVEL', 'DEBUG'))
)

LOGGER = logging.getLogger(__name__)


dot_env_path = os.path.join(os.path.dirname(__file__),
                            os.path.join(os.getcwd(), '.env'))
load_dotenv(dot_env_path)

RabbitMQ_CON_LINE = os.getenv("RabbitMQ_CON_LINE")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
FB_VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")

