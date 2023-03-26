import os
import AES


# 定义获取文件夹中所有文件名的函数
def get_all(folder):
    path = folder
    files = os.listdir(path)
    return files


# 定义判断文件夹是否为空的函数
def is_empty(folder):
    path = folder
    files = os.listdir(path)
    if len(files):
        return False
    else:
        return True


# 定义判断文件是否在文件夹中存在的函数
def is_exist(folder, file):
    path = folder
    files = os.listdir(path)
    if file in files:
        return True
    else:
        return False


# 定义上传文件的函数
def up(file, key):
    path = 'Input/'
    files = os.listdir(path)
    if file not in files:
        return 'fail'
    if is_exist('Data', file):
        return 'fail'
    else:
        defile = open(path + file, 'rb')
        enfile = AES.encrypt(key, defile.read()) # 对文件进行加密
        defile.close()
        res = open('Data/' + file, 'wb')
        res.write(enfile) # 将加密后的文件写入到指定文件夹中
        res.close()
        return 'success'


# 定义下载文件的函数
def down(file, key):
    path = 'Data/'
    files = os.listdir(path)
    if file not in files:
        return 'fail'
    if is_exist('Output', file):
        return 'fail'
    else:
        enfile = open(path + file, 'rb')
        defile = AES.decrypt(key, enfile.read()) # 对文件进行解密
        enfile.close()
        res = open('Output/' + file, 'wb')
        res.write(defile) # 将解密后的文件写入到指定文件夹中
        res.close()
        return 'success'


if __name__ == '__main__':
    # print(is_empty('Users'))
    # print(is_exist('Users','123'))
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
    print(up('test', key))
    print(down('test', key))
    pass