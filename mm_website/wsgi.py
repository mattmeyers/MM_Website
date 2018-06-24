import os
import sys
import logging
from dotenv import load_dotenv

path_to_file = os.path.dirname(os.path.abspath(__file__))

env_path = f'{path_to_file}/../.env'
load_dotenv(dotenv_path=env_path)

logging.basicConfig(stream=sys.stderr)

# Add the current directory to the python path.
sys.path.insert(0, path_to_file)

from mm_website import create_app
application = create_app()
