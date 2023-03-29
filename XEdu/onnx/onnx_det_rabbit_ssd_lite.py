import onnxruntime as rt
import cv2
import BaseData

sess = rt.InferenceSession('det/checkpoints/rabbit.onnx', None)

input_name = sess.get_inputs()[0].name
output_names = [o.name for o in sess.get_outputs()]

image = cv2.imread('det/images/rabbit.JPG')
image = cv2.resize(image, (320, 320))
dt = BaseData.ImageData(image, backbone='SSD_Lite')

input_data = dt.to_tensor()

outputs = sess.run(output_names, {input_name: input_data})

boxes = outputs[0]
labels = outputs[1][0]
img_height, img_width = image.shape[:2]
size = min([img_height, img_width]) * 0.001
text_thickness = int(min([img_height, img_width]) * 0.001)

idx = 0
for box in zip(boxes[0]):
    x1, y1, x2, y2, score = box[0]
    label = 'rabbit'
    idx = idx + 1
    caption = f'{label}{int(score * 100)}%'
    if score >= 0.50:
        (tw, th), _ = cv2.getTextSize(text=caption, fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                      fontScale=size, thickness=text_thickness)
        th = int(th * 1.2)
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(image, caption, (int(x1), int(y1)),
                    cv2.FONT_HERSHEY_SIMPLEX, size, (255, 255, 255), text_thickness, cv2.LINE_AA)

# image = cv2.resize(image, None, fx=3, fy=3)
cv2.imshow('result', image)
cv2.waitKey(0)
