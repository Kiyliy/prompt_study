import os
from pathlib import Path

file_suffix = '.py'
#不进行遍历的文件夹
# 黑名单列表,这些文件夹不会被遍历
FILE_DIR_BLACKLIST = [".git", ".idea", "__pycache__", "venv", "env", "node_modules"]


def generate_file_tree(root_dir):
    """
    生成指定目录下的文件树结构
    :param root_dir: 根目录路径
    :return: 文件树字符串
    """
    file_tree = ""
    for path, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in FILE_DIR_BLACKLIST]  # 过滤掉黑名单中的文件夹
        level = path.replace(root_dir, "").count(os.sep)
        folder_name = os.path.basename(path)
        file_tree += "|  " * level + "|--" + folder_name + "/\n"
        for f in files:
            if f.endswith(file_suffix):
                file_path = os.path.join(path, f)
                relative_path = os.path.relpath(file_path, root_dir)
                file_tree += "|  " * (level + 1) + "|--" + relative_path + "\n"
    return file_tree

if __name__ == "__main__":
    root_dir = input("请输入要生成文件树的根目录路径: ")

    if root_dir == "":
        root_dir = os.getcwd() 
    if not os.path.exists(root_dir):
        print("指定目录不存在")
        exit(1)
    file_tree = generate_file_tree(root_dir)
    print(file_tree)