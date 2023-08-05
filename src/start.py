from pathlib import Path

from src.core import globalVar, initVar

# 0.0.6 的计划
# TODO: 增加兼容性模式和增强兼容性模式
# TODO: 添加pipreqs自动生成requirements.txt文件
# Done: 使用QProcess代替命令行
# Done: 安装模块的时候能选中最快的源

# 0.0.7 的计划
# TODO: 内置GCC
# TODO: 将命令行输出改为既可以用GUI输出也可以用命令行输出
# TODO: 通过命令来初始化nuitkaGUI
# TODO: 能够加载上一次的配置
# TODO: 为命令行GUI添加进度条
# TODO: 添加自动更新功能

# 0.0.8 的计划
# TODO: 增加i18n支持
# TODO: 界面的美化
# TODO: 批处理文件的编写(打包多个入口文件)

globalVar.homePath = Path(__file__).parent

if __name__ == "__main__":
    initVar.initLogger()
    initVar.initWindow()
    print(Path(__file__).parent)

    globalVar.mainWindow.show()
    globalVar.app.exec()
