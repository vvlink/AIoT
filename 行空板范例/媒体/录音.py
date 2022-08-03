from unihiker import Audio
import time

audio = Audio() #实例化音频

print("环境音大小")
for i in range(30):
    print(audio.sound_level())
    time.sleep(0.1)


print("录音3秒")
audio.record('3s.wav', 3) #录音3秒，存到文件3s.wav中

print("开始录音")
audio.start_record('6s.wav') #后台开始录音，存到文件6s.wav中
print("等待6秒")
time.sleep(6) #等待6秒
audio.stop_record() #停止录音
print("停止录音")
