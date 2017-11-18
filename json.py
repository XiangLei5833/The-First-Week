#!/usr/bin/env python3

''' json 是一种轻量级数据交换格式。互联网应用提供的API接口返回值基本都是 json 格式 '''

import json

courses = {1:'Linux', 2:'Vim', 3:'Git'}
json.dumps(courses)

with open('courses.json', 'w') as file:
    file.write(json.dumps(courses))

with open('courses.json', 'r') as file:
    new_courses = json.loads(file.read())
