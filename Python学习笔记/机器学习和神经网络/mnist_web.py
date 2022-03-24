# 手写体识别，上传图片，输出识别结果

from pywebio.input import input,file_upload
from pywebio.output import put_text,put_image

from keras.models import load_model
import pandas as pd
import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import load_img

model = load_model('./model/3-model-lenet.h5')

# 处理图片，预测
def ocr(f1):
    img = load_img(f1,target_size=(28, 28),grayscale=True)
    i_img=[]
    import numpy as np
    img =image.img_to_array(img,dtype="uint8")
    i_img.append(img)
    # 发现训练集中的数据，都是黑底白字，而这里是白底黑字，于是先进行矩阵计算，实现图像的“反转”。
    np_image = 255 - np.array(i_img)
    np_image[np_image > 180] = 255
    np_image[np_image < 181] = 0
    r = np.argmax(model.predict(np_image), axis=-1)
    return r


# 图片上传目录
up_folder='./up/'

while True:
    f = file_upload("请选择一张包含一个手写数字的图片(白底黑字):")
    f1 = up_folder + f['filename']
    webfile = open(f1,'ab')
    webfile.write(f['content'])
    webfile.close()
    put_text('你上传的文件名是：' + f['filename']);
    put_image(open(f1, 'rb').read(),width='50px');
    # 识别并输出
    r = ocr(f1)
    put_text('AI模型的识别结果是：' + str(r[0]));

