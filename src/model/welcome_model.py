from src.config import cfg, PipSrouce


class WelcomeModel:
    def use_default_pip_source(self):
        cfg.set(cfg.pip_source, PipSrouce.Default)

if __name__ == '__main__':
    model = WelcomeModel()
    model.use_default_pip_source()