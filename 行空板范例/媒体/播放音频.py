from unihiker import Audio
import time

audio = Audio() #实例化音频

print("播放3s的音频")
audio.play('3s.wav')
print("播放完成")

print("开始播放6秒的音频")
audio.start_play('6s.mp3')

for i in range(2):
    remain_time = audio.play_time_remain()
    print("剩余时间:" + str(remain_time))
    time.sleep(1)

print("暂停播放")
audio.pause_play()
for i in range(2):
    remain_time = audio.play_time_remain()
    print("剩余时间:" + str(remain_time))
    time.sleep(1)

print("继续播放")
audio.resume_play()
for i in range(2):
    remain_time = audio.play_time_remain()
    print("剩余时间:" + str(remain_time))
    time.sleep(1)

print("停止播放")
audio.stop_play()
print("结束播放")
