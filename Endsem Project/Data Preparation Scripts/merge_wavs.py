import wave
from pydub import AudioSegment 
import os
from os import path
import subprocess
import glob
import csv 

MUSIC_PATH_1='./music_1s/'
MUSIC_PATH_2='./music_2s/'
MUSIC_PATH_3='./music_3s/'
MUSIC_PATH_4='./music_4s/'
MUSIC_PATH_5='./music_5s/'

SPEECH_PATH_1='./speech_1s/'
SPEECH_PATH_2='./speech_2s/'
SPEECH_PATH_3='./speech_3s/'
SPEECH_PATH_4='./speech_4s/'
SPEECH_PATH_5='./speech_5s/'

music_files_1 = glob.glob(MUSIC_PATH_1 + "/*.wav")
music_files_2 = glob.glob(MUSIC_PATH_2 + "/*.wav")
music_files_3 = glob.glob(MUSIC_PATH_3 + "/*.wav")
music_files_4 = glob.glob(MUSIC_PATH_4 + "/*.wav")
music_files_5 = glob.glob(MUSIC_PATH_5 + "/*.wav")

speech_files_1 = glob.glob(SPEECH_PATH_1 + "/*.wav")
speech_files_2 = glob.glob(SPEECH_PATH_2 + "/*.wav")
speech_files_3 = glob.glob(SPEECH_PATH_3 + "/*.wav")
speech_files_4 = glob.glob(SPEECH_PATH_4 + "/*.wav")
speech_files_5 = glob.glob(SPEECH_PATH_5 + "/*.wav")

silent_file_1 = './silent/silent_1s.wav'
silent_file_2 = './silent/silent_2s.wav'
silent_file_3 = './silent/silent_3s.wav'
silent_file_4 = './silent/silent_4s.wav'
silent_file_5 = './silent/silent_5s.wav'
silent_file_6 = './silent/silent_6s.wav'
silent_file_7 = './silent/silent_7s.wav'
silent_file_8 = './silent/silent_8s.wav'
silent_file_9 = './silent/silent_9s.wav'



f = open('./labels_updated', 'w' ,  newline='')
# create the csv writer
writer = csv.writer(f)

cnt=1


for i in range(0,30):
    m5 =music_files_5[i]
    s5=speech_files_5[i]
    
    f2=AudioSegment.from_wav(m5)+AudioSegment.from_wav(s5)

    row=['S'+str(cnt), 0,5,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 5,10,'speech']
    writer.writerow(row)
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



for i in range(30,60):
    m5 =music_files_5[i]
    s4=speech_files_4[i]
    sl1 = silent_file_1
    f2=AudioSegment.from_wav(m5)+AudioSegment.from_wav(sl1)+AudioSegment.from_wav(s4)

    row=['S'+str(cnt), 0,5,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 6,10,'speech']
    writer.writerow(row)
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 


for i in range(60,90):
    m4 =music_files_4[i]
    s5=speech_files_5[i]
    sl1 = silent_file_1
    f2=AudioSegment.from_wav(m4)+AudioSegment.from_wav(sl1)+AudioSegment.from_wav(s5)

    row=['S'+str(cnt), 0,4,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 5,10,'speech']
    writer.writerow(row)
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



for i in range(90,120):
    m3 =music_files_3[i]
    s5=speech_files_5[i]
    sl2 = silent_file_2
    f2=AudioSegment.from_wav(s5)+AudioSegment.from_wav(sl2)+AudioSegment.from_wav(m3)

    row=['S'+str(cnt), 0,5,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 7,10,'music']
    writer.writerow(row)
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(120,150):
    m4 =music_files_4[i]
    s4=speech_files_4[i]
    sl2 = silent_file_2
    f2=AudioSegment.from_wav(s4)+AudioSegment.from_wav(sl2)+AudioSegment.from_wav(m4)

    row=['S'+str(cnt), 0,4,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 6,10,'music']
    writer.writerow(row)
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(150,180):
    m5 =music_files_5[i]
    s3=speech_files_3[i]
    sl2 = silent_file_2
    f2=AudioSegment.from_wav(sl2)+AudioSegment.from_wav(s3)+AudioSegment.from_wav(m5)

    row=['S'+str(cnt), 2,5,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 5,10,'music']
    writer.writerow(row)
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



for i in range(180,210):
    m3 =music_files_3[i]
    s4=speech_files_4[i]
    sl3 = silent_file_3
    f2=AudioSegment.from_wav(m3)+AudioSegment.from_wav(sl3)+AudioSegment.from_wav(s4)

    row=['S'+str(cnt), 0,3 ,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 6,10,'speech']
    writer.writerow(row)
    
    
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(210,240):
    m5 =music_files_5[i]
    s2=speech_files_2[i]
    sl3 = silent_file_3
    f2=AudioSegment.from_wav(s2)+AudioSegment.from_wav(sl3)+AudioSegment.from_wav(m5)

    row=['S'+str(cnt), 0,2,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 5,10,'music']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(270,300):
    m1 =music_files_1[i]
    s5=speech_files_5[i]
    sl4 = silent_file_4
    f2=AudioSegment.from_wav(m1)+AudioSegment.from_wav(s5)+AudioSegment.from_wav(sl4)

    row=['S'+str(cnt), 0,1,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 1,6,'speech']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



for i in range(300,330):
    m4 =music_files_4[i]
    s2=speech_files_2[i]
    sl4 = silent_file_4
    f2=AudioSegment.from_wav(m4)+AudioSegment.from_wav(sl4)+AudioSegment.from_wav(s2)

    row=['S'+str(cnt), 0,4,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 8,10,'speech']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(330, 360):
    m5 =music_files_5[i]
    s1=speech_files_1[i]
    sl4 = silent_file_4
    f2=AudioSegment.from_wav(sl4)+AudioSegment.from_wav(s1)+AudioSegment.from_wav(m5)
    
    row=['S'+str(cnt), 4,5,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 5,10,'music']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(360, 390):
    m2 =music_files_2[i]
    sl2=silent_file_2
    s2=speech_files_2[i]
    s1=speech_files_1[i]
    m1 =music_files_1[i]

    f2=AudioSegment.from_wav(s2)+AudioSegment.from_wav(sl2)+AudioSegment.from_wav(m2)+AudioSegment.from_wav(sl2)+AudioSegment.from_wav(m1) +AudioSegment.from_wav(s1)
    row=['S'+str(cnt), 0,2,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 4,6,'music']
    writer.writerow(row)   
    row=['S'+str(cnt), 8,9,'music']
    writer.writerow(row)   
    row=['S'+str(cnt), 9,10,'speech']
    writer.writerow(row)
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



##########################################################################################################################
for i in range(390,420):
    m2 =music_files_2[i]
    m3 =music_files_3[i]
    s2=speech_files_2[i]
    s3=speech_files_3[i]
    
    f2=AudioSegment.from_wav(m2)+AudioSegment.from_wav(s2)+AudioSegment.from_wav(m3)+AudioSegment.from_wav(s3)

    row=['S'+str(cnt), 0,2,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 2,4,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 4,7,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 7,10,'speech']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



for i in range(420,450):
    m2 =music_files_2[i]
    m3 =music_files_3[i]
    s2=speech_files_2[i]
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(s2)+AudioSegment.from_wav(m3)+AudioSegment.from_wav(s3)+AudioSegment.from_wav(m2)
    row=['S'+str(cnt), 0,2,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 2,5,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 5,8,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 8,10,'music']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(450,480):
    m2 =music_files_2[i]
    m3 =music_files_3[i]
    sl2=silent_file_2
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(s3)+AudioSegment.from_wav(m2)+AudioSegment.from_wav(sl2)+AudioSegment.from_wav(m3)
    row=['S'+str(cnt), 0,3,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 3,5,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 7,10,'music']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(480,510):
    m2 =music_files_2[i]
    sl3=silent_file_3
    s2=speech_files_2[i]
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(s3)+AudioSegment.from_wav(sl3)+AudioSegment.from_wav(m2)+AudioSegment.from_wav(s2)
    row=['S'+str(cnt), 0,3,'speech']
    writer.writerow(row)

    row=['S'+str(cnt), 6,8,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 8,10,'speech']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(510,540):
    m3 =music_files_3[i]
    sl4=silent_file_4
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(s3)+AudioSegment.from_wav(sl4)+AudioSegment.from_wav(m3)
    row=['S'+str(cnt), 0,3,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 7,10, 'music']
    writer.writerow(row)

    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(540,570):
    m2 =music_files_2[i]
    sl3=silent_file_3
    s2=speech_files_2[i]
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(s3)+AudioSegment.from_wav(sl3)+AudioSegment.from_wav(m2)+AudioSegment.from_wav(s2)
    row=['S'+str(cnt), 0,3,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 6,8,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 8,10,'speech']
    writer.writerow(row)
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 


for i in range(570,600):
    m2 =music_files_2[i]
    sl3=silent_file_3
    s2=speech_files_2[i]
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(s3)+AudioSegment.from_wav(sl3)+AudioSegment.from_wav(m2)+AudioSegment.from_wav(s2)
    row=['S'+str(cnt), 0,3,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 6,8,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 8,10,'speech']
    writer.writerow(row)
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 


for i in range(600,630):
    m1 = music_files_1[i]
    sl3=silent_file_3
    s2=speech_files_2[i]
    s4=speech_files_4[-100]
    f2=AudioSegment.from_wav(s2)+AudioSegment.from_wav(sl3)+AudioSegment.from_wav(m1)+AudioSegment.from_wav(s4)
    row=['S'+str(cnt), 0,2,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 5,6,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 6,10,'speech']
    writer.writerow(row)
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(630,660):
    m1 = music_files_1[i]
    sl4=silent_file_4
    s1=speech_files_1[i]
    s4=speech_files_4[i-400]
    f2=AudioSegment.from_wav(s1)+AudioSegment.from_wav(sl4)+AudioSegment.from_wav(s4)+AudioSegment.from_wav(m1)
    row=['S'+str(cnt), 0,1,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 5,9,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 9,10,'music']
    
    writer.writerow(row)
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 



for i in range(660,690):
    m3 =music_files_3[i-300]
    sl2=silent_file_2
    s1=speech_files_1[i]
    s3=speech_files_3[i-400]
    m1 =music_files_1[i]
    f2=AudioSegment.from_wav(s3)+AudioSegment.from_wav(m1)+AudioSegment.from_wav(sl2)+AudioSegment.from_wav(s1)+AudioSegment.from_wav(m3)
    row=['S'+str(cnt), 0,3,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 3,4,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 6,7,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 7,10,'music']
    writer.writerow(row)
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(690,720):
    m3 =music_files_3[i-500]
    sl6=silent_file_6
    s1=speech_files_1[i]
   
    f2=AudioSegment.from_wav(m3)+AudioSegment.from_wav(sl6)+AudioSegment.from_wav(s1)
    row=['S'+str(cnt), 0,3,'music']
    writer.writerow(row)
    row=['S'+str(cnt), 9,10,'speech']
    writer.writerow(row)
   
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 

for i in range(720,750):
    m2 =music_files_2[i]
    sl6=silent_file_6
    s2=speech_files_2[i]
   
    f2=AudioSegment.from_wav(sl6)+AudioSegment.from_wav(s2)+AudioSegment.from_wav(m2)
    row=['S'+str(cnt), 6,8,'speech']
    writer.writerow(row)
    row=['S'+str(cnt), 8,10,'music']
    writer.writerow(row)   
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav") 


for i in range(0,30):
    sl9=silent_file_9
    s1=speech_files_1[i]
    f2=AudioSegment.from_wav(sl9)+AudioSegment.from_wav(s1)
    row=['S'+str(cnt), 9,10,'speech']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")

for i in range(30,60):
    sl8=silent_file_8
    s2=speech_files_2[i]
    f2=AudioSegment.from_wav(s2)+AudioSegment.from_wav(sl8)
    row=['S'+str(cnt), 1,2,'speech']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")

for i in range(60,90):
    sl7=silent_file_7
    s3=speech_files_3[i]
    f2=AudioSegment.from_wav(sl7)+AudioSegment.from_wav(s3)
    row=['S'+str(cnt), 7,10,'speech']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")

for i in range(90,120):
    sl6=silent_file_6
    s4=speech_files_4[i]
    f2=AudioSegment.from_wav(s4)+AudioSegment.from_wav(sl6)
    row=['S'+str(cnt), 1,4,'speech']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")



for i in range(120,150):
    sl5=silent_file_5
    s5=speech_files_5[i]
    f2=AudioSegment.from_wav(sl5)+AudioSegment.from_wav(s5)
    row=['S'+str(cnt), 5,10,'speech']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")


###############################################################################


for i in range(0,30):
    sl9=silent_file_9
    m1=music_files_1[i]
    f2=AudioSegment.from_wav(sl9)+AudioSegment.from_wav(m1)
    row=['S'+str(cnt), 9,10,'music']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")

for i in range(30,60):
    sl8=silent_file_8
    m2=music_files_2[i]
    f2=AudioSegment.from_wav(m2)+AudioSegment.from_wav(sl8)
    row=['S'+str(cnt), 1,2,'music']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")

for i in range(60,90):
    sl7=silent_file_7
    m3=music_files_3[i]
    f2=AudioSegment.from_wav(sl7)+AudioSegment.from_wav(m3)
    row=['S'+str(cnt), 7,10,'music']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")

for i in range(90,120):
    sl6=silent_file_6
    m4=music_files_4[i]
    f2=AudioSegment.from_wav(m4)+AudioSegment.from_wav(sl6)
    row=['S'+str(cnt), 1,4,'music']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")



for i in range(120,150):
    sl5=silent_file_5
    m5=music_files_5[i]
    f2=AudioSegment.from_wav(sl5)+AudioSegment.from_wav(m5)
    row=['S'+str(cnt), 5,10,'music']
    writer.writerow(row)
     
    wav_output='./dest/'+ 'S'+str(cnt)+'.wav'
    cnt=cnt+1
    f2.export(wav_output, format="wav")








# close the file
f.close()