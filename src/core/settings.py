from typing import Sequence

MAX_FILES_IN_DIR: int = 1000
IGNORE_DIRS: Sequence[str] = ('.git',
                              '.idea',
                              '__pycache__',
                              'dist',
                              'build',
                              'venv',
                              ".idea",
                              'node_modules')
