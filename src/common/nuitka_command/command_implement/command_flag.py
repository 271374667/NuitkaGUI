from src.common.nuitka_command.command import CommandFlagBase


class CommandOneFile(CommandFlagBase):
    command: str = 'onefile'
    name: str = '单文件'
    description: str = '将所有文件打包到一个exe文件中'


class CommandStandAlone(CommandFlagBase):
    command: str = 'standalone'
    name: str = '多文件'
    description: str = '将所有文件打包到一个文件夹中'
    enabled = True
    _value = True


class CommandShowProgress(CommandFlagBase):
    command: str = 'show-progress'
    name: str = '显示进度'
    description: str = '在输出窗口内显示打包进度'


class CommandShowMemory(CommandFlagBase):
    command: str = 'show-memory'
    name: str = '显示内存占用'
    description: str = '在输出框内显示内存占用'


class CommandRemoveOutput(CommandFlagBase):
    command: str = 'remove-output'
    name = '自动删除构建文件夹'
    description = '构建完成后自动删除构建文件夹'


class CommandLowMemory(CommandFlagBase):
    command: str = 'low-memory'
    name = '低内存模式'
    description = '编译时占用更少的内存(速度会变慢)'


class CommandMingw64(CommandFlagBase):
    command: str = 'mingw64'
    name = '使用mingw64'
    description = '兼容性比clang更好, 但是速度会慢一些'


class CommandClang(CommandFlagBase):
    command: str = 'clang'
    name = '使用clang'
    description = 'clang编译器,速度更快,但是兼容性不如mingw64'


class CommandQuiet(CommandFlagBase):
    command: str = 'quiet'
    name = '安静模式'
    description = '不显示任何输出'


class CommandLtoNo(CommandFlagBase):
    command: str = 'lto=no'
    name = '关闭lto'
    description = 'lto能够提高性能,减小体积,但是会增加编译时间,关闭lto可以减少编译时间'


class CommandDisableCcache(CommandFlagBase):
    command: str = 'disable-ccache=all'
    name = '禁用缓存'
    description = '不使用缓存,进行完整的重新编译(适合报错的情况)'


class CommandCleanCache(CommandFlagBase):
    command: str = 'clean-cache=all'
    name = '清除缓存'
    description = '在开始编译之前清除之前的所有缓存'


class CommandAssumeYesForDownloads(CommandFlagBase):
    command: str = 'assume-yes-for-downloads'
    name = '自动下载'
    description = '自动下载Nuitka的依赖'


class CommandWindowsUacAdmin(CommandFlagBase):
    command: str = 'windows-uac-admin'
    name = '软件获取管理员权限'
    description = '打包的程序在启动的时候会请求管理员权限'


class CommandWindowsUacAccess(CommandFlagBase):
    command = 'windows-uac-access'
    name = '访问权限'
    description = '打包的程序在启动的时候会请求访问权限'


class CommandWarnImplicitExceptions(CommandFlagBase):
    command: str = 'warn-implicit-exceptions'
    name: str = '编译时显示警告隐式异常'
    description: str = '在编译时警告可能的隐式异常'
