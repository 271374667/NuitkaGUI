import json
import os
import subprocess
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout, QTextEdit, QDialog

class Package(QThread):
    # nuitka_log = Signal(str)  # 定义一个信号
    finished = Signal()

    def __init__(self, nuitka_path, script_path, user_args):
        super().__init__()
        self.nuitka_path = nuitka_path
        self.python_path = os.path.dirname(nuitka_path)+"//activate.bat"
        self.script_path = script_path
        self.user_args = user_args

    def run(self):
        # subprocess.call([self.nuitka_path, self.script_path] + self.user_args)
        # 执行命令，并将输出发送到日志窗口
        print("开始打包")
        # 保存为bat
        '''
        @echo off
        REM 激活虚拟环境
        call E:/Code/GIT/Umi-OCR//venv//Scripts//activate.bat

        REM 执行nuitka
        nuitka E:/Code/GIT/Umi-OCR/main.py --standalone --output-dir=o
        pause
        '''
        bat_args = ' '.join(self.user_args)
        bat_content = ('@echo off\n'+'REM 激活虚拟环境\n'+'call '+self.python_path+'\n'+'nuitka '+self.script_path+' '+bat_args+'\n'+'pause')
        with open("run.bat", "w") as f:
            f.write(bat_content)
        # command = [self.nuitka_path, self.script_path] + self.user_args
        # python_dir = os.path.dirname(self.nuitka_path)
        # python_bat = python_dir + "//activate.bat"
        # env_list = []
        # env_list.append(os.path.dirname(python_dir))
        # env_list.append(self.old_python_dir)
        # env_list.append(os.path.dirname(python_dir) + "//Lib")
        # env_strs = str(";".join(env_list))
        # # env_dict = {"PATH": env_strs}
        # env_vars = os.environ
        # env_vars["PATH"] = env_vars["PATH"]+";"+env_strs
        # print("当前系统变量为：", env_vars)
        # p = subprocess.Popen("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # p.stdin.write(bat_content.encode())
        # p.stdin.flush()
        # while True:
        #     bytes_str = p.stdout.readline()
        #     result = chardet.detect(bytes_str)
        #     output = p.stdout.readline().decode(result['encoding'])
        #     if output == '' and p.poll() is not None:
        #         break
        #     self.nuitka_log.emit(output.strip())  # 发射信号
        #     print(output)
        os.system('run.bat')
        self.finished.emit()


class NewVenv(QThread):
    finished = Signal(str)

    def __init__(self, script_path, python_path):
        super().__init__()
        self.python_path = python_path
        self.python_dir = os.path.dirname(python_path)
        self.env_path = os.path.dirname(script_path)

    def run(self):
        # 获取当前的PATH环境变量
        # 将外部Python解释器的路径加入到PATH环境变量中
        os.environ["PYTHONHOME"] = self.python_dir
        # subprocess.call([self.nuitka_path, self.script_path] + self.user_args)
        # 执行命令，并将输出发送到日志窗口
        print("创建新环境", self.env_path)
        venv_path = self.env_path + "//venv//"
        bat_venv = ('@echo off\n'+'REM 创建虚拟环境\n'+'call '+self.python_path+' -m venv '+venv_path+'\n')
        with open("venv.bat", "w") as f:
            f.write(bat_venv)
        os.system('venv.bat')
        if os.path.exists(venv_path):
            python_dir = self.env_path + "//venv//Scripts"
            self.finished.emit(python_dir)
        else:
            print('创建新环境失败')

class LogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('日志窗口')
        self.resize(400, 400)

        # 创建文本编辑器
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # 创建布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.text_edit)

    def append_log(self, text):
        # 在文本编辑器中追加日志消息
        self.text_edit.append(text)


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.user_config = {}
        self.user_args = []
        self.initUI()
        # self.log_window = LogWindow(self)
        # self.log_window.show()
        self.loadCofig()

    def initUI(self):
        # 创建三个文本框和三个按钮
        self.input1 = QLineEdit(placeholderText='')
        self.btn1 = QPushButton('入口文件路径', self)
        self.input2 = QLineEdit(placeholderText='Python.exe')
        self.btn2 = QPushButton('执行文件路径', self)
        self.input3 = QLineEdit('requirements.txt')
        self.btn3 = QPushButton('依赖管理文件', self)
        self.text_edit = QTextEdit(self, placeholderText="--standalone --windows-disable-console")
        self.btn_load = QPushButton('使用配置文件', self)
        self.btn_save = QPushButton('保存配置文件', self)
        self.btn_ok = QPushButton('开始打包', self)

        # 将按钮与槽函数关联
        self.btn1.clicked.connect(self.showFileDialog1)
        self.btn2.clicked.connect(self.showFileDialog2)
        self.btn3.clicked.connect(self.showFileDialog3)
        self.text_edit.textChanged.connect(self.editClicked)
        self.btn_load.clicked.connect(self.loadClicked)
        self.btn_save.clicked.connect(self.saveClicked)
        self.btn_ok.clicked.connect(self.okClicked)
        # 创建一个垂直布局并将输入框和按钮添加到其中
        vbox = QVBoxLayout()
        v1, v2, v3, v4 = QHBoxLayout(), QHBoxLayout(), QHBoxLayout(), QHBoxLayout()
        v1.addWidget(self.input1)
        v1.addWidget(self.btn1)
        v2.addWidget(self.input2)
        v2.addWidget(self.btn2)
        v3.addWidget(self.input3)
        v3.addWidget(self.btn3)
        v4.addWidget(self.btn_load)
        v4.addWidget(self.btn_save)
        v4.addWidget(self.btn_ok)
        vbox.addLayout(v1)
        vbox.addLayout(v2)
        vbox.addLayout(v3)
        vbox.addWidget(self.text_edit)
        vbox.addLayout(v4)
        # 将布局应用于窗口
        self.setLayout(vbox)
        self.pj_path = os.path.curdir

    def loadCofig(self):
        config_path = self.pj_path + "//user_config.json"
        if os.path.exists(config_path):
            config_path = config_path
        else:
            config_path = os.path.dirname(self.pj_path) + "//user_config.json"
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            self.user_config = user_config
            # 打印加载的数据
            self.input1.setText(user_config['script_path'])
            self.input2.setText(user_config['python_exe'])
            self.input3.setText(user_config['env_file'])
            user_config_text = "  ".join(user_config['user_arg'])
            self.text_edit.setText(user_config_text)
        except Exception:
            # print("配置文件有问题")
            print("\n无配置文件!")

    def loadClicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', self.pj_path, "程序配置文件(*user_config.json)")
        # 加载JSON文件
        try:
            with open(filename, 'r') as f:
                user_config = json.load(f)
            self.user_config = user_config
            # 打印加载的数据
            self.input1.setText(user_config['script_path'])
            self.input2.setText(user_config['python_exe'])
            self.input3.setText(user_config['env_file'])
            user_config_text = "  ".join(user_config['user_arg'])
            self.text_edit.setText(user_config_text)
            print("\n成功使用配置文件！")
        except Exception:
            # print("配置文件有问题")
            print("\n配置文件有问题!")

    def editClicked(self):
        # 针对user_arg格式处理
        user_args = self.text_edit.toPlainText().strip().split("--")[1:]
        new_user_args = []
        for user_arg in user_args:
            new_user_args.append('--' + user_arg.strip())
        self.user_config['user_arg'] = new_user_args  # user_arg

    def saveClicked(self):
        # 定义一个字典
        user_config = {}
        user_config['script_path'] = self.input1.text().strip()  # script_path = self.input1.text().strip()  # 主文件路径
        user_config['python_exe'] = self.input2.text().strip()  # nuitka_path = self.input2.text().strip()  # nuitka路径
        user_config['env_file'] = self.input3.text().strip()  # nuitka_path = self.input2.text().strip()  # env_file
        # 针对user_arg格式处理
        user_args = self.text_edit.toPlainText().strip().split("--")[1:]
        new_user_args = []
        for user_arg in user_args:
            new_user_args.append('--' + user_arg.strip())
        user_config['user_arg'] = new_user_args  # user_arg
        # 将字典保存为JSON文件
        self.user_config = user_config
        # print(user_config)
        with open('user_config.json', 'w') as f:
            json.dump(user_config, f)
        print("\n成功保存配置文件！")

    def showFileDialog1(self):
        # 显示文件选择对话框
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', self.pj_path, "项目入口文件(*.py)")
        self.pj_path = os.path.dirname(filename)
        # 将选择的文件路径显示在对应的输入框中
        self.user_config['script_path'] = filename.strip()
        self.input1.setText(filename)
        # print("打包主文件为：", filename)
        print("\n打包主项目入口为：" + str(filename))

    def showFileDialog2(self):
        # 显示文件夹选择对话框
        filename, _ = QFileDialog.getOpenFileName(self, '选择文件', self.pj_path, "python.exe(*python.exe)")
        # 将选择的文件夹路径显示在对应的输入框中
        self.user_config['python_exe'] = self.input2.text().strip()
        self.input2.setText(filename)
        # print("选择的Python环境路径：", filename)
        print("\n选择的Python环境路径为：" + str(filename))

    def showFileDialog3(self):
        # 显示文件选择对话框
        filename, _ = QFileDialog.getOpenFileName(self, self.pj_path, '选择文件')
        # 将选择的文件路径显示在对应的输入框中
        self.user_config['env_file'] = filename.strip()
        self.input3.setText(filename)
        # print("选择的requirements.txt路径：", filename)
        print("\n选择的requirements.txt路径：" + str(filename))

    def okClicked(self):
        # 开始打包
        print("\n开始打包...")
        script_path = self.user_config['script_path']  # 主文件路径
        script_dir = os.path.dirname(script_path)
        python_path = self.input2.text().strip()
        python_dir = os.path.dirname(python_path)  # Python路径
        python_dll = python_dir + "/Dlls"
        self.old_python_dir = python_dir
        python_bat = python_dir + "//activate.bat"
        if os.path.exists(python_bat):
            self.on_package(python_dir)
        else:
            python_dir = script_dir + "//venv//Scripts"
            python_bat = python_dir + "//activate.bat"
            if os.path.exists(python_bat):
                self.on_package(python_dir)
            else:
                self.new_venv = NewVenv(script_path, python_path)
                self.new_venv.finished.connect(self.on_package)  # 连接信号和槽函数
                self.new_venv.start()

    def on_package(self, python_dir):
        # print("当前Python路径：", python_dir)
        print("\n当前Python路径为：" + str(python_dir))
        # 配置PythonPath
        # sys_path = os.environ.get('PATH')
        # sys.path = sys_path.split(os.pathsep) + sys.path
        # sys.path.append(os.path.dirname(python_dir))
        # sys.path.append(os.path.dirname(python_dir) + "//Lib")
        # print("\n当前系统变量为：：" + str(";".join(sys.path)))
        # print("当前系统变量为：", sys.path)
                # 获取当前的PATH环境变量
        path_env = os.environ.get("PATH")
        # 将外部Python解释器的路径加入到PATH环境变量中
        os.environ["PATH"] = "{};{}".format(path_env, python_dir)
        print("当前环境变量为：",os.environ)
        pip3_path = python_dir + "//pip3.exe"
        nuitka_path = python_dir + "//nuitka.bat"
        python_bat = python_dir + "//activate.bat"
        script_path = self.user_config['script_path']
        user_args = self.user_config['user_arg']
        env_file = self.user_config['env_file']
        # 激活 python 环境
        subprocess.run(['set','pythonpath=',python_dir], shell=True) # 激活Python环境
        subprocess.run(python_bat, shell=True) # 激活Python环境
        # 安装nuitka
        subprocess.call([pip3_path, 'install', '-U', 'nuitka'])
        subprocess.call([pip3_path, 'install', '-U', 'ordered-set'])
        # 读写env_list
        try:
            env_list = []
            with open(env_file, 'r') as f:
                env_list.append(f.readline().strip())
            print(env_file)
            subprocess.call([pip3_path, 'install', '-r', env_file],shell=True)
        except FileNotFoundError:
            print("\n打开requirements.txt错误，自动生成中...")
            subprocess.call([pip3_path, 'freeze > requirements.txt'], shell=True)  # 帮你生成requirements.txt
            self.input3.setText('requirements.txt')
        print("开始执行Package...")
        self.worker = Package(nuitka_path, script_path, user_args)
        # self.worker.nuitka_log.connect(self.on_log)  # 连接信号和槽函数
        self.worker.finished.connect(self.on_finished)  # 连接信号和槽函数
        self.worker.start()

    # def on_log(self, nuitka_log):
    #     print(nuitka_log)

    def on_finished(self):
        if os.path.exists('venv.bat'):
            os.remove('venv.bat')
        print("--------------------------------------------------------------")