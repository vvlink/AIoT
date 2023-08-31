# 录制音频
import pyaudio
# 数据流块大小
CHUNK = 1024
# 位数
FORMAT = pyaudio.paInt16
# 声道
CHANNELS = 1
# 频率：16000
RATE = 16000
# 声音长度，单位秒
record_second = 5
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print("录音开始")
frames = []
for i in range(0, int(RATE / CHUNK * record_second)):
    data = stream.read(CHUNK)
    frames.append(data)
stream.stop_stream()
stream.close()
print("录音结束")