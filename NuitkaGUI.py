import loguru
from PySide6.QtWidgets import QApplication

from src.config import cfg
from src.presenter.main_presenter import MainPresenter
from src.presenter.welcome_presenter import WelcomePresenter


@loguru.logger.catch(reraise=True)
def main():
    app = QApplication([])
    is_first_run: bool = cfg.get(cfg.is_first_run)
    print(is_first_run)
    if is_first_run:
        welcome_presenter = WelcomePresenter()
        welcome_presenter.view.show()
    else:
        main_presenter = MainPresenter()
        main_presenter.view.show()
    app.exec()


if __name__ == "__main__":
    main()
