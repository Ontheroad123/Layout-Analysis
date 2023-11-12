1、数据预处理
    中英文分类: pdf_lang_classifier.py
    筛选出中文和英文: deal_jsonl.py
    随机选择pdf转png： random_engchi2png.py
2、使用预训练模型预测
    PaddlePaddle(cdla数据集训练)预训练模型做预测: Paddle_predict.py  
    CnSTD预训练模型预测： CnSTD_predict.py
    根据测试结果选择Paddle_predict.py
3、将预测结果转为labelme可编辑格式: paddlejson2labelme.py  
4、人工修改后，统一json格式以及矫正检测框（取修改后四点坐标的最大外接矩形为检测框，删除重复检测框）: check_json.py  

数据来源及labelme使用详情参考文档：https://www.yuque.com/heqiang-ybpcx/hytsuk/th70waup943c1peu?singleDoc# 《mnbvc-版面检测验证集》

