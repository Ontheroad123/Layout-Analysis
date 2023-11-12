1、pdf转为png: pdf2png.py  
2、使用PaddlePaddle(cdla数据集训练)预训练模型做预测: Paddle_predict.py  
3、将预测结果转为labelme可编辑格式: paddlejson2labelme.py  
4、人工修改后，统一json格式以及矫正检测框（取修改后四点坐标的最大外接矩形为检测框，删除重复检测框）: check_json.py  

数据来源及labelme使用详情参考文档：https://www.yuque.com/heqiang-ybpcx/hytsuk/th70waup943c1peu?singleDoc# 《mnbvc-版面检测验证集》

