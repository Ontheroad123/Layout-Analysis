#将MNBVC项目中抽取的54篇pdf，每篇1/5页png，预测版面分析结果
#conda activate PaddlePaddle
import json 
import os 
import os.path as osp

import random 

pdfpath = './'
savepath = osp.join(pdfpath, '100pdf_png')#体检将扫描版pdf转成png
layout_path = osp.join(pdfpath, '100pdf_layout_pub')

for fil in os.listdir(savepath):
  pngpath = osp.join(savepath, fil)
  layout_path1 = osp.join(layout_path, fil)
  if not osp.exists(layout_path1):
    os.makedirs(layout_path1)
  for fil1 in os.listdir(pngpath):
    pngname = osp.join(pngpath, fil1)
    layout_name = osp.join(layout_path1, fil1)
    newjson = osp.join(layout_path1, fil1[:-3]+'json')
    if not osp.exists(newjson):
      
      os.system('python ./deploy/python/infer.py --model_dir=./output_inference/picodet_lcnet_x1_0_fgd_layout_infer/ --image_file={} --output_dir={} --device=CPU'.format(pngname, layout_path1))
      orijson = osp.join(layout_path1, 'bbox.json')
      if osp.exists(orijson):
        os.rename(orijson, newjson)
    #break 
  #break
