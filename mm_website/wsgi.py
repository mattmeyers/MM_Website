import sys
import logging
from mcgpyutils import FileSystemUtils

logging.basicConfig(stream=sys.stderr)

# Add the current directory to the python path.
fsu = FileSystemUtils()
sys.path.insert(0, fsu.get_path_to_script(__file__))

from __init__ import create_app
application = create_app()
