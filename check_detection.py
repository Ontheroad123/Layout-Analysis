"""
check()某些json文件格式不对,因为不同版本的labelme保存的json格式略有差异,现在同意使用labelme=4.5.6版本的格式
modify_detection()检测框矫正时，四个坐标并非矩形，取四个坐标最小外接矩形,同时判断是否有重复的检测框，手动修改
"""

import json 

def check(jsonname):
  with open(jsonname, 'rb') as f:
    data = json.load(f)
    if 'lineColor' not in data.keys():
      data['lineColor'] = [0,255,0,128]
    if 'fillColor' not in data.keys():
      data['fillColor'] = [255,0,0,128]
    image_path = data['imagePath']
    if '/'  in image_path:
      image_path = image_path.split('/')[-1]
      data['imagePath'] = image_path

    for shape in data['shapes']:
      if 'line_color' not in shape.keys():
        shape['line_color'] = None
      if 'fill_color' not in shape.keys():
        shape['fill_color'] = None
      
    json.dump(data, open(jsonname, 'w'), ensure_ascii=False, indent=2)
#check('*.json')


import cv2
import numpy as np
def modify_detection(jsonname):
  with open(jsonname, 'rb') as f:
    data = json.load(f)
    is_repeat = []
    for shape in data['shapes']:
      points = shape['points']
      newpoints = []
      xpoints = []
      ypoints = []
      for i in range(len(points)): 
        xpoints.append(points[i][0])
        ypoints.append(points[i][1])
      newpoints.append([min(xpoints),min(ypoints)])
      newpoints.append([max(xpoints),min(ypoints)])
      newpoints.append([max(xpoints),max(ypoints)])
      newpoints.append([min(xpoints),max(ypoints)])
      if newpoints not in is_repeat:
        is_repeat.append(newpoints)
      else:
        print('newpoints:',newpoints, 'is_repeat:',is_repeat)
        print('repeat detection:', jsonname)
        break
      if newpoints != points:
        data['shapes'].remove(shape)
        shape['points'] = newpoints
        data['shapes'].append(shape)
    json.dump(data, open(jsonname, 'w'), ensure_ascii=False, indent=2)
#modify_detection('*.json')


path = ''
import os 
num = 0
for roots, dirs, files in os.walk(path):
  for fil in files:
    if fil.endswith('json'):
      num+=1
      jsonname = os.path.join(roots, fil)
      check(jsonname)
      modify_detection(jsonname)
print(num)
