import numpy as np, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
x, sr = librosa.load('../songs/抓住我的自由-7_Shekels.mp3')
if sr not == 22050:
    print("sr is not 22050 but " + str(sr) + "!")
    return
y_harmonic, y_percussive = librosa.effects.hpss(x)
x = y_percussive
librosa.output.write_wav('../y_percussive.wav', y_percussive, sr)