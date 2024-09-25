from typing import Sequence

MAX_FILES_IN_DIR: int = 500
MAX_RECURSION_LEVEL: int = 500
IGNORE_DIRS: Sequence[str] = (
    ".git",
    ".idea",
    "__pycache__",
    "dist",
    "build",
    "venv",
    ".idea",
    "node_modules",
)
DEFAULT_OPTIMIZATION_OPTIONS: dict[str, Sequence[str]] = {
    "Normal": ['show-progress',
                'assume-yes-for-downloads'
                ],
    "Compatibility": ['show-progress',
                      'show-memory',
                      'mingw64',
                      'disable-ccache=all',
                      'assume-yes-for-downloads',
                      'warn-implicit-exceptions'
                      ],
    "Speed": ['show-progress',
              'clang',
              'lto=no',
              'assume-yes-for-downloads',
              'plugin-no-detection'
              ],
    "Size": ['show-progress',
             'remove-output',
             'mingw64',
             'assume-yes-for-downloads'
             ],
}
