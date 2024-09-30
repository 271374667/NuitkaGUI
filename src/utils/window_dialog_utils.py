import ctypes
from ctypes import wintypes


class WindowDialogUtils:
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.user32.MessageBoxW.argtypes = [
            wintypes.HWND,
            wintypes.LPCWSTR,
            wintypes.LPCWSTR,
            wintypes.UINT
        ]

    def create_warning_dialog(self, title: str, content: str) -> bool:
        """Creates a warning dialog with an OK button."""
        return self._show_message_box(title, content, 0x30)

    def create_success_dialog(self, title: str, content: str) -> bool:
        """Creates a success dialog with an OK button."""
        # Assuming 0x40 as an icon representing success (information)
        return self._show_message_box(title, content, 0x40)

    def create_info_dialog(self, title: str, content: str) -> bool:
        """Creates an information dialog with an OK button."""
        return self._show_message_box(title, content, 0x40)

    def _show_message_box(self, title: str, content: str, icon_type: int) -> bool:
        """Shows a message box with the specified icon and an OK button."""
        result = self.user32.MessageBoxW(0, content, title, icon_type | 0x00000000)
        return result == 1


if __name__ == '__main__':
    dialog = WindowDialogUtils()
    dialog.create_success_dialog('Success', 'This is a successful message.')
    dialog.create_warning_dialog('Warning', 'This is a warning message.')
    dialog.create_info_dialog('Information', 'This is an information message.')
