#coding:utf-8
import os


path = '../output_data'
for item in os.listdir(path):
    print(item)
    file_path = os.path.join(path, item)
    f = open(file_path,"r")

    lines = f.readlines()

    if len(lines)==1:

        lines = "\n".join(lines)
        print(lines)
        ret_= lines.replace("\\n", "\n")
        ret_= ret_.replace('\\"', '\"')
        print(ret_)
        f = open(file_path,"w")
        f.write(ret_)

        f.flush()
        f.close()

