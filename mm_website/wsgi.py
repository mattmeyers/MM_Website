import sys
import logging
from dotenv import load_dotenv
from pathlib import path

env_path = Path('.')/'../.env'
load_dotenv(dotenv_path=env_path)

logging.basicConfig(stream=sys.stderr)

# Add the current directory to the python path.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mm_website import create_app
application = create_app()
