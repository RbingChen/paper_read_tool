#coding:utf-8
import os

def list_files_only(directory):
    """仅列出目录中的文件（不包括子目录）"""
    try:
        # 获取所有条目
        all_items = os.listdir(directory)

        # 筛选出文件
        files = [item for item in all_items
                 if os.path.isfile(os.path.join(directory, item))]

        # print(f"目录 '{directory}' 中的文件:")
        # for file in files:
        #     print(f"  - {file}")
        return files
    except FileNotFoundError:
        print(f"错误: 目录 '{directory}' 不存在")
        return []
    except NotADirectoryError:
        print(f"错误: '{directory}' 不是目录")
        return []
    except PermissionError:
        print(f"错误: 没有权限访问目录 '{directory}'")
        return []
