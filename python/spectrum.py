# -*- coding: utf-8 -*-
from pydub import AudioSegment
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import get_ipython

path = os.getcwd()
name ="000615.mp3"

sound = AudioSegment.from_file(name)

#フーリエ変換
samples = np.array(sound.get_array_of_samples())
sample = samples[::sound.channels]

spec = np.fft.fft(sample)

freq = np.fft.fftfreq(sample.shape[0],1.0/sound.frame_rate)

#窓幅
w = 2000
#刻み
s = 500

#スペクトル格納用
ampList = []

#刻みずつずらしながら窓幅分のデータをフーリエ変換する
for i in range(int((sample.shape[0]- w) / s)):
    data = sample[i*s:i*s+w]
    spec = np.fft.fft(data)
    spec = spec[:int(spec.shape[0]/2)]
    spec[0] = spec[0] / 2
    ampList.append(np.abs(spec))


#周波数は共通なので１回だけ計算（縦軸表示に使う）  
freq = np.fft.fftfreq(data.shape[0], 1.0/sound.frame_rate)
freq = freq[:int(freq.shape[0]/2)]

#時間も共通なので１回だけ計算（横軸表示に使う）
time = np.arange(0, i+1, 1) * s / sound.frame_rate

#numpyの配列にしておく
ampList = np.array(ampList)

df_amp = pd.DataFrame(data=ampList, index=time, columns=freq)

#seabornのheatmapを使う
spectrum = sns.heatmap(data=np.log(df_amp.iloc[:, :100].T), 
            cbar = False,
            cmap=plt.cm.gist_rainbow_r,
           )
spectrum.axis("off")

sfig = spectrum.get_figure()
sfig.subplots_adjust(left=0, right=1, bottom=0, top=1)
sfig.savefig("spectrum%s.png"%(name),  orientation="landscape")