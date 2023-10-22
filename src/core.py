from enum import Enum


class Plugin(Enum):
    ANTI_BLOAT = 'anti-bloat'
    DATA_FILES = 'data-files'
    DELVEWHEEL = 'delvewheel'
    DILL_COMPAT = 'dill-compat'
    DLL_FILES = 'dll-files'
    ENUM_COMPAT = 'enum-compat'
    EVENTLET = 'eventlet'
    GEVENT = 'gevent'
    GI = 'gi'
    GLFW = 'glfw'
    IMPLICIT_IMPORTS = 'implicit-imports'
    KIVY = 'kivy'
    MATPLOTLIB = 'matplotlib'
    MULTIPROCESSING = 'multiprocessing'
    NO_QT = 'no-qt'
    OPTIONS_NANNY = 'options-nanny'
    PBR_COMPAT = 'pbr-compat'
    PKG_RESOURCES = 'pkg-resources'
    PMW_FREEZER = 'pmw-freezer'
    PYLINT_WARNINGS = 'pylint-warnings'
    PYQT5 = 'pyqt5'
    PYQT6 = 'pyqt6'
    PYSIDE2 = 'pyside2'
    PYSIDE6 = 'pyside6'
    PYWEBVIEW = 'pywebview'
    TK_INTER = 'tk-inter'
    TRANSFORMERS = 'transformers'
    UPX = 'upx'


class BoolCommands(Enum):
    onefile = '--onefile'
    standalone = '--standalone'
    show_progress = '--show-progress'
    show_memory = '--show-memory'
    remove_output = '--remove-output'
    low_memory = '--low-memory'
    windows_disable_console = '--windows-disable-console'
    mingw64 = '--mingw64'
    quiet = '--quiet'
    lto_no = '--lto=no'
    disable_ccache = '--disable-ccache'
    assume_yes_for_downloads = '--assume-yes-for-downloads'
    clang = '--clang'
    windows_uac_admin = '--windows-uac-admin'
    clean_cache = '--clean-cache'


class StrCommands(Enum):
    output_dir = '--output-dir'
    main = '--main'
    nofollow_import_to = '--nofollow-import-to'
    include_package = '--include-package'
    include_data_dir = '--include-data-dir'
    windows_icon_from_ico = '--windows-icon-from-ico'
    windows_company_name = '--windows-company-name'
    windows_file_version = '--windows-file-version'
    windows_product_version = '--windows-product-version'
    windows_file_description = '--windows-file-description'
    onefile_tempdir_spec = '--onefile-tempdir-spec'


class IntCommands(Enum):
    jobs = '--jobs'


class JsonSettings(Enum):
    PythonExe = 'pythonexe'
    FastestPipSrouce = 'pypi_url'
    GccAvailable = 'gcc_available'
    FirstRun = 'first_run'
    OptimizationEnabled = 'optimization_enabled'
