import ctypes
from enum import Enum
from pathlib import Path
from typing import List


class FILETIME(ctypes.Structure):
    _fields_ = [
        ("dwLowDateTime", ctypes.c_uint32),
        ("dwHighDateTime", ctypes.c_uint32),
    ]


class WIN32_FIND_DATA(ctypes.Structure):
    _fields_ = [
        ("dwFileAttributes", ctypes.c_uint32),
        ("ftCreationTime", FILETIME),
        ("ftLastAccessTime", FILETIME),
        ("ftLastWriteTime", FILETIME),
        ("nFileSizeHigh", ctypes.c_uint32),
        ("nFileSizeLow", ctypes.c_uint32),
        ("dwReserved0", ctypes.c_uint32),
        ("dwReserved1", ctypes.c_uint32),
        ("cFileName", ctypes.c_wchar * 260),
        ("cAlternateFileName", ctypes.c_wchar * 14),
    ]


INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value
FILE_ATTRIBUTE_DIRECTORY = 0x10


class WindowExplorerUtils:
    class FileType(Enum):
        FILES = 1
        DIRECTORIES = 2
        BOTH = 3

    def __init__(self):
        self._kernel32 = ctypes.windll.kernel32
        self._kernel32.FindFirstFileW.argtypes = [ctypes.c_wchar_p, ctypes.POINTER(WIN32_FIND_DATA)]
        self._kernel32.FindFirstFileW.restype = ctypes.c_void_p
        self._kernel32.FindNextFileW.argtypes = [ctypes.c_void_p, ctypes.POINTER(WIN32_FIND_DATA)]
        self._kernel32.FindNextFileW.restype = ctypes.c_bool
        self._kernel32.FindClose.argtypes = [ctypes.c_void_p]
        self._kernel32.FindClose.restype = ctypes.c_bool

    def get_dir_files(self, source_dir_path: Path) -> List[str]:
        files = []
        stack = [source_dir_path]

        while stack:
            current_dir = stack.pop()
            search_path = str(current_dir / '*')
            find_data = WIN32_FIND_DATA()
            handle = self._kernel32.FindFirstFileW(search_path, ctypes.byref(find_data))

            if handle == INVALID_HANDLE_VALUE:
                err = ctypes.GetLastError()
                print(f"Error finding first file: {err}")
                continue

            try:
                while True:
                    file_name = find_data.cFileName
                    if file_name not in ('.', '..'):
                        file_path = current_dir / file_name
                        if find_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY:
                            stack.append(file_path)
                        else:
                            files.append(str(file_path))

                    if not self._kernel32.FindNextFileW(handle, ctypes.byref(find_data)):
                        err = ctypes.GetLastError()
                        if err == 18:  # ERROR_NO_MORE_FILES
                            break
                        else:
                            print(f"Error finding next file: {err}")
                            break
            finally:
                if handle != INVALID_HANDLE_VALUE:
                    self._kernel32.FindClose(handle)

        return files

    def get_dir_files_count(self, source_dir_path: Path, file_type: FileType) -> int:
        file_count = 0
        search_path = str(source_dir_path / '*')
        find_data = WIN32_FIND_DATA()
        handle = self._kernel32.FindFirstFileW(search_path, ctypes.byref(find_data))

        if handle == INVALID_HANDLE_VALUE:
            err = ctypes.GetLastError()
            print(f"Error finding first file: {err}")
            return file_count

        try:
            while True:
                file_name = find_data.cFileName
                if file_name not in ('.', '..'):
                    if find_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY:
                        if file_type in (self.FileType.DIRECTORIES, self.FileType.BOTH):
                            file_count += 1
                    else:
                        if file_type in (self.FileType.FILES, self.FileType.BOTH):
                            file_count += 1

                if not self._kernel32.FindNextFileW(handle, ctypes.byref(find_data)):
                    err = ctypes.GetLastError()
                    if err == 18:  # ERROR_NO_MORE_FILES
                        break
                    else:
                        print(f"Error finding next file: {err}")
                        break
        finally:
            if handle != INVALID_HANDLE_VALUE:
                self._kernel32.FindClose(handle)

        return file_count

    def find_files_in_dir(self, source_dir_path: Path, search_file_name: str, file_type: FileType) -> List[Path]:
        found_files = []
        search_path = str(source_dir_path / '*')
        find_data = WIN32_FIND_DATA()
        handle = self._kernel32.FindFirstFileW(search_path, ctypes.byref(find_data))

        if handle == INVALID_HANDLE_VALUE:
            err = ctypes.GetLastError()
            print(f"Error finding first file: {err}")
            return found_files

        try:
            while True:
                file_name = find_data.cFileName
                if file_name not in ('.', '..'):
                    file_path = source_dir_path / file_name
                    if find_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY:
                        if file_type in (self.FileType.DIRECTORIES, self.FileType.BOTH):
                            if search_file_name in file_name:
                                found_files.append(file_path)
                    else:
                        if file_type in (self.FileType.FILES, self.FileType.BOTH):
                            if search_file_name in file_name:
                                found_files.append(file_path)

                if not self._kernel32.FindNextFileW(handle, ctypes.byref(find_data)):
                    err = ctypes.GetLastError()
                    if err == 18:  # ERROR_NO_MORE_FILES
                        break
                    else:
                        print(f"Error finding next file: {err}")
                        break
        finally:
            if handle != INVALID_HANDLE_VALUE:
                self._kernel32.FindClose(handle)

        return found_files

    def find_files_in_dir_recursive(self, source_dir_path: Path, search_file_name: str, file_type: FileType) -> List[
        Path]:
        found_files = []
        stack = [source_dir_path]
        find_data = WIN32_FIND_DATA()

        while stack:
            current_dir = stack.pop()
            search_path = str(current_dir / '*')
            handle = self._kernel32.FindFirstFileW(search_path, ctypes.byref(find_data))

            if handle == INVALID_HANDLE_VALUE:
                err = ctypes.GetLastError()
                print(f"Error finding first file: {err}")
                continue

            try:
                while True:
                    file_name = find_data.cFileName
                    if file_name not in ('.', '..'):
                        file_path = current_dir / file_name
                        if find_data.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY:
                            stack.append(file_path)
                            if file_type in (self.FileType.DIRECTORIES, self.FileType.BOTH):
                                if search_file_name in file_name:
                                    found_files.append(file_path)
                        else:
                            if file_type in (self.FileType.FILES, self.FileType.BOTH):
                                if search_file_name in file_name:
                                    found_files.append(file_path)

                    if not self._kernel32.FindNextFileW(handle, ctypes.byref(find_data)):
                        err = ctypes.GetLastError()
                        if err == 18:  # ERROR_NO_MORE_FILES
                            break
                        else:
                            print(f"Error finding next file: {err}")
                            break
            finally:
                if handle != INVALID_HANDLE_VALUE:
                    self._kernel32.FindClose(handle)

        return found_files

    def get_dir_size(self, source_dir_path: Path) -> float:
        """获取文件夹大小，单位为MB"""
        total_size = 0
        files = self.get_dir_files(source_dir_path)

        for file in files:
            try:
                find_data = WIN32_FIND_DATA()
                handle = self._kernel32.FindFirstFileW(file, ctypes.byref(find_data))
                if handle != INVALID_HANDLE_VALUE:
                    # 计算文件大小
                    file_size = (find_data.nFileSizeHigh << 32) + find_data.nFileSizeLow
                    total_size += file_size
                    self._kernel32.FindClose(handle)
            except Exception as e:
                print(f"Error calculating file size for {file}: {str(e)}")

        return total_size / (1024 * 1024)


# Example usage
if __name__ == "__main__":
    directory = Path(r"E:\load\python\Project\nuitkaGUIOld\githubOpenSource2")
    directory2 = Path(r'E:\load\python\Project\NuitkaGUI')
    fs = WindowExplorerUtils()
    print(fs.find_files_in_dir_recursive(directory2, 'python.exe', WindowExplorerUtils.FileType.FILES))
    # files = fs.get_dir_files(directory)
    # print(f"Files in directory: {files}")
    # file_count = fs.get_dir_files_count(directory, WindowExplorerUtils.FileType.FILES)
    # print(f"File count: {file_count}")
    # dir_count = fs.get_dir_files_count(directory, WindowExplorerUtils.FileType.DIRECTORIES)
    # print(f"Directory count: {dir_count}")

    # search_file_name = "tran"
    # found_files = fs.find_files_in_dir(directory, search_file_name, WindowExplorerUtils.FileType.FILES)
    # print(f"Files found: {found_files}")
    #
    # dir_size = fs.get_dir_size(directory)
    # print(f"Directory size: {dir_size:.2f} MB")
