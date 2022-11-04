import wave
from pydub import AudioSegment 
import os
from os import path
import subprocess
import glob


MUSIC_PATH='./music_wav/'
music_files = glob.glob(MUSIC_PATH + "/*.wav")
print(len(music_files))

cnt=0

for waveFileName in music_files:
    tstart=0
    for i in range(7):
        newAudio = AudioSegment.from_wav(waveFileName)
        #print(len(newAudio))
        newAudio = newAudio[tstart:tstart+4000]
        wav_output='./music_4s/'+ 'music_4s_'+str(cnt)+'.wav'
        cnt=cnt+1
        tstart=tstart+4000
        newAudio.export(wav_output, format="wav") 

