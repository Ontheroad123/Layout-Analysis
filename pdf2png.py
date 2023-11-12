#将pdf转为png
from pdf2image import convert_from_path
import os 
import os.path as osp

savename = ''
pdfname = '100pdf_png'
for fil in os.listdir(pdfname):
  onepdf = osp.join(pdfname, fil)
  savepdf = osp.join(savename, fil)
  if not osp.exists(savepdf):
    os.makedirs(savepdf)
    pages = convert_from_path(onepdf, 300, savepdf, fmt='png', output_file='ok', thread_count=8)
   

