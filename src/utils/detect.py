import subprocess


def isPythonAvailable(pythonExePath: str):
    try:
        output = subprocess.check_output([pythonExePath, "-V"], timeout=3)
    except (TimeoutError, FileNotFoundError):
        output = b""
    return output.startswith(b"Python 3.")
