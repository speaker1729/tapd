import User, File
from MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItem, QStandardItemModel


class Main(QMainWindow):
    # 主窗口类，继承自QMainWindow
    def __init__(self):
        super(Main, self).__init__()
        # 初始化父类
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 调用UI类的setupUi方法，将UI控件加载进来
        self.ui.pushButton.pressed.connect(self.registry)
        self.ui.pushButton_2.pressed.connect(self.login)
        self.ui.pushButton_3.pressed.connect(self.input_list)
        self.ui.pushButton_4.pressed.connect(self.data_list)
        self.ui.pushButton_5.pressed.connect(self.upload)
        self.ui.pushButton_6.pressed.connect(self.download)
        self.ui.listView.clicked.connect(self.select)
        # 绑定按钮点击事件和列表点击事件到对应的方法上
        #
        self.model = None
        self.user_cur = None
        self.file_cur = None
        # 初始化模型和当前用户以及当前文件

    def registry(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        statue = User.registry(username, password)
        self.ui.label_3.setText(statue)
        # 注册按钮点击事件对应的方法，获取用户名和密码，并调用User类的registry方法进行注册
        # 将User类的返回值设置为标签的文本

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        statue = User.login(username, password)
        self.ui.label_3.setText(statue + ' ' + username)
        if statue == 'success':
            self.user_cur = User.load(username)
        # 登录按钮点击事件对应的方法，获取用户名和密码，并调用User类的login方法进行登录
        # 如果返回值为'success'，则将当前用户设置为User.load(username)的返回值

    def input_list(self):
        files = File.get_all('Input')
        self.ui.label_4.setText('Input')
        self.model = QStandardItemModel()
        for file in files:
            item = QStandardItem(file)
            self.model.appendRow(item)
        self.ui.listView.setModel(self.model)
        # 输入文件列表按钮点击事件对应的方法，调用File类的get_all方法获取所有的输入文件
        # 将标签的文本设置为'Input'，并使用QStandardItemModel创建模型
        # 遍历所有文件名，将它们添加到模型中，并将模型设置到列表控件中

    def data_list(self):
        files = File.get_all('Data')
        self.ui.label_4.setText('Data')
        self.model = QStandardItemModel()
        for file in files:
            item = QStandardItem(file)
            self.model.appendRow(item)
        self.ui.listView.setModel(self.model)
        # 数据文件列表按钮点击事件对应的方法，调用File类的get_all方法获取所有的数据文件
        # 将标签的文本设置为'Data'，并使用QStandardItemModel创建模型
        # 遍历所有文件名，将它们添加到模型中，并将模型设置到列表控件中

    def upload(self):
        key = bytes.fromhex(self.user_cur[1])
        statue = File.up(self.file_cur, key)
        self.ui.label_4.setText('Input' + ' ' + statue)
        # 上传按钮点击事件对应的方法，获取当前用户的密钥，调用File类的up方法将当前文件上传
        # 将标签的文本设置为'Input'和File.up方法的返回值

    def download(self):
        key = bytes.fromhex(self.user_cur[1])
        statue = File.down(self.file_cur, key)
        self.ui.label_4.setText('Data' + ' ' + statue)
        # 下载按钮点击事件对应的方法，获取当前用户的密钥，调用File类的down方法将当前文件下载
        # 将标签的文本设置为'Data'和File.down方法的返回值

    def select(self, index):
        selected_item = self.model.itemFromIndex(index)
        self.file_cur = selected_item.text()
        # 列表点击事件对应的方法，获取当前选中的项，并将它的文本设置为当前文件名

if __name__ == '__main__':
    app = QApplication()

    window = Main()
    window.show()
    app.exec()
    # 如果当前文件被作为主程序运行，则创建QApplication，初始化主窗口并显示出来