from PySide6.QtWidgets import QApplication

from src.presenter.main_presenter import MainPresenter


def main():
    app = QApplication([])
    main_presenter = MainPresenter()
    main_presenter.view.show()
    app.exec()


if __name__ == '__main__':
    main()
