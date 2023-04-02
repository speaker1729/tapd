import User, File, Admin
from MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItem, QStandardItemModel


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 页面更改
        self.ui.btn_user.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.btn_admin.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.btn_file.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        # 用户页面
        self.ui.btn_registry.pressed.connect(self.registry)
        self.ui.btn_login.pressed.connect(self.login)
        self.ui.btn_logout.pressed.connect(self.logout)
        # 管理员页面
        self.ui.btn_choose.pressed.connect(self.choose)
        self.ui.btn_delete.pressed.connect(self.delete)
        self.ui.btn_apply.pressed.connect(self.apply)
        self.ui.btn_cancle.pressed.connect(self.cancle)
        self.ui.btn_open.pressed.connect(self.open)
        self.ui.btn_add.pressed.connect(self.add)
        self.ui.lv_user.clicked.connect(self.select_0)
        self.ui.lv_folder.clicked.connect(self.select_1)
        # 文件页面
        self.ui.btn_upview.pressed.connect(self.upview)
        self.ui.btn_up.pressed.connect(self.up)
        self.ui.btn_down.pressed.connect(self.down)
        self.ui.btn_downview.pressed.connect(self.downview)
        self.ui.lv_folder_2.clicked.connect(self.select_2)
        # 共享变量
        self.model = [QStandardItemModel() for i in range(3)]
        self.user_cur = None  # 用户状态
        self.file_cur = None  # 文件状态
        # 管理员用
        self.user_tem = None  # 临时用户
        self.file_tem = None  # 临时文件

    # 用户界面按钮
    def registry(self):
        username = self.ui.in_username.text()
        password = self.ui.in_password.text()
        statue = User.registry(username, password)
        # 展示状态
        self.ui.lab_statue.setText(statue + ' ' + username)
        # 创建用户文件访问列表
        if statue == '注册成功':
            if username == 'admin':
                # 管理员访问全部文件
                User.save(username, password, [['*', '*']])
                # 并创建密钥对
                Admin.create(password)
            else:
                # 其他用户默认无文件访问
                User.save(username, password, [['^', '^']])
                # 保存该用户的密钥
                Admin.save_key(username, password)

    def login(self):
        username = self.ui.in_username.text()
        password = self.ui.in_password.text()
        statue = User.login(username, password)
        # 展示状态
        self.ui.lab_statue.setText(statue + ' ' + username)
        # 导入用户
        if statue == '登录成功':
            # 展示用户
            self.ui.lab_user.setText(username)
            # 导入用户名
            self.user_cur = (username, password)
            # 导入文件
            self.file_cur = User.load(username, password)
            if username == 'admin':
                # 管理员可访问用户列表
                self.ui.lab_admin.setText('是')
                # 管理员可访问所有文件
                self.file_cur = Admin.load_list(password)

    def logout(self):
        if self.user_cur:
            # 更改状态
            self.ui.lab_statue.setText('退出登录' + ' ' + self.user_cur[0])
            # 当前没有用户
            self.ui.lab_user.setText('无')
            if self.user_cur[0] == 'admin':
                # 退出管理员界面的登录
                self.ui.lab_admin.setText('否')
            # 清空信息
            self.user_cur = None
            self.file_cur = None
            self.ui.in_username.clear()
            self.ui.in_password.clear()

    # 管理员界面按钮
    def choose(self):
        if self.ui.lab_admin.text() == '否':
            return '非管理员'
        # 列出用户
        if self.ui.lab_userview.text() == '无':
            # 列出所有用户
            files = File.get_all('Users/sha')
            # 除去管理员
            files.remove('admin')
            # 清理现文件再添加
            self.model[0].clear()
            for file in files:
                item = QStandardItem(file)
                self.model[0].appendRow(item)
            self.ui.lv_user.setModel(self.model[0])
        # 重新加载
        elif self.file_tem:
            # 清理现文件再添加
            self.model[0].clear()
            files = [f[0] for f in self.file_tem]
            for file in files:
                item = QStandardItem(file)
                self.model[0].appendRow(item)
            self.ui.lv_user.setModel(self.model[0])
        # 列出用户的可访问文件
        else:
            if not self.user_tem:
                username = self.ui.lab_userview.text()
                password = Admin.load_key(username, self.user_cur[1])
                # 临时用户导入
                self.user_tem = [username, password]
            else:
                username = self.user_tem[0]
                password = self.user_tem[1]
            # 导入文件
            self.file_tem = User.load(username, password)
            files = File.filter(self.file_tem)
            # 清理现文件再添加
            self.model[0].clear()
            for file in files:
                item = QStandardItem(file[0])
                self.model[0].appendRow(item)
            self.ui.lv_user.setModel(self.model[0])

    def delete(self):
        if self.ui.lab_admin.text() == '否':
            return '非管理员'
        # 获取文件名
        filename = self.ui.lab_userview.text()
        # 找到并删除
        for i in range(len(self.file_tem)):
            if self.file_tem[i][0] == filename:
                self.file_tem.pop(i)
                # GUI
                self.choose()
                break

    def apply(self):
        if self.ui.lab_admin.text() == '否':
            return '非管理员'
        # 应用
        username = self.user_tem[0]
        password = self.user_tem[1]
        User.save(username, password, self.file_tem)
        # 返回上一级 未选择用户
        self.ui.lab_userview.setText('无')
        self.choose()
        # 将临时文件清空
        self.file_tem = None

    def cancle(self):
        if self.ui.lab_admin.text() == '否':
            return '非管理员'
        # 返回上一级 未选择用户
        self.ui.lab_userview.setText('无')
        self.choose()
        # 将临时文件清空
        self.file_tem = None

    def open(self):
        if self.ui.lab_admin.text() == '否':
            return '非管理员'
        # 清理现文件再添加
        self.model[1].clear()
        files = File.get_all('Data')
        for file in files:
            item = QStandardItem(file)
            self.model[1].appendRow(item)
        self.ui.lv_folder.setModel(self.model[1])

    def add(self):
        if self.ui.lab_admin.text() == '否':
            return '非管理员'
        # 清理现文件再添加
        # 获取文件名
        filename = self.ui.lab_folder.text()
        # 找到并添加
        for i in range(len(self.file_cur)):
            if self.file_cur[i][0] == filename:
                t = [filename, self.file_cur[i][1]]
                self.file_tem.append(t)
                # GUI
                self.choose()
                break

    def select_0(self, index):
        # 选取管理员页面的用户列表
        selected_item = self.model[0].itemFromIndex(index)
        # 将选择的用户存储或文件
        self.ui.lab_userview.setText(selected_item.text())

    def select_1(self, index):
        # 选取管理员页面的文件列表
        selected_item = self.model[1].itemFromIndex(index)
        # 将选择的将要添加的文件存储
        self.ui.lab_folder.setText(selected_item.text())

    # 文件界面按钮
    def upview(self):
        files = File.get_all('Input')
        # 表明当前目录
        self.ui.lab_folder_2.setText('输入区')
        # 清除存储的文件名
        self.ui.lab_file.setText('无')
        # 清理现文件再添加
        self.model[2].clear()
        for file in files:
            item = QStandardItem(file)
            self.model[2].appendRow(item)
        self.ui.lv_folder_2.setModel(self.model[2])

    def downview(self):
        # 按照用户的列表过滤
        files = File.filter(self.file_cur)
        # 表明当前目录
        self.ui.lab_folder_2.setText('文件夹')
        # 清除存储的文件名
        self.ui.lab_file.setText('无')
        # 清理现文件再添加
        self.model[2].clear()
        for file in files:
            item = QStandardItem(file[0])
            self.model[2].appendRow(item)
        self.ui.lv_folder_2.setModel(self.model[2])

    def up(self):
        # 导入密钥
        key = self.user_cur[1]
        # 读取文件名
        file_cur = self.ui.lab_file.text()
        statue = File.up(file_cur, key)
        # 输出当前状态
        self.ui.lab_statue_2.setText(statue)
        # 在管理员文件夹注册
        Admin.up(file_cur, key)

    def down(self):
        # 读取文件名
        file_cur = self.ui.lab_file.text()
        # 导入密钥
        key = dict(self.file_cur)[file_cur]
        statue = File.down(file_cur, key)
        # 输出当前状态
        self.ui.lab_statue_2.setText(statue)

    def select_2(self, index):
        # 选取文件页面的列表
        selected_item = self.model[2].itemFromIndex(index)
        # 将选择的文件存储
        self.ui.lab_file.setText(selected_item.text())


# 运行
if __name__ == '__main__':
    app = QApplication()

    window = Main()
    window.show()
    app.exec()
