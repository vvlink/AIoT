# 多用户收集数据
import gradio as gr
import os


def image_mod(image):
    return image


demo = gr.Interface(
    image_mod,
    gr.Image(type="numpy",source="webcam"),
    "image",
    flagging_options=["1", "2", "3"],
)
'''
def snap(image, video):
    return [image, video]
demo = gr.Interface(
    snap,
    [gr.Image(source="webcam", tool=None), gr.Video(source="webcam")],
    ["image", "video"],)
'''

if __name__ == "__main__":
    demo.launch(server_name='0.0.0.0',share=True)