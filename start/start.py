import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK=1024
RATE=8000

def spectrum_trans(input):

    hammingWindow = np.hamming(CHUNK)
    input = hammingWindow * input

    # 高速フーリエ変換
    F = np.fft.fft(input)


    # 振幅スペクトルを計算
    Amp = np.abs(F)
    # Amp =  [np.sqrt(c.real ** 2 + c.imag ** 2) for c in F]

    return Amp


def start_conversation():
    
    p=pyaudio.PyAudio()

    stream=p.open(    format = pyaudio.paInt16,
            channels = 1,
            rate = RATE,
            frames_per_buffer = CHUNK,
            input = True,
            output = True) # inputとoutputを同時にTrueにする


    # plt.ion()
    # plt.figure()
    # x = np.fft.fftfreq(CHUNK, d=1.0/RATE)
    # print(len(x))
    # plt.ylim(0, 3)
    # plt.xlim(0, 4000)
    # li, = plt.plot(x, np.zeros(len(x)))

    while stream.is_active():

        input = stream.read(CHUNK)

        y = np.frombuffer(input, dtype="int16") / 32768.0  # -1 - +1に正規化
        spec = spectrum_trans(y)
        # li.set_ydata(spec)

        leng = len(spec)
        half = len(spec)/2
        start = int(leng*100/RATE)
        end = int(leng*1000/RATE)

        if np.amax(spec[start:end]) > 1.0:
            print("You can call Lam.")
            return True

        # plt.pause(.01)

        # output = stream.write(input)


start_conversation()
