#MNBVC项目中100本pdf分类结果，筛选包含中文或者英文的页面，没有找到合适的中文pdf用于测试，很多pdf包含中英文
import json 
import jsonlines
fp = open('./pdf_classification.jsonl', 'r')
books_info = {}
for info in jsonlines.Reader(fp):
  print(info)
  #break
  name = info['file_path']
  text_only = info['text_only']
  if text_only ==1:
    language = info['language_type']
    #print(language)
    if name not in books_info.keys():
      books_info[name] = set()
    #print(books_info)
    for lang in language:
      books_info[name].add(lang)
    #break
print(books_info)
print(len(books_info.keys()))
eng_name = []
chi_name = []
for key in books_info.keys():
  values =list(books_info[key])
  
  for value in values:
    if value == 'Language.ENGLISH':
      #print('unclude english:', key)
      eng_name.append(key)
      #break
    if value == 'Language.CHINESE':
      print('unclude chinese:', key)
      chi_name.append(key)
      #break
print('eng num:', len(eng_name))
print('chi num', len(chi_name))
json.dump(eng_name, open('eng_name.json', 'w'))
json.dump(chi_name, open('chi_name.json', 'w'))

c_e = 0
for chi in chi_name:
  if chi in eng_name:
    c_e+=1
print(c_e)
