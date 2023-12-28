# workflow范例代码
from XEdu.hub import Workflow as wf
# 实例化模型,"pose_face106"是脸部关键点检测
face = wf(task='pose_face106') 
img = 'face.jpg'
# 进行推理，同时返回结果和带标注图片
result,new_img = face.inference(data=img,img_type='cv2')
print(result) # 输出推理结果
face.show(new_img) # 显示带标注图片