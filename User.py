import File  # 导入文件操作模块
import Hash  # 导入哈希函数模块


# 定义注册函数
def registry(username, password):
    # 如果用户名是'admin'，并且'Users'文件夹不为空，则返回'fail'
    if username == 'admin':
        if not File.is_empty('Users'):
            return 'fail'
    # 如果用户已经存在，则返回'fail'
    if File.is_exist('Users', username + '.txt'):
        return 'fail'
    # 将用户名和密码写入文件
    user = username + '\n' + password + '\n'
    path = 'Users/' + username + '.txt'
    open(path, 'w').write(user)
    return 'success'


# 定义登录函数
def login(username, password):
    # 如果用户不存在，则返回'fail'
    if not File.is_exist('Users', username + '.txt'):
        return 'fail'
    # 读取用户文件，判断密码是否正确
    path = 'Users/' + username + '.txt'
    user = open(path, 'r').read().split('\n')
    if password in user:
        return 'success'
    else:
        return 'fail'


# 定义加载用户函数
def load(username):
    # 读取用户文件，并对密码进行哈希
    path = 'Users/' + username + '.txt'
    user = open(path, 'r').read().split('\n')
    user[1] = Hash.sha(user[1])
    return user


# 当前文件为主文件时，执行以下代码
if __name__ == '__main__':
    # 执行注册和登录函数，并输出结果
    print(registry('123', '123'))
    print(login('123', '123'))
