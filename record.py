import pyaudio
import wave
import numpy as np


        

#https://people.csail.mit.edu/hubert/pyaudio/

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "output.wav"

def record_audio_buffer(dev_index):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index = dev_index,
                    frames_per_buffer=CHUNK)


    #the bytes of the recording
    frames = []
    #records a chunk of audio (rate/chunk) for x seconds
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #stops the stream when done
    stream.stop_stream()
    stream.close()
    p.terminate()

    return np.frombuffer(b''.join(frames), dtype=np.int16)

def process_audio_buffer():
    return

def get_audio_transcription():
    return

if __name__ == "__main__":
    p = pyaudio.PyAudio()

    dev_index = None

    #find the realtek stereo mix (data from the realtek speaker output) to use as microphone
    for i in range(p.get_device_count()):
        dev = p.get_device_info_by_index(i)
        if (dev['name'] == 'Stereo Mix (Realtek(R) Audio)' and dev['hostApi'] == 0):
            dev_index = dev['index'];

    while True:
        audio = record_audio_buffer(dev_index)
        print(audio)

"""#converts bytes to a wav file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()"""
