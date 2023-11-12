#版面分析测试
#condad activate cnstd
from cnstd import LayoutAnalyzer, CATEGORY_DICT
import cv2 
from pdf2image import convert_from_path
import os 
import os.path as osp

savename = './mnbvc_pdf_png'
layoutname = './mnbvc_pdf_layout'
pdfname = '../100pdf/renamed-100/0001/0385.pdf'
if not osp.exists(savename):
  os.makedirs(savename)
  os.makedirs(layoutname)
pages = convert_from_path(pdfname, 300, savename, fmt='png', output_file='ok', thread_count=8)
for fil1 in os.listdir(savename):
  img_fp = osp.join(savename, fil1)
  img0 = cv2.imread(img_fp)
  analyzer = LayoutAnalyzer('layout')
  #out = analyzer.analyze(img_fp, resized_shape=(2336,1632))
  out = analyzer.analyze(img_fp)
  analyzer.save_img(img0, out, osp.join(layoutname, fil1))
  #break

