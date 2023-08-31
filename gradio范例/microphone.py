import os
import numpy as np
import gradio as gr


# 输入麦克风的音频，输出反向后的音频
def reverse_audio(audio):
    sr, data = audio
    return (sr, np.flipud(data))


demo = gr.Interface(fn=reverse_audio, 
                    inputs="microphone", 
                    outputs="audio", 
                    examples=[
                    "https://samplelib.com/lib/preview/mp3/sample-3s.mp3"], 
                    cache_examples=True,
                    allow_flagging="never")

if __name__ == "__main__":
    demo.launch()