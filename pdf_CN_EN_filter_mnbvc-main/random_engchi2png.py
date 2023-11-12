#根据pdf分类结果，100本中54本包括英文，13本包括中文的，13本中文全部包含在54本英文pdf中，每篇pdf随机抽取1/5转成图片
#conda activate nlp
import json 
import os 
import os.path as osp
from pdf2image import convert_from_bytes
import random 

pdfpath = '/home/hq/workspace/pdf-parse/'
savepath = osp.join(pdfpath, '100pdf_png')
layout_path = osp.join(pdfpath, '100pdf_layout')
if not osp.exists(savepath):
  os.makedirs(savepath)
  os.makedirs(layout_path)
with open('eng_name.json', 'r') as fp:
  names =json.load(fp, strict=False)
  for name in names:
    pdfname = osp.join(pdfpath, name[3:])
    pngpath = osp.join(savepath, name.split('/')[-1])
    layputpath = osp.join(layout_path, name.split('/')[-1])
    print(pngpath)
    if not osp.exists(pngpath):
      os.makedirs(pngpath)
      os.makedirs(layputpath)
 
      images = convert_from_bytes(open(pdfname, 'rb').read())
      random_choice = 0 
      allpages = len(images)
      print(allpages)
      while random_choice<int(allpages/5):
        i = random.randint(0, allpages-1)
        image = images[i]
        random_choice+=1
        image.save(osp.join(pngpath, '%s.png' % i), 'PNG')
      
      print(pdfname)
    #break