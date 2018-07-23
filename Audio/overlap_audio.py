# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:52:37 2018

@author: Aishwarya Srivastava
"""

from pydub import AudioSegment
from pydub.playback import play
from rish import start_time_indices, end_time_indices
from begin import samplerate as sr


#audio1 = AudioSegment.from_file("today_later.wav") #your first audio file
#audio2 = AudioSegment.from_file("output_friday.wav") #your second audio file


#mixed = audio1.overlay(audio2)          #combine , superimpose audio files
         
#If you need to save mixed file
#mixed.export("mixed.wav", format='wav') #export mixed  audio file
#play(mixed)    

import contextlib
import wave

fname = 'stereo_file.wav'
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
import soundfile as sf
data, samplerate = sf.read('stereo_file.wav')
#data[0]=0.0
#print(data[70624])
k=0
data1, samplerate = sf.read('output_friday.wav')
for i in range(len(start_time_indices)):
    a=int(start_time_indices[i]*sr-1)
    b=int(end_time_indices[i]*sr-1)
    for j in range(a,b):
        data[j]=data1[k]
        k=k+1

import scipy.io.wavfile
scipy.io.wavfile.write('silenced_data1.wav',rate,data)


