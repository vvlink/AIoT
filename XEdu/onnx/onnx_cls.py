import onnxruntime as rt
import BaseData
import numpy as np

with open(r'cls/dataset/imagenet.txt', 'r', encoding='utf-8') as f:
    tag = [e.rstrip("\n") for e in f.readlines()]

sess = rt.InferenceSession('cls/checkpoints/imagenet.onnx', None)

input_name = sess.get_inputs()[0].name
out_name = sess.get_outputs()[0].name
dt = BaseData.ImageData('cls/images/orange.JPG', backbone='MobileNet')

input_data = dt.to_tensor()
pred_onx = sess.run([out_name], {input_name: input_data})
ort_output = pred_onx[0]
idx = np.argmax(ort_output, axis=1)[0]
print('result:' + tag[idx])
