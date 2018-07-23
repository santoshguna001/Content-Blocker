# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 19:11:51 2018

@author: Santosh
"""

#from pydub import AudioSegment

#sound = AudioSegment.from_file(d)
#sound = sound.set_frame_rate(16000)
from pydub import AudioSegment


sound = AudioSegment.from_file("Recording.wav", format="wav")
sound = sound.set_channels(1)
sound.export('wave.wav', format='wav')

import soundfile as sf
data, samplerate = sf.read('wave.wav')
sf.write('stereo_file.wav', data, samplerate, subtype='PCM_16')