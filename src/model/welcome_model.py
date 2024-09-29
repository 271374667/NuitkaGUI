from typing import Optional

from src.common.manager.pip_manager import PipManager
from src.config import cfg, PipSrouce


class WelcomeModel:
    def __init__(self):
        self._pip_manager = PipManager()

    @property
    def pip_source(self) -> PipSrouce:
        return cfg.get(cfg.pip_source)

    @pip_source.setter
    def pip_source(self, value: PipSrouce) -> None:
        cfg.set(cfg.pip_source, value)

    @property
    def default_pip_source(self) -> PipSrouce:
        return PipSrouce.Default

    def auto_pip_source(self) -> Optional[str]:
        return self._pip_manager.get_fastest_url([i.value for i in PipSrouce])


if __name__ == '__main__':
    model = WelcomeModel()
