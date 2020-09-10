import os
import shutil


def move_file():

    # 输入要创建的文件夹的名字
    file_name = input('请输入要创建的文件夹名: ')

    path = r'H:\亿寻下载文件\Flask框架\{}'.format(file_name)

    # 在指定目录创建一个文件夹
    os.mkdir(path)

    # 返回该目录下的所有文件
    files = os.listdir(r'H:\亿寻下载文件')

    # 遍历该路径下的所有文件
    for file in files:

        # 将指定后缀的文件移动到前面创建号的文件夹中
        if os.path.splitext(file)[1] == '.ev4':
            print(file)
            shutil.move(r'H:\亿寻下载文件\{}'.format(file), path)
        else:
            pass


if __name__ == '__main__':
    move_file()