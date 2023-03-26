import hashlib

# 定义sha256哈希函数
def sha(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hash_hex = hash_object.hexdigest() # 获取哈希值的16进制字符串表示
    return hash_hex

if __name__ == '__main__':
    res = sha('123')
    print(res) # 输出哈希值的16进制字符串表示
    print(type(res)) # 输出哈希值类型
    print(len(res)) # 输出哈希值的长度
