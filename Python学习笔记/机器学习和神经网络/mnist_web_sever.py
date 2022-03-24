# 手写体识别，上传图片，输出识别结果
# 这是服务器版本

from pywebio.input import input,file_upload
from pywebio.output import put_text,put_image
from pywebio import start_server

from keras.models import load_model
import pandas as pd
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import load_img

model = load_model('./model/3-model-lenet.h5')

# 处理图片，预测
def ocr(f1):
    img = load_img(f1,target_size=(28, 28),grayscale=True)
    # 灰度转黑白
    # img = img.convert('L')
    i_img=[]
    import numpy as np
    img =image.img_to_array(img,dtype="uint8")
    i_img.append(img)
    image_output = image.array_to_img(i_img[0])
    image_output.save(f1 + '.1.png')
    # 发现训练集中的数据，都是黑底白字，而这里是白底黑字，于是先进行矩阵计算，实现图像的“反转”。
    np_image = 255 - np.array(i_img)
    np_image[np_image > 180] = 255
    np_image[np_image < 181] = 0
    image_output = image.array_to_img(np_image[0])
    image_output.save(f1 + '.2.png')
    r = np.argmax(model.predict(np_image), axis=-1)
    return r


# Web上传
up_folder='./up/'

def app():
    while True:
        f = file_upload("请选择一张包含一个手写数字的图片(白底黑字):")
        f1 = up_folder + f['filename']
        webfile = open(f1,'wb+') # 覆盖写入
        webfile.write(f['content'])
        webfile.close()
        put_text('你上传的文件名是：' + f['filename']);
        put_image(open(f1, 'rb').read(),width='50px');
        # 识别并输出
        r = ocr(f1)
        put_text('AI模型的识别结果是：' + str(r[0]));

start_server(app, port=8080, debug=True)
# f1 = './up/44.png'
# print(ocr(f1))

