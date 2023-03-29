# onnx推理，输出类别和置信度
import onnxruntime as rt
import BaseData
import numpy as np

def get_tag(path):
    with open(path, 'r', encoding='utf-8') as f:
        tag = [e.rstrip("\n") for e in f.readlines()]
    return tag
def infer(img,pth,backbone):
    sess = rt.InferenceSession(pth, None)
    input_name = sess.get_inputs()[0].name
    out_name = sess.get_outputs()[0].name
    dt = BaseData.ImageData(img, backbone=backbone)
    input_data = dt.to_tensor()
    pred_onx = sess.run([out_name], {input_name: input_data})
    ort_output = pred_onx[0]
    idx = np.argmax(ort_output, axis=1)[0]
    return [idx,ort_output[0][idx]]
    
tag = get_tag('cls/dataset/imagenet.txt')
backbone='MobileNet'
img = 'cls/images/orange.JPG'
pth = 'cls/checkpoints/mobilenetv2.onnx'
idx,acc = infer(img,pth,backbone)
print('result:' + tag[idx] + ' , and acc:' + str(acc))
