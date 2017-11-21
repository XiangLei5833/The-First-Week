#!/usr/bin/env python3

import pickle

courses = {1:'Linux', 2:'Vim', 3:'Git'}
with open('./courses.date', 'wb') as file:   # 读取和写入都需要用二进制形式
    pickle.dump(courses, file)

with open('./courses.date', 'rb') as file:
    new_courses = pickle.load(file)

print(new_courses)
