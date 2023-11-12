#将paddleocr中版面分析预测的json文件转成labelme能读取的格式
#cdla模型的预测结果
import json 
import os 
import os.path as osp
import shutil
from PIL import Image, ImageDraw
import cv2

class LabelmeItem:
    def __init__(self, img_path):
        # labelme字段
        self.version = "4.5.6"
        self.flags = {}
        
        self.shapes = []
        self.lineColor = [0, 255, 0, 128]
        self.fillColor = [255, 0, 0, 128]
        self.imagePath = img_path
        self.imageData = None
        
        # 自定义字段
        #self.label_liver = label  # 标签前缀
        #self.labell_id = 1  # 标签后缀id
        #self.lable_ganlie = 'g'
        #self.labelg_id = 1

    def add_shape(self, contours, label):
        # 把cv2的contours转换为labelme的points
        shape = {}
        points = contours
        
        shape['label'] = label
        shape['line_color'] = None
        shape['fill_color'] = None
        shape['points'] = points
        shape['shape_type'] = "polygon"
        shape['flags'] = {}
        self.shapes.append(shape)

    def save_json(self, save_dir, h, w):
        save_path = save_dir
        instance = {}
        instance['version'] = "4.5.6"
        instance['flags'] = {}
        instance['shapes'] = self.shapes
        instance['lineColor'] = self.lineColor
        instance['fillColor'] = self.fillColor
        instance['imagePath'] = self.imagePath
        instance['imageData'] = self.imageData

        instance['imageHeight'] = h
        instance['imageWidth'] = w
        print(len(self.shapes))
        if len(self.shapes) > 0:
            json.dump(instance, open(save_path, 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)  # indent=2 更加美观显示

def convert_json(newpng, jsonname, newjson, h, w):
  item = LabelmeItem(newpng)
  with open(jsonname) as f: 
    infos = json.load(f, strict=False)
    for info in infos:
      print(info)
      flag = info['category_id']
      #id2class
      label = dicts[flag]
      bbox = info['bbox']
      print(bbox)
      newboxx = []
      newboxx.append((bbox[0], bbox[1]))
      newboxx.append((bbox[0], bbox[1]+bbox[3]))
      newboxx.append((bbox[0]+bbox[2], bbox[1]+bbox[3]))
      newboxx.append((bbox[0]+bbox[2], bbox[1]))
      #newboxx.append((bbox[0], bbox[1]))
      item.add_shape(newboxx, label)
  item.save_json(newjson, h, w)
    
dicts = ['text', 'title', 'figure', 'figure_caption', 'table', 'table_caption', 'header', 'footer', 'reference', 'equation']

pngpath = './100pdf_png'
layout_path = './100pdf_layout_cdla'
label_path = './100pdf_labelme'
for fil in os.listdir(layout_path):
  layout_path1 = osp.join(layout_path, fil)
  label_path1 = osp.join(label_path, fil)
  if not osp.exists(label_path1):
    os.makedirs(label_path1)
  for fil1 in os.listdir(layout_path1):
    if fil1.endswith('json'):
      pngname = osp.join(pngpath, fil, fil1[:-4]+'png')
      newpng = osp.join(label_path1, fil1[:-4]+'png')
      print(pngname)
      print(cv2.imread(pngname, 0).shape)
      height, width = cv2.imread(pngname, 0).shape
      shutil.copy(pngname, newpng)
      jsonname = osp.join(layout_path1, fil1)
      newjson = osp.join(label_path1, fil1)
      print(jsonname)
      print(newjson)
      convert_json(newpng, jsonname, newjson, height, width)
      #break 
  #break
