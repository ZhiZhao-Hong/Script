# /user/bin/python3
# -*- coding:utf-8 -*-
# @Time     :12/29/2018 1:19 PM
# @Author   :zhong
# @Software :PyCharm
import os
import shutil
from datetime import datetime


# 输入文件的路径
print("注意：你输入的路径的上级会自动创建一个文件夹用于存放提取的数据。")
while True:
    folder_dir = input('输入需要提取的文件目录，输入break单词则退出程序！:\n')
    if folder_dir == 'break':
        break
    else:
        if os.path.exists(folder_dir):
            if not os.listdir(folder_dir):
                print("该文件夹为空，重新输入：\n")
            else:
                break
        else:
            print("输入的文件路径不存在，重新输入：\n")


# 获取该文件目录的上级目录，用于存放抽取的文件
stored_folder = os.path.dirname(folder_dir) + '\\stored_folder_' + datetime.now().strftime('%Y%m%d%H%M%S')
os.makedirs(stored_folder)
endswith = '.3oxz'
search_list = [folder_dir]
count = 0


def list_dir(search_path):
    """查找该目录下所有的目录"""
    for file_name in os.listdir(search_path):
        new_search_path = os.path.join(search_path, file_name)
        if os.path.isdir(new_search_path):
            search_list.append(new_search_path)
            list_dir(new_search_path)


def find_file(search_path):
    """根据目录检索所有的"""
    global count
    for name in os.listdir(search_path):
        new_search_path = os.path.join(search_path, name)
        if os.path.isfile(new_search_path):
            shutil.copy(
                new_search_path,
                stored_folder+'\\'+name
            )
            print("成功提取：", name)
            count += 1


def main():
    print("正在检索该目录下所有的目录\n")
    list_dir(folder_dir)
    print("开始遍历所有的目录！\n")
    for search_path in search_list:
        find_file(search_path)
    print("提取结束，一共提取数据包个数为：", count)


if __name__ == '__main__':
    main()
