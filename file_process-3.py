#!/usr/bin/env python3

''' copy file '''

import sys

def copy_file(src, dst):
    with open(src, 'r') as src_file:
        with open(dst, 'w') as dst_file:
            dst_file.write(src_file.read())

if __name__ == '__main__':
    if len(sys.argv) == 3:
        copy_file(sys.argv[1], sys.argv[2])
        print(sys.argv[0], 'srcfile dstfile') 
        sys.exit(-1)
    sys.exit(0)     # sys.exit()是告诉系统退出，负数，0为安全退出，正数为异常退出
